# CHECKPOINT-0004: Clean AVBOIT Source Checkpoint

Status: passed-local
UTC: 2026-06-21T05:50:06Z
Plan: PLAN-4-0
Branch: AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced
Base: origin/baseline/theforge-1.58-windows-vs-dx12 @ c2b643ae770aa3bc7fc8fd5e4a06d5e3fed6eafc
Selected source donor: local commit 081bf9f48030688bd37a97acf6cd5e6aced3e3d2

## Summary

Created a clean checkpoint branch from the remote The Forge 1.58 DX12 baseline and restored only the AVBOIT source, documentation, and reusable validation scripts needed to continue development. The local 081bf9f4 history was intentionally not used as branch ancestry because it contained large Art resources, screenshots, and scratch files.

## Included Scope

- AVBOIT changes under `Examples_3/Unit_Tests/src/15_Transparency`.
- `15_Transparency` FSL shader additions and shader list updates.
- `15_Transparency` script additions, with `Test_DynamicAVBOIT.lua` selecting mode 5.
- Reusable root validation scripts, with hard-coded local paths removed.
- Root docs and guidance package docs for checkpoint recovery.
- `.gitignore` rules for local resources, screenshots, visual results, and scratch patch/inject files.

## Excluded Scope

- `/Art/`
- `/Screenshots/`
- `/LocalVisualResults/`
- `/Local_Egaku/`
- `/temp.cpp`
- `/out.txt`
- `/aoit_lines.txt`
- `/Automation_Scripts/patch*.py`
- `/Automation_Scripts/inject*.py`
- MSBuild-emitted `*.metaproj` and `*.metaproj.tmp` files.

## Validation

`git check-ignore -v --no-index` verified all required local-only paths are ignored, including `Art/cameraPath.txt`, `Screenshots/foo.png`, `Local_Egaku/somefile`, `LocalVisualResults/HIVE_4090x2/...`, scratch files, patch/inject scripts, and `Unit_Tests.sln.metaproj`.

`git diff --stat` and forbidden-path checks confirmed no `Art`, screenshots, local visual results, `Local_Egaku`, or scratch files are part of the checkpoint diff.

Build command:

```powershell
msbuild 'Examples_3\Unit_Tests\PC Visual Studio 2019\Unit_Tests.sln' /m '/t:Examples\15_Transparency' /p:Configuration=Release /p:Platform=x64 /p:WindowsTargetPlatformVersion=10.0.26100.0 /p:PlatformToolset=v143 /v:m /fl /flp:"logfile=LocalVisualResults\HIVE_4090x2\Build\Unit_Tests_15_Transparency_MSBuild.log;verbosity=normal"
```

Build result: success, exit code 0. The log contains an optional copy message for `*.lua`, but MSBuild completed successfully.

Runtime capture command:

```powershell
.\Run-ForgeModeCapture.ps1 -ExePath 'Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe' -OutputDir 'LocalVisualResults\HIVE_4090x2\VisualResults\15_Transparency\Mode_5_CleanCheckpoint_4' -ScreenshotPath 'LocalVisualResults\HIVE_4090x2\VisualResults\Screenshots\UT_15_Transparency_DX12_Mode_5_AVBOIT_CleanCheckpoint.png' -ModeIndex 5 -Arguments '--d3d12 --no-auto-exit' -StartupWaitSeconds 10 -StabilizeSeconds 5 -CloseWaitSeconds 5
```

Runtime result: success. `CaptureStatus=CAPTURED_CLIENT_PRINTWINDOW`, `Status=WINDOW_READY;CLOSED`.

Screenshot validation:

- Path: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_5_AVBOIT_CleanCheckpoint.png`
- Size: 1536 x 864
- Mean RGB: `[24.74224703 24.82059884 22.64817904]`
- Max RGB: `[255 255 255]`
- Std RGB: `[61.93500185 62.03849892 58.91824627]`

Capture note: the UI confirms `(AVBOIT) Adaptive voxel-based order independent transparency` is selected, but this `PrintWindow` capture does not faithfully capture the DX12 swapchain and should not be used as visual correctness evidence.

Reference images supplied by the user:

- Current AVBOIT: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_5_AVBOIT.png`
- Baseline: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Default_01.png`

User reference comparison: the AVBOIT screenshot has the skybox, ground, and opaque objects visible, but most transparent objects are absent compared with the baseline. That missing-transparency delta is the active development issue.

## Resume

Continue development from branch `AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced`. Start by comparing the user-supplied baseline and current AVBOIT screenshots, then debug why AVBOIT mode 5 loses the transparent geometry while the skybox, ground, and opaque objects remain visible.
