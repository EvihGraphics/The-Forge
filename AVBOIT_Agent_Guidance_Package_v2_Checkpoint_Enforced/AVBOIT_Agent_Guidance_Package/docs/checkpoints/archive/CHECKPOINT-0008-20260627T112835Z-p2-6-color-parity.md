# CHECKPOINT-0008 - P2.6 Transmittance Direction and Color Parity

Timestamp: `20260627T112835Z`

Branch: `baseline/theforge-1.58-windows-vs-dx12`

Start HEAD: `83b3f8e4e47e7272441a9fb53f6cfc7fd4eda4af`

End HEAD before docs commit: `ba103708`

## Result

Status: `blocked-local`

P2.6 capture and analytic infrastructure was implemented, but the transmittance direction gate did not complete. The default AVBOIT direction remains `legacy`; no front-default fix commit was made.

## Implementation Summary

- Added deterministic auto-capture controls and JSON metadata sidecars.
- Auto-capture now honors `--transparency-mode=0/5`.
- Capture names include API, mode, resolution, debug view, direction, multiplier, frame, commit, and analytic scene/case/order suffixes where needed to prevent overwrite.
- Added `--avboit-transmittance-direction=legacy|front`.
- Added candidate exclusive front LUT integration and forward event-weight selection.
- Added analytic scenes and submit-order control.
- Added unlit material flag for analytic straight-alpha comparisons.
- Extended AVBOIT debug views to `0..14`.
- Added `tools/avboit_color_parity_metrics.py`.

## Gates

- Baseline branch/head guard: PASS.
- Worktree clean before implementation: PASS.
- Build Release x64: PASS.
- DX12 AVBOIT shader generation: PASS.
- Vulkan AVBOIT shader generation: PASS.
- Deterministic capture naming/metadata: PARTIAL PASS.
- Single-layer analytic smoke: PASS, but non-discriminating.
- Two-layer direction test: FAIL/PENDING. First data was invalid because layers did not overlap; after fixing overlap, runtime capture became unstable.
- Direction promotion to `front`: NOT RUN / BLOCKED.
- Default scene gate: NOT RUN.
- Cross-API gate: NOT RUN.
- Coverage invariant: NOT RUN in P2.6.
- Performance gate: NOT RUN.

## Local Evidence

Results directory:

`LocalVisualResults/P2_6_ColorParity_20260627T112835Z`

Build command:

```powershell
$env:FSL_COMPILER_DXC="C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64"
$env:PATH="$env:FSL_COMPILER_DXC;$env:PATH"
MSBuild.exe "Examples_3\Unit_Tests\PC Visual Studio 2019\Unit_Tests.sln" /m /t:"Examples\15_Transparency" /p:Configuration=Release /p:Platform=x64 /p:PlatformToolset=v143 /p:WindowsTargetPlatformVersion=10.0.26100.0 /v:m
```

Observed local build issue:

- `fatal error LNK1103: debugging information corrupt` appeared for Renderer link artifacts after repeated local builds.
- Clearing generated Release Renderer/15_Transparency link artifacts and rebuilding resolved it.

Runtime blocker:

- After the overlap correction, local launch attempts for auto-capture either returned exit `-1` without screenshot/log or timed out with no stable capture.
- No source reset/rebase/amend was performed.

## Next Required Work

1. Investigate the no-log/exit-`-1` local launch blocker.
2. Recapture the analytic matrix from `ba103708` or later.
3. Only commit `fix(avboit): use exclusive front transmittance event weights` if the analytic gates pass.
4. Then run default-scene, cross-API, coverage, and performance gates.
