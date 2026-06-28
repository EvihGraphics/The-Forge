# P2.6T Reverse-Z Depth Mapping and Explicit Weight Closure

## Scope

P2.6T continues from the P2.6S blocked-local result. It fixes the actual reverse-Z device-depth mapping used by `15_Transparency`, validates CPU/GPU target slices, and closes selected-weight propagation with explicit analytic layer IDs and raw MRT evidence.

This phase does not start Depth Warp, sparse memory, occupancy, prefix sum, or XY reconstruction.

## Implementation

- Added `--avboit-depth-mapping=legacy|reverse_correct` and promoted the validated default to `reverse_correct`.
- Centralized AVBOIT depth helpers in `avboit.h.fsl` and shared them from splat and accumulate shaders.
- Added CPU projection metadata: world, view, clip, device depth, legacy/reverse linear depth, normalized depth, and zIndex.
- Added depth debug views 21..25 for raw device depth, legacy/reverse normalized depth, and legacy/reverse z slice.
- Added explicit analytic layer IDs in material padding, with non-analytic objects using `0xFFFFFFFF`.
- Added simultaneous legacy/front LUT channels: `R=selected`, `G=legacy`, `B=exclusive front`, `A=total transmittance`.
- Fixed low-res volume over-extinction by averaging splat extinction over `downsampleFactor^2`.
- Promoted validated default transmittance direction to `front`; `legacy` remains available by command line.

## Formula

The app uses reverse-Z projection. For `camClipInfo = (zNear * zFar, zNear - zFar, zFar, 0)`, corrected linearization is:

```text
linearDepth = clipInfo.x / (clipInfo.y * (1.0 - deviceDepth) + clipInfo.z)
```

Equivalently:

```text
linearDepth = zNear * zFar / (zNear + deviceDepth * (zFar - zNear))
```

So device depth `1` maps to `zNear`, and device depth `0` maps to `zFar`.

## Evidence

Evidence root:

```text
LocalVisualResults/P2_6T_ReverseZDepth_20260628T164524Z/
```

Key parsed metrics:

- `metrics/depth_calibration_raw_summary.json`
- `metrics/slice_validation_summary.json`
- `metrics/forced_weight_gate.json`
- `metrics/dual_direction_gate.json`
- `metrics/dx12_direction_gate.json`
- `metrics/vulkan_direction_gate.json`
- `metrics/default_scene_gate.json`
- `metrics/performance_gate.json`
- `metrics/final_summary.md`

## Gate Snapshot

- Reverse-Z device-depth gate: PASS.
- Target slice gate: PASS.
- Explicit layer ID gate: PASS.
- Forced weight sensitivity gate: PASS.
- Dual direction diagnostic gate: PASS.
- DX12 analytic direction gate: PASS.
- Vulkan minimal analytic gate: PASS.
- Cross-API front gate: PASS minimal.
- Coverage invariant gate: PASS.
- Performance gate: PASS smoke; full 300-frame benchmark not run.
- Renderer validation layer gate: NOT RUN.

## Remaining Error

Default scene still has visible darkening versus Mode0 in transparent coverage. Since analytic direction, target slices, selected weights, coverage, and cross-API checks pass, the remaining default-scene error is classified as low-resolution volume/resolve approximation rather than depth direction or selected-weight propagation.
