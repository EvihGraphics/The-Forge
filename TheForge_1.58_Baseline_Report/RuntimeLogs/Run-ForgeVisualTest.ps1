param(
    [Parameter(Mandatory=$true)][string]$ExePath,
    [Parameter(Mandatory=$true)][string]$OutputDir,
    [Parameter(Mandatory=$true)][string]$ScreenshotPath,
    [string]$Arguments = "",
    [int]$StartupWaitSeconds = 14,
    [int]$MaxWaitSeconds = 35,
    [int]$CloseWaitSeconds = 6
)

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $ScreenshotPath) | Out-Null

$stdout = Join-Path $OutputDir "stdout.txt"
$stderr = Join-Path $OutputDir "stderr.txt"
$meta = Join-Path $OutputDir "run_metadata.txt"
$start = Get-Date

$signature = @"
using System;
using System.Runtime.InteropServices;
public static class Win32Capture {
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr hWnd, IntPtr hdcBlt, uint nFlags);
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
}
"@

Add-Type -TypeDefinition $signature -ErrorAction SilentlyContinue
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$p = $null
$status = "UNKNOWN"
$exitCode = ""
$windowTitle = ""
$windowHandle = 0
$captureStatus = "NOT_CAPTURED"
$captureError = ""

try {
    $psiArgs = @{
        FilePath = $ExePath
        WorkingDirectory = (Split-Path -Parent $ExePath)
        PassThru = $true
        RedirectStandardOutput = $stdout
        RedirectStandardError = $stderr
    }
    if ($Arguments -ne "") {
        $psiArgs.ArgumentList = $Arguments
    }
    $p = Start-Process @psiArgs

    $deadline = (Get-Date).AddSeconds($MaxWaitSeconds)
    do {
        Start-Sleep -Milliseconds 500
        $p.Refresh()
        if ($p.HasExited) { break }
        if ($p.MainWindowHandle -ne 0) { break }
    } while ((Get-Date) -lt $deadline)

    if ($p.HasExited) {
        $status = "EXITED_BEFORE_CAPTURE"
        $exitCode = $p.ExitCode
    } elseif ($p.MainWindowHandle -eq 0) {
        $status = "NO_WINDOW"
    } else {
        $status = "WINDOW_READY"
        $windowHandle = $p.MainWindowHandle.ToInt64()
        $windowTitle = $p.MainWindowTitle
        [Win32Capture]::ShowWindow($p.MainWindowHandle, 9) | Out-Null
        [Win32Capture]::SetForegroundWindow($p.MainWindowHandle) | Out-Null
        Start-Sleep -Seconds $StartupWaitSeconds
        $p.Refresh()

        if (-not $p.HasExited -and $p.MainWindowHandle -ne 0) {
            $rect = New-Object Win32Capture+RECT
            if ([Win32Capture]::GetWindowRect($p.MainWindowHandle, [ref]$rect)) {
                $width = [Math]::Max(1, $rect.Right - $rect.Left)
                $height = [Math]::Max(1, $rect.Bottom - $rect.Top)
                $bmp = New-Object System.Drawing.Bitmap($width, $height)
                $g = [System.Drawing.Graphics]::FromImage($bmp)
                $hdc = $g.GetHdc()
                $printed = [Win32Capture]::PrintWindow($p.MainWindowHandle, $hdc, 2)
                $g.ReleaseHdc($hdc)
                if (-not $printed) {
                    $g.CopyFromScreen($rect.Left, $rect.Top, 0, 0, (New-Object System.Drawing.Size($width, $height)))
                    $captureStatus = "CAPTURED_WINDOW_COPYFROMSCREEN"
                } else {
                    $captureStatus = "CAPTURED_WINDOW_PRINTWINDOW"
                }
                $bmp.Save($ScreenshotPath, [System.Drawing.Imaging.ImageFormat]::Png)
                $g.Dispose()
                $bmp.Dispose()
            } else {
                $captureStatus = "CAPTURE_FAILED"
                $captureError = "GetWindowRect failed"
            }
        } else {
            $status = "EXITED_BEFORE_CAPTURE_AFTER_WAIT"
            if ($p.HasExited) { $exitCode = $p.ExitCode }
        }
    }
}
catch {
    $status = "EXCEPTION"
    $captureError = $_.Exception.Message
}
finally {
    if ($p -ne $null) {
        try {
            $p.Refresh()
            if (-not $p.HasExited) {
                $p.CloseMainWindow() | Out-Null
                if (-not $p.WaitForExit($CloseWaitSeconds * 1000)) {
                    Stop-Process -Id $p.Id -Force
                    $status = "$status;FORCE_KILLED"
                } else {
                    $status = "$status;CLOSED"
                }
            }
            $p.Refresh()
            if ($p.HasExited) { $exitCode = $p.ExitCode }
        } catch {
            $captureError = "$captureError CloseError=$($_.Exception.Message)"
        }
    }

    $end = Get-Date
    @(
        "ExePath=$ExePath",
        "Arguments=$Arguments",
        "WorkingDirectory=$(Split-Path -Parent $ExePath)",
        "Start=$($start.ToString('o'))",
        "End=$($end.ToString('o'))",
        "Status=$status",
        "ExitCode=$exitCode",
        "WindowHandle=$windowHandle",
        "WindowTitle=$windowTitle",
        "CaptureStatus=$captureStatus",
        "CapturePath=$ScreenshotPath",
        "CaptureError=$captureError"
    ) | Set-Content -LiteralPath $meta -Encoding UTF8
}

Get-Content -LiteralPath $meta
