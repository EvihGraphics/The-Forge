# P2.6 - Transmittance Direction and Color Parity

## Summary

P2.6 adds deterministic capture infrastructure and analytic AVBOIT test scenes so the low-resolution LUT direction can be tested before changing the default. The implementation keeps the runtime default at `legacy` until analytic, coverage, cross-API, default-scene, and performance gates pass.

Start guard:

- Branch: `baseline/theforge-1.58-windows-vs-dx12`
- Required start HEAD: `83b3f8e4e47e7272441a9fb53f6cfc7fd4eda4af`
- Historical P2 results: `LocalVisualResults/KeyResults/P2_FullResResolve_20260627`

## Implemented

- Deterministic capture controls:
  - `--avboit-auto-capture`
  - `--avboit-capture-frame=N`
  - `--avboit-fixed-delta=SECONDS`
  - `--avboit-random-seed=N`
  - `--avboit-output-dir=PATH`
  - `--avboit-commit-sha=SHA`
  - `--avboit-capture-hide-ui`
- Auto-capture now honors `--transparency-mode=0/5` and writes unique PNG/JSON pairs with API, mode, debug view, direction, multiplier, frame, commit, analytic scene, case, and submit order.
- AVBOIT uniform remains 32 bytes and now includes `avboitTransmittanceDirection` and `avboitAnalyticFlags`.
- `--avboit-transmittance-direction=legacy|front` controls LUT integration and event-weight lookup. Default is still `legacy`.
- Candidate front LUT is exclusive front transmittance: slices are integrated from near to far and the current slice is excluded from its own event weight.
- Analytic scenes:
  - `--avboit-test-scene=default|single_layer|two_layer|three_layer|same_slice`
  - `--avboit-test-case=<id>`
  - `--avboit-submit-order=normal|reverse|perm012...`
- Analytic material path uses `MATERIAL_FLAG_UNLIT` so GPU output is linear straight-alpha material color without lighting/shadow/specular terms.
- Debug views now include `6..14` for z/weight/denominator/opacity/color diagnostic output.
- Added stdlib PNG metric tool: `tools/avboit_color_parity_metrics.py`.

## Current Gate Result

The direction gate did not pass in this run.

- Single-layer smoke matched Mode 0 within PNG quantization, but single-layer cases do not distinguish legacy and front directions.
- The first two-layer dataset was invalid because the red and green planes did not overlap on screen. The analytic scene was corrected to place layers along the camera ray.
- After that correction, local runtime capture became unstable: launch attempts either returned exit `-1` without screenshot/log or timed out under `start /wait`. The build remained valid.
- Because the analytic matrix was not recaptured after the overlap fix, `fix(avboit): use exclusive front transmittance event weights` was intentionally not committed.

## Local Results

Archived at:

`LocalVisualResults/KeyResults/P2_6_ColorParity_20260627T112835Z`

Important subdirectories:

- `analytic/single_layer_smoke`
- `analytic/two_layer_pre_overlap_fix_invalid`
- `metrics`
- `metadata`

## Resume Plan

1. Rebuild Release x64 after confirming no stale `15_Transparency` process is running.
2. Capture overlapping analytic cases from HEAD `ba103708` or later.
3. Run `tools/avboit_color_parity_metrics.py` for Mode 5 legacy/front versus Mode 0.
4. Promote default direction to `front` only if the analytic matrix passes and the default-scene/cross-API/performance gates remain acceptable.
5. If runtime capture still exits without logs, investigate Windows launch/log initialization before changing AVBOIT math.
