param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$ResultRoot = "",
    [string]$ExePath = "",
    [ValidateSet("depth-calibration", "slice-validation", "forced-weight", "dual-direction", "direction-matrix", "vulkan-minimal", "default-scene-smoke")]
    [string]$Phase = "depth-calibration",
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

    $beforeFiles = @{}
    Get-ChildItem -LiteralPath $OutputDir -File -ErrorAction SilentlyContinue | ForEach-Object {
        $beforeFiles[$_.FullName] = $_.LastWriteTimeUtc
    }

    $fullArgs = @($LaunchArgs + @("--avboit-bootstrap-log-dir=$bootstrapDir"))
    $argLine = Join-Args $fullArgs
    $startTime = Get-Date
    $classification = "UNKNOWN"
    $pidText = ""
    $exitCodeText = ""
    $processCreated = $false

    try {
        $process = Start-Process -FilePath $ExePath -ArgumentList $argLine -WorkingDirectory (Split-Path -Parent $ExePath) `
            -PassThru -WindowStyle Hidden -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath
        $processCreated = $true
        $pidText = [string]$process.Id
        $finished = $process.WaitForExit($TimeoutSeconds * 1000)
        if (-not $finished) {
            $classification = "APP_HUNG_OR_CAPTURE_TIMEOUT"
            try { Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue } catch {}
        } else {
            $process.Refresh()
            $exitCodeText = [string]$process.ExitCode
            $classification = if ($process.ExitCode -eq 0) { "APP_EXITED_ZERO" } else { "APP_EXITED_NONZERO" }
        }
    } catch {
        $classification = "PROCESS_CREATION_FAILED"
        $exitCodeText = $_.Exception.GetType().FullName
        Set-Content -Path $stderrPath -Value $_.Exception.ToString() -Encoding UTF8
    }

    $runtimeMs = [int]((Get-Date) - $startTime).TotalMilliseconds
    $newFiles = @(Get-ChildItem -LiteralPath $OutputDir -File -ErrorAction SilentlyContinue | Where-Object {
        (-not $beforeFiles.ContainsKey($_.FullName)) -or ($_.LastWriteTimeUtc -gt $beforeFiles[$_.FullName])
    } | ForEach-Object { $_.FullName })
    $newPng = @($newFiles | Where-Object { $_.EndsWith(".png") })
    $newJson = @($newFiles | Where-Object { $_.EndsWith(".json") })
    $newBin = @($newFiles | Where-Object { $_.EndsWith(".bin") })

    if ($classification -eq "APP_HUNG_OR_CAPTURE_TIMEOUT" -and $newPng.Count -gt 0) {
        $classification = "SCRIPT_WAIT_FAILURE_OR_LATE_EXIT"
    }

    [pscustomobject]@{
        name = $Name
        phase = $Phase
        classification = $classification
        processCreated = $processCreated
        pid = $pidText
        exitCode = $exitCodeText
        runtimeMs = $runtimeMs
        command = "$ExePath $argLine"
        pngCount = $newPng.Count
        jsonCount = $newJson.Count
        binCount = $newBin.Count
        outputs = ($newFiles -join ';')
        stdout = $stdoutPath
        stderr = $stderrPath
    }
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
    $ResultRoot = Join-Path $RepoRoot "LocalVisualResults\P2_6T_ReverseZDepth_$timestamp"
}
if (-not $ExePath) {
    $ExePath = Join-Path $RepoRoot "Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe"
}

New-Directory $ResultRoot
foreach ($subdir in @("depth_calibration", "slice_validation", "explicit_layer_id", "forced_weight", "dual_direction", "direction_matrix", "default_scene", "metrics", "metadata")) {
    New-Directory (Join-Path $ResultRoot $subdir)
}

$rows = @()

if ($Phase -eq "depth-calibration") {
    $outDir = Join-Path $ResultRoot "depth_calibration\dx12"
    foreach ($case in @("near_1_1", "slice48", "slice32", "slice16", "far_3500")) {
        foreach ($debugView in @(21, 22, 23, 24, 25)) {
            $name = "dx12_depth_${case}_debug${debugView}"
            $args = @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-debug-view=$debugView", "--avboit-test-scene=depth_calibration", "--avboit-test-case=$case",
                "--avboit-depth-mapping=legacy", "--avboit-dump-raw-accum")
            $rows += Invoke-AvboitLaunch $name $args $outDir
        }
    }
}

if ($Phase -eq "slice-validation") {
    $outDir = Join-Path $ResultRoot "slice_validation\dx12"
    foreach ($mapping in @("legacy", "reverse_correct")) {
        foreach ($entry in @(
            @{ scene = "two_layer"; case = "two_a050_050"; layers = @("0", "1") },
            @{ scene = "three_layer"; case = "three_a050_050_050"; layers = @("0", "1", "2") },
            @{ scene = "same_slice"; case = "same_a050_050"; layers = @("0", "1") }
        )) {
            foreach ($layer in $entry.layers) {
                $name = "dx12_slice_$($entry.scene)_$($entry.case)_layer${layer}_${mapping}"
                $args = @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                    "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                    "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                    "--avboit-debug-view=6", "--avboit-test-scene=$($entry.scene)", "--avboit-test-case=$($entry.case)",
                    "--avboit-analytic-layer-filter=$layer", "--avboit-depth-mapping=$mapping")
                $rows += Invoke-AvboitLaunch $name $args $outDir
            }
        }
    }
}

if ($Phase -eq "forced-weight") {
    $outDir = Join-Path $ResultRoot "forced_weight\dx12"
    foreach ($pattern in @("a", "b")) {
        $name = "dx12_forced_layer_${pattern}"
        $args = @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
            "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
            "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
            "--avboit-debug-view=0", "--avboit-test-scene=two_layer", "--avboit-test-case=two_a050_050",
            "--avboit-depth-mapping=reverse_correct", "--avboit-weight-source=layer_id", "--avboit-weight-pattern=$pattern",
            "--avboit-dual-direction-diagnostic", "--avboit-dump-raw-accum")
        $rows += Invoke-AvboitLaunch $name $args $outDir
    }
}

if ($Phase -eq "dual-direction") {
    $outDir = Join-Path $ResultRoot "dual_direction\dx12"
    foreach ($direction in @("legacy", "front")) {
        foreach ($debugView in @(15, 16, 17)) {
            $name = "dx12_dual_two_a050_050_${direction}_debug${debugView}"
            $args = @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-debug-view=$debugView", "--avboit-test-scene=two_layer", "--avboit-test-case=two_a050_050",
                "--avboit-depth-mapping=reverse_correct", "--avboit-transmittance-direction=$direction",
                "--avboit-dual-direction-diagnostic", "--avboit-dump-raw-accum")
            $rows += Invoke-AvboitLaunch $name $args $outDir
        }
    }
}

if ($Phase -eq "direction-matrix") {
    $outDir = Join-Path $ResultRoot "direction_matrix\dx12"
    $twoCases = @("two_a025_025", "two_a050_050", "two_a075_050", "two_a010_090")
    $threeCases = @("three_a050_050_050", "three_a020_060_080", "three_a090_020_040")
    $twoOrders = @("normal", "reverse")
    $threeOrders = @("perm012", "perm021", "perm102", "perm120", "perm201", "perm210")

    foreach ($case in $twoCases) {
        foreach ($order in $twoOrders) {
            $mode0Name = "dx12_dir_mode0_${case}_${order}"
            $mode0Args = @("--d3d12", "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-test-scene=two_layer", "--avboit-test-case=$case", "--avboit-submit-order=$order")
            $rows += Invoke-AvboitLaunch $mode0Name $mode0Args $outDir

            foreach ($direction in @("legacy", "front")) {
                $name = "dx12_dir_two_${case}_${order}_${direction}"
                $args = @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                    "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                    "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                    "--avboit-debug-view=0", "--avboit-test-scene=two_layer", "--avboit-test-case=$case",
                    "--avboit-submit-order=$order", "--avboit-depth-mapping=reverse_correct",
                    "--avboit-transmittance-direction=$direction", "--avboit-dual-direction-diagnostic")
                $rows += Invoke-AvboitLaunch $name $args $outDir
            }
        }
    }

    foreach ($case in $threeCases) {
        foreach ($order in $threeOrders) {
            $mode0Name = "dx12_dir_mode0_${case}_${order}"
            $mode0Args = @("--d3d12", "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-test-scene=three_layer", "--avboit-test-case=$case", "--avboit-submit-order=$order")
            $rows += Invoke-AvboitLaunch $mode0Name $mode0Args $outDir

            foreach ($direction in @("legacy", "front")) {
                $name = "dx12_dir_three_${case}_${order}_${direction}"
                $args = @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                    "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                    "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                    "--avboit-debug-view=0", "--avboit-test-scene=three_layer", "--avboit-test-case=$case",
                    "--avboit-submit-order=$order", "--avboit-depth-mapping=reverse_correct",
                    "--avboit-transmittance-direction=$direction", "--avboit-dual-direction-diagnostic")
                $rows += Invoke-AvboitLaunch $name $args $outDir
            }
        }
    }

    foreach ($order in $twoOrders) {
        $mode0Name = "dx12_dir_mode0_same_a050_050_${order}"
        $mode0Args = @("--d3d12", "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui",
            "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
            "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
            "--avboit-test-scene=same_slice", "--avboit-test-case=same_a050_050", "--avboit-submit-order=$order")
        $rows += Invoke-AvboitLaunch $mode0Name $mode0Args $outDir

        foreach ($direction in @("legacy", "front")) {
            $name = "dx12_dir_same_a050_050_${order}_${direction}"
            $args = @("--d3d12", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-debug-view=0", "--avboit-test-scene=same_slice", "--avboit-test-case=same_a050_050",
                "--avboit-submit-order=$order", "--avboit-depth-mapping=reverse_correct",
                "--avboit-transmittance-direction=$direction", "--avboit-dual-direction-diagnostic")
            $rows += Invoke-AvboitLaunch $name $args $outDir
        }
    }
}

if ($Phase -eq "vulkan-minimal") {
    $depthDir = Join-Path $ResultRoot "depth_calibration\vulkan"
    foreach ($case in @("near_1_1", "slice48", "slice32", "slice16", "far_3500")) {
        foreach ($debugView in @(21, 25)) {
            $name = "vulkan_depth_${case}_debug${debugView}"
            $args = @("--vulkan", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$depthDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-debug-view=$debugView", "--avboit-test-scene=depth_calibration", "--avboit-test-case=$case",
                "--avboit-depth-mapping=legacy", "--avboit-dump-raw-accum")
            $rows += Invoke-AvboitLaunch $name $args $depthDir
        }
    }

    $matrixDir = Join-Path $ResultRoot "direction_matrix\vulkan"
    foreach ($entry in @(
        @{ scene = "two_layer"; case = "two_a050_050"; order = "normal" },
        @{ scene = "two_layer"; case = "two_a010_090"; order = "normal" },
        @{ scene = "three_layer"; case = "three_a050_050_050"; order = "perm012" },
        @{ scene = "same_slice"; case = "same_a050_050"; order = "normal" }
    )) {
        $mode0Name = "vulkan_dir_mode0_$($entry.case)_$($entry.order)"
        $mode0Args = @("--vulkan", "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui",
            "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
            "--avboit-output-dir=$matrixDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
            "--avboit-test-scene=$($entry.scene)", "--avboit-test-case=$($entry.case)", "--avboit-submit-order=$($entry.order)")
        $rows += Invoke-AvboitLaunch $mode0Name $mode0Args $matrixDir

        foreach ($direction in @("legacy", "front")) {
            $name = "vulkan_dir_$($entry.case)_$($entry.order)_${direction}"
            $args = @("--vulkan", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=$CaptureFrame", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$matrixDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-debug-view=0", "--avboit-test-scene=$($entry.scene)", "--avboit-test-case=$($entry.case)",
                "--avboit-submit-order=$($entry.order)", "--avboit-depth-mapping=reverse_correct",
                "--avboit-transmittance-direction=$direction", "--avboit-dual-direction-diagnostic")
            $rows += Invoke-AvboitLaunch $name $args $matrixDir
        }
    }
}

if ($Phase -eq "default-scene-smoke") {
    foreach ($api in @("d3d12", "vulkan")) {
        $apiName = if ($api -eq "d3d12") { "DX12" } else { "Vulkan" }
        $outDir = Join-Path $ResultRoot "default_scene\$apiName"
        $mode0Name = "${api}_default_mode0"
        $mode0Args = @("--$api", "--transparency-mode=0", "--avboit-auto-capture", "--avboit-capture-hide-ui",
            "--avboit-capture-frame=240", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
            "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0")
        $rows += Invoke-AvboitLaunch $mode0Name $mode0Args $outDir

        foreach ($entry in @(
            @{ name = "legacy_depth_legacy_dir"; depth = "legacy"; direction = "legacy"; debug = 0 },
            @{ name = "reverse_depth_legacy_dir"; depth = "reverse_correct"; direction = "legacy"; debug = 0 },
            @{ name = "reverse_depth_front_dir"; depth = "reverse_correct"; direction = "front"; debug = 0 },
            @{ name = "reverse_depth_front_coverage"; depth = "reverse_correct"; direction = "front"; debug = 2 },
            @{ name = "reverse_depth_front_opacity"; depth = "reverse_correct"; direction = "front"; debug = 5 }
        )) {
            $name = "${api}_default_$($entry.name)"
            $args = @("--$api", "--transparency-mode=5", "--avboit-auto-capture", "--avboit-capture-hide-ui",
                "--avboit-capture-frame=240", "--avboit-fixed-delta=0.0166666667", "--avboit-random-seed=1337",
                "--avboit-output-dir=$outDir", "--avboit-commit-sha=$CommitSha", "--avboit-multiplier=1.0",
                "--avboit-debug-view=$($entry.debug)", "--avboit-depth-mapping=$($entry.depth)",
                "--avboit-transmittance-direction=$($entry.direction)")
            $rows += Invoke-AvboitLaunch $name $args $outDir
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
