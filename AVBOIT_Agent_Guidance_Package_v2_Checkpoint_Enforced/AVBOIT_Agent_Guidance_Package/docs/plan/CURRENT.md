# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

Verified P2.6T start point: `dbeb4094409c34f2bf67721d93aa727ef4e073da`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0011-20260628T164524Z-p2-6t-reverse-z-depth.md`

Status: `passed-local`

## Latest State

P2.6T fixed the reverse-Z depth mapping used by AVBOIT, normalized low-resolution splat extinction by `downsampleFactor^2`, and closed explicit selected-weight propagation. Evidence is stored in `LocalVisualResults/P2_6T_ReverseZDepth_20260628T164524Z/`.

DX12 and Vulkan target slices now hit 48/32/16, forced layer-id A/B changes raw and final coverage color, and the analytic front direction matrix improves against Mode0 by about 97%. The validated defaults are now `reverse_correct` depth mapping and `front` transmittance direction, with legacy command-line overrides preserved.

## Current Plan

`docs/plan/phase_p2_6t_reverse_z_depth.md`

## Validation Snapshot

- Build: PASS with Release x64 MSBuild after setting `FSL_COMPILER_DXC` to Windows Kits `10.0.26100.0\x64`.
- Reverse-Z calibration: PASS, near device depth is high and far device depth is low.
- Target slices: PASS, DX12/Vulkan raw medians hit 48/32/16 within tolerance.
- Explicit layer IDs and forced weight sensitivity: PASS.
- Dual legacy/front diagnostics: PASS with simultaneous LUT channels.
- DX12 analytic direction matrix: PASS, front improves average MAE by about 97%.
- Vulkan minimal gate and cross-API front parity: PASS minimal.
- Coverage invariant: PASS.
- Performance: PASS smoke; full 300-frame benchmark not run.
- Renderer validation layer gate: NOT RUN.

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Use `LocalVisualResults/P2_6T_ReverseZDepth_20260628T164524Z/metrics/final_summary.md` as the current evidence index.
3. Treat remaining default-scene darkening as low-resolution volume/resolve approximation, not depth direction failure.
4. If continuing, start a later reconstruction/resolve phase; do not revisit Depth Warp until default-scene residuals are attributed with an XY/Z matrix.
