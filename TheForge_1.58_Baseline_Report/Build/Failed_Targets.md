# Failed Targets

Generated: 2026-06-20T01:48:41+08:00

## Compile/Link Failures After Adaptation
None. All 19 counted Unit Test executables were produced in Examples_3/Unit_Tests/PC Visual Studio 2019/x64/Release.

## Preserved Original Failures
| Stage | Log | Category | Summary |
|---|---|---|---|
| VS2019 original build | Build/Full_Build_Log_Original.txt | TOOLCHAIN_ERROR | VS2019 C++ targets were incomplete; Microsoft.Cpp.Default.props under v160 was missing. |
| VS2022 original SDK build | Build/Full_Build_Log_VS2022_OriginalSDK.txt | TOOLCHAIN_ERROR | Project-requested Windows SDK 10.0.17763.0 was not installed. |
| VS2022 SDK override, unpatched | Build/Full_Build_Log_VS2022_v143_SDK22621.txt | TOOLCHAIN_ERROR | Config.h rejected _MSC_VER 1938. |
| Patched, no warning suppression | Build/Full_Build_Log_Patched_VS2022_v143_SDK22621.txt | CPP_COMPILE_ERROR | Newer compiler produced unused-local C4189 treated as error. |
| Resource post-build | Build/Full_Build_Log_ResourceAdapt_FinalPostBuild.txt | MISSING_ASSET | Remaining post-build xcopy failures for optional common scripts/cameraPath/font copies. |

## Runtime Limitations
- 36_AlgorithmsAndContainers: MANUAL_INTERACTION_REQUIRED/automation-limited; logs say Bstring tests cannot run without AUTOMATED_TESTING macro.
- 15_Transparency per-mode visual switching: mode inventory is complete, but regular-build UI automation did not reliably switch modes for accepted per-mode screenshots.
