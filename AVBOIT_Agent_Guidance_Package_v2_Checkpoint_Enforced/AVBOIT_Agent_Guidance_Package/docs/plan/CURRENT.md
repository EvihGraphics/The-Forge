# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

Verified P2 start point: `7dfd798d4d987dd7e7a980b1b595461729098c32`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0007-20260627T033223Z-p2-fullres-resolve-vulkan-parity.md`

Status: `passed-local`

## Latest State

P2 implemented a full-resolution AVBOIT accumulation and resolve path. The low-resolution 1/8 XY volume remains in use for extinction/transmittance weighting, but final color and opacity are resolved only from full-resolution transparent fragments. The P1 uncovered-background dark 8x8 expansion is guarded by a coverage invariant: coverage debug view 2 and resolve-opacity debug view 5 must produce `outsideCoverageNonZeroOpacityPixelCount = 0` at threshold `1/65535`.

Release command-line renderer selection now works for normal builds. `--d3d12` and `--vulkan` were both verified to create the requested API instead of falling back silently.

## Current Plan

`docs/plan/phase_p2_fullres_resolve_vulkan_parity.md`

## Validation Snapshot

- Build: PASS with Release x64 MSBuild after setting `FSL_COMPILER_DXC` to Windows Kits `10.0.26100.0\x64`.
- DX12 Mode 5 auto-capture: PASS, local GPU dump about `0.49-0.51 ms`.
- Vulkan Mode 5 auto-capture: PASS, local GPU dump about `0.53-0.56 ms`.
- DX12/Vulkan Mode 0 startup smoke: PASS.
- DX12/Vulkan coverage invariant: PASS, `outsideCoverageNonZeroOpacityPixelCount = 0`.
- Visual parity ROI/SSIM matrix: PENDING.

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Confirm latest local P2 commits with `git log -5 --oneline`.
3. Rebuild with `FSL_COMPILER_DXC` pointed at a Windows Kits DXC directory if the repo-local DXC cannot load `dxcompiler.dll`.
4. For invariant validation, capture Mode 5 debug views 2 and 5 with `--avboit-capture-hide-ui`, then run `tools/avboit_coverage_invariant.py`.
5. Complete remaining visual ROI/SSIM matrix before moving to Depth Warp or occupancy work.
