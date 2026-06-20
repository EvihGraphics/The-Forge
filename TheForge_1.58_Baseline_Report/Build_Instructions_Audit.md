# Build Instructions Audit

Generated: 2026-06-20T01:47:25+08:00

## Files Audited
- README.md
- PRE_BUILD.bat
- Examples_3/Unit_Tests/PC Visual Studio 2019/Unit_Tests.sln
- Unit Test .vcxproj files in Examples_3/Unit_Tests/PC Visual Studio 2019
- Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp
- Examples_3/Unit_Tests/src/15_Transparency/GPUCfg/gpu.cfg
- Examples_3/Unit_Tests/src/15_Transparency/Scripts/*.lua

## Repo Required
- Use the checked-in Visual Studio 2019 Unit Tests solution for PC: Examples_3/Unit_Tests/PC Visual Studio 2019/Unit_Tests.sln.
- Project configurations available in the solution: Debug|x64 and Release|x64.
- Project files target WindowsTargetPlatformVersion 10.0.17763.0 and the VS2019/v142 era toolchain.
- PRE_BUILD.bat downloads Art.zip and extracts it with Tools/7z.exe.
- Shader/resource copies are implemented as Visual Studio project build and post-build steps.

## Repo Recommended
- Use the repository-provided Visual Studio solution rather than inventing a CMake flow.
- Use the repository-provided tools and asset layout.
- Keep shader, renderer, and Unit Test source unchanged for the baseline.

## Agent-Selected Due Environment
- Primary build configuration: Release|x64.
- Debug|x64 was recorded as available but not used for visual baseline.
- Final build used VS2022 MSBuild/v143 with WindowsTargetPlatformVersion=10.0.22621.0 after preserving the original VS2019 and SDK-missing failures.
- A one-line toolchain adaptation allowed _MSC_VER 1938 in Config.h. No renderer, OIT, UI, shader, or test-scene logic was modified.
- CL=/wd4189 was used to suppress an unused-local warning promoted to error by the newer compiler.
- Primary graphics backend: DX12. Vulkan was environment-recorded only because validation layers were missing.
