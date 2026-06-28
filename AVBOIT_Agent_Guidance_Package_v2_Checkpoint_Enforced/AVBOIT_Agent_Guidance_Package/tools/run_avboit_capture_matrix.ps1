param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$ResultRoot = "",
    [string]$ExePath = "",
    [ValidateSet("runtime", "analytic-dx12", "analytic-vulkan", "default-smoke")]
    [string]$Phase = "runtime",
    [int]$TimeoutSeconds = 120,
    [int]$CaptureFrame = 60,
    [string]$CommitSha = ""
)

$ErrorActionPreference = "Stop"

function New-Directory([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Force -Path $Path | Out-Null
    }
}

function Quote-Arg([string]$Arg) {
    if ($Arg -match '[\s"]') {
        return '"' + ($Arg -replace '"', '\"') + '"'
    }
    return $Arg
}

function Join-Args([string[]]$LaunchArgs) {
    return ($LaunchArgs | ForEach-Object { Quote-Arg $_ }) -join ' '
}

function Api-Arg([string]$Api) {
    if ($Api -eq "Vulkan") { return "--vulkan" }
    return "--d3d12"
}

function Invoke-AvboitLaunch {
    param(
        [string]$Name,
        [string[]]$LaunchArgs,
        [string]$OutputDir
    )

    New-Directory $OutputDir
    $bootstrapDir = Join-Path $OutputDir "bootstrap"
    New-Directory $bootstrapDir
    $stdoutPath = Join-Path $OutputDir "$Name.stdout.txt"
    $stderrPath = Join-Path $OutputDir "$Name.stderr.txt"

    $beforePngInfo = @{}
    Get-ChildItem -LiteralPath $OutputDir -Filter "*.png" -ErrorAction SilentlyContinue | ForEach-Object {
        $beforePngInfo[$_.FullName] = $_.LastWriteTimeUtc
    }
    $beforeBootstrap = @(Get-ChildItem -LiteralPath $bootstrapDir -Filter "*.log" -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName })
    $fullArgs = @($LaunchArgs + @("--avboit-bootstrap-log-dir=$bootstrapDir"))
    $argLine = Join-Args $fullArgs
    $startTime = Get-Date
    $classification = "UNKNOWN"
    $pidText = ""
    $exitCodeText = ""
    $runtimeMs = 0
    $processCreated = $false

    try {
        $process = Start-Process -FilePath $ExePath -ArgumentList $argLine -WorkingDirectory (Split-Path -Parent $ExePath) `
            -PassThru -WindowStyle Hidden -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath
        $processCreated = $true
        $pidText = [string]$process.Id
        $finished = $process.WaitForExit($TimeoutSeconds * 1000)
        $runtimeMs = [int]((Get-Date) - $startTime).TotalMilliseconds
        if (-not $finished) {
            $classification = "APP_HUNG_OR_CAPTURE_TIMEOUT"
            try { Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue } catch {}
        } else {
            $process.Refresh()
            if ($null -eq $process.ExitCode) {
                $process.WaitForExit()
                $process.Refresh()
            }
            $exitCodeText = [string]$process.ExitCode
            if ($process.ExitCode -eq 0) {
                $classification = "APP_EXITED_ZERO"
            } else {
                $classification = "APP_EXITED_NONZERO"
            }
        }
    } catch {
        $runtimeMs = [int]((Get-Date) - $startTime).TotalMilliseconds
        $classification = "PROCESS_CREATION_FAILED"
        $exitCodeText = $_.Exception.GetType().FullName
        Set-Content -Path $stderrPath -Value $_.Exception.ToString() -Encoding UTF8
    }

    $newPng = @(Get-ChildItem -LiteralPath $OutputDir -Filter "*.png" -ErrorAction SilentlyContinue | Where-Object {
        (-not $beforePngInfo.ContainsKey($_.FullName)) -or ($_.LastWriteTimeUtc -gt $beforePngInfo[$_.FullName])
    } | ForEach-Object { $_.FullName })
    $bootstrapLogs = @(Get-ChildItem -LiteralPath $bootstrapDir -Filter "*.log" -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName })
    $newBootstrapLogs = @($bootstrapLogs | Where-Object { $beforeBootstrap -notcontains $_ })
    $bootstrapText = ""
    foreach ($log in $newBootstrapLogs) {
        $bootstrapText += (Get-Content -LiteralPath $log -Raw -ErrorAction SilentlyContinue)
    }
    if ($classification -eq "APP_HUNG_OR_CAPTURE_TIMEOUT" -and $newPng.Count -gt 0) {
        $classification = "SCRIPT_WAIT_FAILURE_OR_LATE_EXIT"
    }
    if ($classification -eq "APP_EXITED_ZERO" -and $newPng.Count -eq 0 -and ($LaunchArgs -contains "--avboit-auto-capture")) {
        $classification = "APP_EXITED_ZERO_WITHOUT_CAPTURE"
    }
    if ($classification -eq "APP_EXITED_NONZERO" -and -not $exitCodeText -and $bootstrapText.Contains("CAPTURE_WRITTEN") -and $bootstrapText.Contains("APP_EXITED")) {
        $classification = "APP_EXITED_ZERO_CAPTURED"
        $exitCodeText = "unreported"
    }

    $row = [pscustomobject]@{
        name = $Name
        classification = $classification
        processCreated = $processCreated
        pid = $pidText
        exitCode = $exitCodeText
        runtimeMs = $runtimeMs
        workingDirectory = (Split-Path -Parent $ExePath)
        command = "$ExePath $argLine"
        screenshotCount = $newPng.Count
        screenshots = ($newPng -join ';')
        bootstrapLogs = ($newBootstrapLogs -join ';')
        stdout = $stdoutPath
        stderr = $stderrPath
    }
    return $row
}

Push-Location $RepoRoot
try {
    if (-not $CommitSha) {
        $CommitSha = (git rev-parse --short HEAD).Trim()
    }
} finally {
    Pop-Location
}

if (-not $ResultRoot) {
    $timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
    $ResultRoot = Join-Path $RepoRoot "LocalVisualResults\P2_6R_DirectionClosure_$timestamp"
}
if (-not $ExePath) {
    $ExePath = Join-Path $RepoRoot "Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe"
}

New-Directory $ResultRoot
New-Directory (Join-Path $ResultRoot "bootstrap")
New-Directory (Join-Path $ResultRoot "bootstrap_logs")
New-Directory (Join-Path $ResultRoot "crash_dumps")
New-Directory (Join-Path $ResultRoot "callstacks")
New-Directory (Join-Path $ResultRoot "metadata")
New-Directory (Join-Path $ResultRoot "metrics")
New-Directory (Join-Path $ResultRoot "comparisons")

$rows = @()

if ($Phase -eq "runtime") {
    $runtimeDir = Join-Path $ResultRoot "bootstrap"
    $rows += Invoke-AvboitLaunch "01_bare_dx12" @("--d3d12") $runtimeDir
    $rows += Invoke-AvboitLaunch "02_mode0_dx12" @("--d3d12", "--transparency-mode=0") $runtimeDir
    $rows += Invoke-AvboitLaunch "03_mode5_dx12" @("--d3d12", "--transparency-mode=5") $runtimeDir
    $rows += Invoke-AvboitLaunch "04_capture_mode0_dx12" @("--d3d12", "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$runtimeDir", "--avboit-commit-sha=$CommitSha") $runtimeDir
    $rows += Invoke-AvboitLaunch "05_capture_mode5_dx12" @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$runtimeDir", "--avboit-commit-sha=$CommitSha") $runtimeDir
    $rows += Invoke-AvboitLaunch "06_capture_single_dx12" @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$runtimeDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=single_layer", "--avboit-test-case=single_a050", "--avboit-transmittance-direction=legacy") $runtimeDir
    $rows += Invoke-AvboitLaunch "07_bare_vulkan" @("--vulkan") $runtimeDir
    $rows += Invoke-AvboitLaunch "08_capture_mode0_vulkan" @("--vulkan", "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$runtimeDir", "--avboit-commit-sha=$CommitSha") $runtimeDir
    $rows += Invoke-AvboitLaunch "09_capture_mode5_vulkan" @("--vulkan", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$runtimeDir", "--avboit-commit-sha=$CommitSha") $runtimeDir
}

if ($Phase -like "analytic-*") {
    $api = if ($Phase -eq "analytic-vulkan") { "Vulkan" } else { "DX12" }
    $apiArg = Api-Arg $api
    $analyticDir = Join-Path $ResultRoot "analytic"
    New-Directory $analyticDir

    $singleCases = @("single_a025", "single_a050", "single_a075")
    foreach ($case in $singleCases) {
        foreach ($mode in @("0", "5")) {
            $dirs = if ($mode -eq "5") { @("legacy", "front") } else { @("legacy") }
            foreach ($dir in $dirs) {
                $name = "${api}_single_${case}_mode${mode}_${dir}"
                $launchArgs = @($apiArg, "--transparency-mode=$mode", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=single_layer", "--avboit-test-case=$case", "--avboit-transmittance-direction=$dir")
                $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir
            }
        }
    }

    $twoCases = @("two_a025_025", "two_a050_050", "two_a075_050", "two_a010_090")
    foreach ($case in $twoCases) {
        foreach ($order in @("normal", "reverse")) {
            foreach ($mode in @("0", "5")) {
                $dirs = if ($mode -eq "5") { @("legacy", "front") } else { @("legacy") }
                foreach ($dir in $dirs) {
                    $name = "${api}_${case}_${order}_mode${mode}_${dir}"
                    $launchArgs = @($apiArg, "--transparency-mode=$mode", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=two_layer", "--avboit-test-case=$case", "--avboit-submit-order=$order", "--avboit-transmittance-direction=$dir")
                    $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir
                }
            }
        }
        foreach ($layer in @("all", "0", "1")) {
            $name = "${api}_${case}_coverage_layer${layer}"
            $launchArgs = @($apiArg, "--transparency-mode=5", "--avboit-debug-view=2", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=two_layer", "--avboit-test-case=$case", "--avboit-analytic-layer-filter=$layer")
            $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir
        }
    }

    $threeCases = @("three_a050_050_050", "three_a020_060_080", "three_a090_020_040")
    $permutations = @("perm012", "perm021", "perm102", "perm120", "perm201", "perm210")
    foreach ($case in $threeCases) {
        $name = "${api}_${case}_mode0_reference"
        $launchArgs = @($apiArg, "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=three_layer", "--avboit-test-case=$case", "--avboit-submit-order=normal")
        $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir

        foreach ($order in $permutations) {
            foreach ($dir in @("legacy", "front")) {
                $name = "${api}_${case}_${order}_mode5_${dir}"
                $launchArgs = @($apiArg, "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=three_layer", "--avboit-test-case=$case", "--avboit-submit-order=$order", "--avboit-transmittance-direction=$dir")
                $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir
            }
        }

        foreach ($layer in @("all", "0", "1", "2")) {
            $name = "${api}_${case}_coverage_layer${layer}"
            $launchArgs = @($apiArg, "--transparency-mode=5", "--avboit-debug-view=2", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=three_layer", "--avboit-test-case=$case", "--avboit-analytic-layer-filter=$layer")
            $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir
        }
    }

    $sameSliceCases = @(
        @{ scene = "same_slice"; case = "same_a050_050"; orders = @("normal", "reverse") },
        @{ scene = "same_slice"; case = "same_three_a020_060_080"; orders = $permutations }
    )
    foreach ($entry in $sameSliceCases) {
        $case = $entry.case
        $orders = $entry.orders
        $name = "${api}_${case}_mode0_reference"
        $launchArgs = @($apiArg, "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=same_slice", "--avboit-test-case=$case", "--avboit-submit-order=normal")
        $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir
        foreach ($order in $orders) {
            foreach ($dir in @("legacy", "front")) {
                $name = "${api}_${case}_${order}_mode5_${dir}"
                $launchArgs = @($apiArg, "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$analyticDir", "--avboit-commit-sha=$CommitSha", "--avboit-test-scene=same_slice", "--avboit-test-case=$case", "--avboit-submit-order=$order", "--avboit-transmittance-direction=$dir")
                $rows += Invoke-AvboitLaunch $name $launchArgs $analyticDir
            }
        }
    }
}

if ($Phase -eq "default-smoke") {
    foreach ($api in @("DX12", "Vulkan")) {
        $apiArg = Api-Arg $api
        $dir = Join-Path $ResultRoot $api
        New-Directory $dir
        foreach ($mode in @("0", "5")) {
            $dirs = if ($mode -eq "5") { @("legacy", "front") } else { @("legacy") }
            foreach ($direction in $dirs) {
                $name = "${api}_default_mode${mode}_${direction}"
                $launchArgs = @($apiArg, "--transparency-mode=$mode", "--avboit-auto-capture", "--avboit-capture-hide-ui", "--avboit-capture-frame=240", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337", "--avboit-output-dir=$dir", "--avboit-commit-sha=$CommitSha", "--avboit-transmittance-direction=$direction")
                $rows += Invoke-AvboitLaunch $name $launchArgs $dir
            }
        }
    }
}

$matrixPath = Join-Path $ResultRoot "launch_matrix.tsv"
$allRows = @()
if (Test-Path -LiteralPath $matrixPath) {
    $allRows += Import-Csv -Path $matrixPath -Delimiter "`t"
}
$allRows += $rows
$allRows | Export-Csv -Path $matrixPath -Delimiter "`t" -NoTypeInformation -Encoding UTF8
$rows | Format-Table -AutoSize
Write-Host "Launch matrix: $matrixPath"
Write-Host "Result root: $ResultRoot"
