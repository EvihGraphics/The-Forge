# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

Verified P2.6S start point: `4120b7e5b8c79f843086e7ed6b83c1e6075959e0`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0010-20260628T110901Z-p2-6s-weight-propagation.md`

Status: `blocked-local`

## Latest State

P2.6S added explicit analytic target-slice placement, selected-weight debug views, forced analytic weights, and raw MRT dumps in `LocalVisualResults/P2_6S_WeightPropagation_20260628T110901Z/`.

Raw MRT tracing shows legacy/front first differ at `AVBOITAccumColorWeight`, with final Debug0 RGB MAE `0.00350683`. However, the hard gates failed: GPU zIndex remained `63` for expected target slices `48/32/16`, selected/legacy/front simultaneous weights were not proven, and forced layer-id A/B changed raw accumulation but not final overlap output. The default direction remains `legacy`; no front-default commit was made.

## Current Plan

`docs/plan/phase_p2_6s_weight_propagation.md`

## Validation Snapshot

- Build: PASS with Release x64 MSBuild after setting `FSL_COMPILER_DXC` to Windows Kits `10.0.26100.0\x64`.
- Runtime auto-capture/raw dump: PASS enough for evidence; launcher exit code is noisy but files are written.
- Slice target placement: FAIL, GPU zIndex is `63` for expected slices `48/32/16`.
- Selected-weight diagnostic: FAIL, current layer filter changes the LUT under test.
- Raw MRT stage trace: PASS, first differing stage is `AVBOITAccumColorWeight`.
- Forced layer-id final sensitivity: FAIL, raw differs but final overlap RGB MAE is `0.0`.
- Front-default switch: NOT COMMITTED.
- Vulkan analytic, default scene, cross-API, coverage, and performance gates: NOT RUN after P2.6S hard gates failed.

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Confirm latest local P2.6S commits with `git log -8 --oneline`.
3. Use `LocalVisualResults/P2_6S_WeightPropagation_20260628T110901Z/metrics/p2_6s_weight_propagation_metrics.json` as the current blocked evidence.
4. Fix analytic target-slice placement against the actual GPU depth path before rerunning the direction matrix.
5. Add a diagnostic that observes selected, legacy, and front weights without rebuilding the low-res LUT differently for each layer.
6. Do not switch default direction to `front` until all DX12/Vulkan/default/perf gates pass.
