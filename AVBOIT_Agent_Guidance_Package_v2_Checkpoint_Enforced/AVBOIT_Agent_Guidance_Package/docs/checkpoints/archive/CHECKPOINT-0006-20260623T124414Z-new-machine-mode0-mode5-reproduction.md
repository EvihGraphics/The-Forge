# CHECKPOINT-0006 - New Machine Mode 0/5 Reproduction

UTC: `2026-06-23T12:44:14Z`

Status: `failed`

Plan / Stage: `new-machine-mode0-mode5-reproduction`

## Scope

Fresh clone validation of `15_Transparency` on branch `baseline/theforge-1.58-windows-vs-dx12`, using the remote default AVBOIT multiplier and comparing new-machine Mode 0 and Mode 5 screenshots against the checked-in HIVE references.

Clone root:

`G:\Game\AVBOIT\The-Forge-NewMachineVerification_20260623T114619Z`

Evidence root:

`LocalVisualResults/DESKTOP-KCK6JUT/NewMachineVerification_20260623T114619Z/`

## Source And State

- Remote branch: `baseline/theforge-1.58-windows-vs-dx12`
- Required HEAD: `39046051cef37bff0e52e497ca7df07ba9aebe65`
- Verified HEAD: `39046051cef37bff0e52e497ca7df07ba9aebe65`
- Drift marker: `state-metadata-drift`
- Root `docs/plan/CURRENT.md` was stale and still pointed at Checkpoint 0004 / missing-transparent-geometry work.
- Nested guidance package `CURRENT.md` recorded Checkpoint 0005, RGB restoration, and SSIM results.
- This run used the verified remote HEAD, real source, and current reference PNGs as truth.

Source default check:

- `Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp` keeps `float gAVBOITMultiplier = 2.5f`.
- Runtime args did not pass `--avboit-multiplier`.
- Runtime logs show transparency mode command-line selection for modes 0 and 5, and no command-line multiplier override.

## Toolchain

- Machine: `DESKTOP-KCK6JUT`
- SDK selected: `10.0.26100.0`
- Visual Studio: VS 2022 Community 17.14
- PlatformToolset: `v143`
- Selected runtime GPU/API: `NVIDIA GeForce RTX 3060 Ti`, D3D12
- Runtime log detected two RTX 3060 Ti adapters and selected `GPU[0]`.
- Repository-bundled DXC failed because `dxcompiler.dll` was missing beside `dxc.exe`.
- Build was retried with `FSL_COMPILER_DXC=C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64`.

Build command:

```text
MSBuild.exe "Examples_3\Unit_Tests\PC Visual Studio 2019\Unit_Tests.sln" /m /t:"Examples\15_Transparency" /p:Configuration=Release /p:Platform=x64 /p:PlatformToolset=v143 /p:WindowsTargetPlatformVersion=10.0.26100.0 /v:m
```

## Gate Results

First recorded gate: `state-metadata-drift`

First operational failing gate: `submodule_update`

Overall result: `failed`

| Gate | Status | Evidence | Notes |
|---|---|---|---|
| Remote branch / HEAD | pass | `repository_state_initial.txt` | Remote target matched `39046051cef37bff0e52e497ca7df07ba9aebe65`. |
| State metadata drift | recorded | `repository_state_initial.txt` | Root CURRENT and nested guidance CURRENT disagreed. |
| Initial tracked worktree | pass | `repository_state_initial.txt` | Fresh clone was clean before asset restore output. |
| Post-PRE_BUILD tracked worktree | fail | `git_status_final_before_checkpoint.txt` | Art restore left tracked `Art/*` text/config files modified. |
| Git LFS | pass | `git_lfs_pull.log`, `git_lfs_fsck.log` | LFS pull and fsck completed; fsck reported OK. |
| Submodules | fail | `git_submodule_update.log`, `submodule_failure_analysis.txt` | `Local_Egaku` is a gitlink but `.gitmodules` has no URL for it. |
| PRE_BUILD exit | pass | `PRE_BUILD_exit.txt`, `PRE_BUILD_full.log` | `Art.zip` downloaded/extracted; exit code alone was not treated as sufficient. |
| Required asset layout | fail | `asset_verification.tsv`, `asset_layout_analysis.txt` | `Art/UnitTestResources` was absent; assets unpacked under top-level `Art`. |
| Toolchain detection | pass | `toolchain_detection.txt` | VS2022/v143 and SDK `10.0.26100.0` selected without editing `.vcxproj`. |
| Build | pass after override | `msbuild_retry_exit.txt`, `build_output_verification.tsv` | `15_Transparency.exe` and AVBOIT DXIL outputs exist. |
| Runtime capture | pass | `Mode_*_attempt4_client1920x1080/run_metadata.txt` | Visible desktop, client-area `CopyFromScreen`; no `PrintWindow`. |
| Runtime PNG gate | pass | `image_metrics_final.tsv` | New PNGs are nonblank, `1920x1080`, >100 KB, >1000 unique colors, non-flat luminance, and not reference-hash copies. |
| Visual comparison | pass | `image_metrics_final.tsv` | Both modes meet SSIM >= 0.95 and MAE <= 0.05. |

## Runtime Notes

Because `PRE_BUILD.bat` produced top-level `Art` folders but not `Art/UnitTestResources`, early visible runtime attempts exited with missing resource errors for meshes, fonts, skybox, and `Textures/grid.tex`. A diagnostic, non-source runtime resource layout adaptation copied the real PRE_BUILD-created top-level assets into the `15_Transparency` build output so the executable could be exercised. This adaptation is recorded in `runtime_resource_layout_adaptation.log` and does not make the official `Art/UnitTestResources` asset gate pass.

Successful final runtime args:

```text
--d3d12 --no-auto-exit --transparency-mode=0
--d3d12 --no-auto-exit --transparency-mode=5
```

Final generated PNGs:

- `LocalVisualResults/DESKTOP-KCK6JUT/NewMachineVerification_20260623T114619Z/Screenshots/UT_15_Transparency_DX12_Mode_0.png`
- `LocalVisualResults/DESKTOP-KCK6JUT/NewMachineVerification_20260623T114619Z/Screenshots/UT_15_Transparency_DX12_Mode_5.png`

References, read-only:

- `LocalVisualResults/KeyResults/HIVE_4090x2/VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_0.png`
- `LocalVisualResults/KeyResults/HIVE_4090x2/VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_5.png`

## PNG Hashes And Metrics

| Mode | Generated SHA-256 | Reference SHA-256 | Dimensions | MAE | Max Diff | SSIM | Pass |
|---:|---|---|---|---:|---:|---:|---|
| 0 | `e93f0c04008d04500b3ecab86158bf0f0904acff35fb9b065ddd7089493abe08` | `ef55bd5173ad97b6354f0426c44e304d42231d243aaa7346275a5201f831075e` | `1920x1080` | `0.009433655` | `217` | `0.957815536` | yes |
| 5 | `017e3008e06bca2c9b17eb40cec9d8453f57993eb37dc46da09da11abf8487f6` | `f2b4f7e4a85d01b73dbe3358c7f97948dc8e6fd2f81647e1ebece076aa3e897d` | `1920x1080` | `0.005494095` | `204` | `0.971785077` | yes |

## Build Outputs

Verified:

- `Examples_3/Unit_Tests/PC Visual Studio 2019/x64/Release/15_Transparency/15_Transparency.exe`
- `CompiledShaders/DIRECT3D12/avboit_forward.frag_0.dxil`
- `CompiledShaders/DIRECT3D12/avboit_integrate.comp_0.dxil`
- `CompiledShaders/DIRECT3D12/avboit_composite.frag_0.dxil`

## Forbidden Actions Not Performed

- Did not touch `MaterialShaderExample`.
- Did not modify AVBOIT shaders.
- Did not modify the AVBOIT multiplier source default.
- Did not pass `--avboit-multiplier`.
- Did not modify extinction or depth mapping.
- Did not modify scene or camera.
- Did not use `PrintWindow` black/blank capture as evidence.
- Did not copy reference PNG hashes into generated output.
- Did not overwrite historical checkpoint or reference PNGs.

## Resume Entry

1. Continue from `CHECKPOINT-0006-20260623T124414Z-new-machine-mode0-mode5-reproduction.md`.
2. Treat visual Mode 0/5 reproduction as passed for the adapted runtime output.
3. Treat the overall validation as failed until `Local_Egaku` submodule metadata and the `Art/UnitTestResources` asset-layout expectation are reconciled.
4. Re-run from a fresh clone after those repository/resource gates are fixed, using the same no-multiplier DX12 mode commands and client-area `CopyFromScreen` capture.
