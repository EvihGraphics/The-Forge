# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

HEAD: `8d94c9caf2f4a6abb54ebbf81967f8a84e5b5b9c`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0012-20260630T043500Z-p2-7a-xy-z-resolution-attribution.md`

Status: `partial`

## Latest State

P2.7A implemented CLI arguments `--avboit-downsample-factor=` (2/4/8, default 8) and `--avboit-depth-slices=` (32/64/128/256, default 64). The shader constant `AVBOIT_MAX_VOLUME_DEPTH` was expanded from 64 to 256 and the integrate shader's fixed-size arrays were updated accordingly. A 1536 MiB budget gate was added around AVBOIT resource creation. Build gate, default-behaviour gate, CLI gate, invalid-arg gate, and budget gate all passed.

The experiment matrix (XY axis, Z axis, combination, attribution decision) has not been executed yet.

## Current Plan

`docs/plan/phase_p2_7a_xy_z_resolution_attribution.md`

## Validation Snapshot

- Build: PASS (Release x64, WholeProgramOptimization=false, MSBuild v143)
- Default behaviour (D8 Z64): PASS — volume 240×135×64, 23.73 MiB, budget OK
- CLI override (D4 Z128): PASS — volume 480×270×128, 189.84 MiB, budget OK
- Invalid arg fallback (D3 Z99): PASS — WARNING printed, fallback to D8 Z64
- Experiment matrix: NOT RUN
- Attribution conclusion: PENDING

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Read CHECKPOINT-0012.
3. Read `docs/plan/phase_p2_7a_xy_z_resolution_attribution.md`.
4. Build with `/p:WholeProgramOptimization=false` to ensure fresh exe.
5. Create `LocalVisualResults/TempResults/P2_7A_XYZAttribution_<UTC>/` output layout.
6. Run experiment matrix: Group A (regression), B (XY axis DX12), C (Z axis DX12), then Vulkan for key configs.
7. Compute all required metrics per config.
8. Apply attribution rules (≥15% relative improvement threshold).
9. Create CHECKPOINT-0013 with attribution conclusion.
