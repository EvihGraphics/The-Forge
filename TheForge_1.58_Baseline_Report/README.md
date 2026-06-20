# The Forge 1.58 Windows/VS Unit Test Baseline

Generated: 2026-06-20T01:50:11+08:00

## Baseline
- Repository: https://github.com/EvihGraphics/The-Forge
- Upstream: https://github.com/ConfettiFX/The-Forge
- Commit: 2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d
- Release: The Forge 1.58, 2024-06-17
- Machine: Windows 11 Pro, Intel i9-14900KF, NVIDIA GeForce RTX 4060 Ti
- Visual Studio: original VS2019 path attempted; final output used VS2022 17.13/v143 with SDK 10.0.22621.0
- Build Configuration: Release|x64
- Primary Graphics API: DX12
- Vulkan Status: runtime/driver present, validation layer missing, NOT_TESTED
- Patch Applied: YES, toolchain-only Config.h compiler whitelist patch

## Report Entry Points
- Final report: Final_Baseline_Report.md
- Environment: Environment_Report.md
- Repository: Repository_Baseline.md
- Build audit: Build_Instructions_Audit.md
- Build summary: Build/Build_Summary.md
- Unit Test inventory: UnitTest_Inventory.md
- Visual result index: Visual_Result_Index.md
- Screenshot montage: VisualResults/Screenshot_Montage_All.png
- 15_Transparency report: 15_Transparency/Transparency_Baseline_Report.md

## Reproduce Build
```powershell
git clone --recursive https://github.com/EvihGraphics/The-Forge.git
cd The-Forge
git checkout 2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d
git submodule sync --recursive
git submodule update --init --recursive
.\PRE_BUILD.bat
```

On this machine the official VS2019/SDK path was blocked, so the recorded final build used:

```powershell
$env:CL='/wd4189'
& 'E:\tools\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\MSBuild.exe' 
  'D:\HTC\avboit\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\Unit_Tests.sln' 
  /m /t:Build /p:Configuration=Release /p:Platform=x64 
  /p:PlatformToolset=v143 /p:WindowsTargetPlatformVersion=10.0.22621.0 /v:minimal
```

Apply Patches/toolchain_vs2022_1938_whitelist.patch before using that adapted VS2022 command.

## Reproduce Visual Tests
Use RuntimeLogs/Run-ForgeVisualTest.ps1 for each produced executable. Example:

```powershell
powershell -ExecutionPolicy Bypass -File .\RuntimeLogs\Run-ForgeVisualTest.ps1 
  -ExePath 'D:\HTC\avboit\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe' 
  -WorkingDirectory 'D:\HTC\avboit\The-Forge\Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency' 
  -ScreenshotPath '.\VisualResults\15_Transparency\Screenshots\UT_15_Transparency_DX12_Default_01.png' 
  -LogDir '.\VisualResults\15_Transparency\Logs' 
  -Arguments '--no-auto-exit --d3d12'
```

## Final Verdict
READY_WITH_LIMITATIONS
