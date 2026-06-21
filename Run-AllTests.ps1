param(
    [string]$BuildRoot = (Join-Path $PSScriptRoot "Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release"),
    [string]$OutputRoot = (Join-Path $PSScriptRoot "LocalVisualResults\HIVE_4090x2\VisualResults"),
    [string]$Arguments = "",
    [int]$StartupWaitSeconds = 12,
    [int]$MaxWaitSeconds = 30,
    [int]$CloseWaitSeconds = 5
)

$ErrorActionPreference = "Stop"

$testFiles = Get-ChildItem -Path $BuildRoot -Filter *.exe -Recurse | Where-Object { $_.Name -notmatch "AssetPipelineCmd|buny" }
foreach ($test in $testFiles) {
    $testName = $test.BaseName
    $logDir = Join-Path $OutputRoot "Logs"
    $screenshot = Join-Path $OutputRoot "Screenshots\UT_$($testName)_DX12_Default_01.png"
    Write-Host "Running test: $testName"
    & (Join-Path $PSScriptRoot "Run-ForgeVisualTest.ps1") -ExePath $test.FullName -OutputDir $logDir -ScreenshotPath $screenshot -Arguments $Arguments -StartupWaitSeconds $StartupWaitSeconds -MaxWaitSeconds $MaxWaitSeconds -CloseWaitSeconds $CloseWaitSeconds
}
