param(
    [string]$ExePath = (Join-Path $PSScriptRoot "Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe"),
    [string]$OutputRoot = (Join-Path $PSScriptRoot "LocalVisualResults\HIVE_4090x2\VisualResults\15_Transparency"),
    [int]$FirstMode = 0,
    [int]$LastMode = 5,
    [string]$Arguments = "--d3d12 --no-auto-exit",
    [int]$StartupWaitSeconds = 10,
    [int]$StabilizeSeconds = 5,
    [int]$CloseWaitSeconds = 5
)

$ErrorActionPreference = "Stop"

for ($i = $FirstMode; $i -le $LastMode; $i++) {
    $outputDir = Join-Path $OutputRoot "Mode_$i"
    $screenshot = Join-Path $OutputRoot "Screenshots\UT_15_Transparency_DX12_Mode_$i.png"
    Write-Host "Running 15_Transparency Mode $i"
    & (Join-Path $PSScriptRoot "Run-ForgeModeCapture.ps1") -ExePath $ExePath -OutputDir $outputDir -ScreenshotPath $screenshot -ModeIndex $i -Arguments $Arguments -StartupWaitSeconds $StartupWaitSeconds -StabilizeSeconds $StabilizeSeconds -CloseWaitSeconds $CloseWaitSeconds
}
