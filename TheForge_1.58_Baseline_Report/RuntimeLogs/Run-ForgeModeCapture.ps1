param(
    [Parameter(Mandatory=$true)][string]$ExePath,
    [Parameter(Mandatory=$true)][string]$OutputDir,
    [Parameter(Mandatory=$true)][string]$ScreenshotPath,
    [Parameter(Mandatory=$true)][int]$ModeIndex,
    [string]$Arguments = "--d3d12 --no-auto-exit",
    [int]$StartupWaitSeconds = 8,
    [int]$StabilizeSeconds = 5,
    [int]$MaxWaitSeconds = 45,
    [int]$CloseWaitSeconds = 8
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
public static class ForgeModeCaptureWin32 {
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr hWnd, IntPtr hdcBlt, uint nFlags);
    [DllImport("user32.dll")] public static extern bool SetCursorPos(int X, int Y);
    [DllImport("user32.dll")] public static extern void mouse_event(uint dwFlags, uint dx, uint dy, uint dwData, UIntPtr dwExtraInfo);
    [DllImport("user32.dll")] public static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
}
"@

Add-Type -TypeDefinition $signature -ErrorAction SilentlyContinue
Add-Type -AssemblyName System.Drawing

function Invoke-Click([int]$x, [int]$y) {
    [ForgeModeCaptureWin32]::SetCursorPos($x, $y) | Out-Null
    Start-Sleep -Milliseconds 150
    [ForgeModeCaptureWin32]::mouse_event(0x0002, 0, 0, 0, [UIntPtr]::Zero)
    Start-Sleep -Milliseconds 80
    [ForgeModeCaptureWin32]::mouse_event(0x0004, 0, 0, 0, [UIntPtr]::Zero)
}

function Invoke-Key([byte]$vk) {
    [ForgeModeCaptureWin32]::keybd_event($vk, 0, 0, [UIntPtr]::Zero)
    Start-Sleep -Milliseconds 60
    [ForgeModeCaptureWin32]::keybd_event($vk, 0, 0x0002, [UIntPtr]::Zero)
}

$p = $null
$status = "UNKNOWN"
$exitCode = ""
$windowTitle = ""
$windowHandle = 0
$captureStatus = "NOT_CAPTURED"
$captureError = ""
$selectedMode = $ModeIndex

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
        [ForgeModeCaptureWin32]::ShowWindow($p.MainWindowHandle, 9) | Out-Null
        [ForgeModeCaptureWin32]::SetForegroundWindow($p.MainWindowHandle) | Out-Null
        Start-Sleep -Seconds $StartupWaitSeconds

        $rect = New-Object ForgeModeCaptureWin32+RECT
        if ([ForgeModeCaptureWin32]::GetWindowRect($p.MainWindowHandle, [ref]$rect)) {
            $dropdownX = $rect.Left + 345
            $dropdownY = $rect.Top + 468
            Invoke-Click $dropdownX $dropdownY
            Start-Sleep -Milliseconds 300
            Invoke-Key 0x24
            Start-Sleep -Milliseconds 100
            for ($i = 0; $i -lt $ModeIndex; ++$i) {
                Invoke-Key 0x28
                Start-Sleep -Milliseconds 80
            }
            Invoke-Key 0x0D
            Start-Sleep -Seconds $StabilizeSeconds

            $p.Refresh()
            if (-not $p.HasExited -and $p.MainWindowHandle -ne 0) {
                $rect = New-Object ForgeModeCaptureWin32+RECT
                if ([ForgeModeCaptureWin32]::GetWindowRect($p.MainWindowHandle, [ref]$rect)) {
                    $width = [Math]::Max(1, $rect.Right - $rect.Left)
                    $height = [Math]::Max(1, $rect.Bottom - $rect.Top)
                    $bmp = New-Object System.Drawing.Bitmap($width, $height)
                    $g = [System.Drawing.Graphics]::FromImage($bmp)
                    $hdc = $g.GetHdc()
                    $printed = [ForgeModeCaptureWin32]::PrintWindow($p.MainWindowHandle, $hdc, 2)
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
                    $captureError = "GetWindowRect failed after mode selection"
                }
            } else {
                $status = "EXITED_BEFORE_CAPTURE_AFTER_WAIT"
                if ($p.HasExited) { $exitCode = $p.ExitCode }
            }
        } else {
            $captureStatus = "CAPTURE_FAILED"
            $captureError = "Initial GetWindowRect failed"
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
        "ModeIndex=$selectedMode",
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
