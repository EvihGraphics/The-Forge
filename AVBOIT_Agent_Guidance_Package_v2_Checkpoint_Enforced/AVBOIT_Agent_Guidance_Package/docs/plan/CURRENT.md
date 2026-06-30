# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

HEAD: `64d3e5f056c8f5971acd620158538a9ef0d1d251`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0012-20260630T043500Z-p2-7a-xy-z-resolution-attribution.md`

Status: `partial`

## State Drift Note

The previous CURRENT.md incorrectly recorded HEAD as `8d94c9caf2f4a6abb54ebbf81967f8a84e5b5b9c`. The actual remote HEAD at time of this update is `64d3e5f056c8f5971acd620158538a9ef0d1d251` (commit: "update"). This file now records the correct HEAD.

The commit `64d3e5f0` included:
- CHECKPOINT_INDEX.md with 0012 entry (reported-pass, raw evidence unavailable for smoke tests)
- Updated CURRENT.md (with stale HEAD — now corrected in this file)
- 15_Transparency.vcxproj with avboit_bootstrap_win32.cpp reference (bootstrap file was untracked)
- 15_Transparency.cpp with P2.7A CLI parsing code
- avboit.h.fsl with AVBOIT_MAX_VOLUME_DEPTH=256
- avboit_integrate.comp.fsl with [AVBOIT_MAX_VOLUME_DEPTH] arrays

Files added in this correction commit (committed alongside this CURRENT.md fix):
- `Examples_3/Unit_Tests/src/15_Transparency/avboit_bootstrap_win32.cpp` (was untracked)
- `AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced/AVBOIT_Agent_Guidance_Package/docs/plan/phase_p2_7a_xy_z_resolution_attribution.md` (was untracked)
- `AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced/AVBOIT_Agent_Guidance_Package/docs/checkpoints/archive/CHECKPOINT-0012-20260630T043500Z-p2-7a-xy-z-resolution-attribution.md` (was untracked)

## Latest State

P2.7A implemented CLI arguments `--avboit-downsample-factor=` (2/4/8, default 8) and `--avboit-depth-slices=` (32/64/128/256, default 64). The shader constant `AVBOIT_MAX_VOLUME_DEPTH` was expanded from 64 to 256 and the integrate shader's fixed-size arrays were updated accordingly. A 1536 MiB budget gate was added around AVBOIT resource creation.

Build gate passed (with /p:WholeProgramOptimization=false to work around pre-existing Renderer.lib PDB issue).

Smoke tests (reported-pass; raw logs from previous session available in working tree only):
- Default behaviour (D8 Z64): reported-pass — volume 240×135×64, 23.73 MiB, budget OK
- CLI override (D4 Z128): reported-pass — volume 480×270×128, 189.84 MiB, budget OK
- Invalid arg fallback (D3 Z99): reported-pass — WARNING printed, fallback to D8 Z64

The experiment matrix (XY axis, Z axis, combination, attribution decision) has NOT been executed yet.

## Current Plan

`docs/plan/phase_p2_7a_xy_z_resolution_attribution.md`

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Confirm HEAD = `64d3e5f056c8f5971acd620158538a9ef0d1d251`.
3. Read CHECKPOINT-0012.
4. Read `docs/plan/phase_p2_7a_xy_z_resolution_attribution.md`.
5. Build with `/p:WholeProgramOptimization=false` to ensure fresh exe.
6. Create `LocalVisualResults/TempResults/P2_7A_XYZAttribution_<UTC>/` output layout.
7. Run Group A (regression D8 Z64 DX12 + Vulkan).
8. Run Group B (XY axis: D4 Z64, D2 Z64 DX12).
9. Run Group C (Z axis: D8 Z32, D8 Z128, D8 Z256 DX12).
10. Run Vulkan key configs.
11. Compute all metrics per config.
12. Apply attribution rules (≥15% relative improvement threshold).
13. Create CHECKPOINT-0013 with attribution conclusion.
