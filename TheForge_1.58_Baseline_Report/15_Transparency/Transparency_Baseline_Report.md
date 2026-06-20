# 15_Transparency Baseline Report

Generated: 2026-06-20T01:49:08+08:00

## Scope
- Source path: Examples_3/Unit_Tests/src/15_Transparency
- Project: Examples_3/Unit_Tests/PC Visual Studio 2019/15_Transparency.vcxproj
- Executable: Examples_3/Unit_Tests/PC Visual Studio 2019/x64/Release/15_Transparency/15_Transparency.exe
- Configuration: Release|x64
- API: DX12

## Present Transparency Modes
The fixed commit defines five transparency modes:
- Alpha blended
- Weighted blended order independent transparency
- Weighted blended order independent transparency - Volition
- Phenomenological transparency
- Adaptive order independent transparency, AOIT

Default mode in source: TRANSPARENCY_TYPE_PHENOMENOLOGICAL.

## AOIT vs AVBOIT
- AOIT means Intel Adaptive Order-Independent Transparency in this baseline.
- AVBOIT means Activision Adaptive Voxel-Based Order-Independent Transparency and is absent from this baseline.
- No AOIT name, UI, shader, or behavior was renamed to AVBOIT.
- No AVBOIT shader, render path, or UI was added.

## Runtime Result
- Default 15_Transparency launch: PASS_WITH_WARNINGS.
- Accepted screenshot: VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Default_01.png.
- Visual description: transparent colored volumes/particles over a desert scene, with the Forge UI overlay visible; no black-screen failure was observed for the default mode.
- AOIT capability: runtime log reports EnableAOIT set to 1 on the selected NVIDIA RTX 4060 Ti DX12 adapter.

## Per-Mode Limitation
The source/UI/script inventory confirms all five modes, but regular Release UI automation did not reliably change the selected mode. Attempt screenshots under 15_Transparency/Screenshots are retained as evidence, but they are not accepted as per-mode visual baselines except for the default Phenomenological screenshot.

## Suitability For AVBOIT Follow-Up
15_Transparency is suitable as the code and default-visual baseline for follow-up work, but the next AVBOIT phase should first add a reliable reproducible mode-capture mechanism or use a clean official automated-testing build to capture all pre-existing modes before comparing new AVBOIT output.
