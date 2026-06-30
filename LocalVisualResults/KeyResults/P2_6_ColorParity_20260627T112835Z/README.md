# P2.6 Color Parity Local Results

Timestamp: `20260627T112835Z`

Branch: `baseline/theforge-1.58-windows-vs-dx12`

Start HEAD: `83b3f8e4e47e7272441a9fb53f6cfc7fd4eda4af`

Implementation HEAD at archive creation: `ba103708`

## Contents

- `analytic/single_layer_smoke`: DX12 single-layer alpha `0.50` Mode 0, Mode 5 legacy, and Mode 5 front captures plus metrics. This confirms deterministic capture naming/metadata and PNG-level agreement for a case that cannot distinguish transmittance direction.
- `analytic/two_layer_pre_overlap_fix_invalid`: DX12 two-layer captures taken before the analytic scene was corrected to place layers along the camera ray. These captures are intentionally archived as invalidated evidence because red and green did not overlap on screen.
- `metadata`: copied JSON metadata sidecars from the archived captures.
- `metrics`: copied stdlib PNG metric outputs for the archived captures.
- `DX12`, `Vulkan`, `comparisons`: reserved for the next completed capture pass.

## Gate Status

- Build Release x64: PASS after clearing corrupted local Renderer link debug artifacts and rebuilding.
- Deterministic capture controls: PARTIAL PASS. Auto filenames and JSON sidecars work and no longer overwrite legacy/front or analytic case variants.
- Single-layer analytic smoke: PASS within PNG quantization (`rgbMaxAbsDiff = 1/255`).
- Direction gate: FAIL/PENDING. The initial two-layer dataset was invalid because layers did not overlap. After fixing layer placement, local runtime capture became unstable (`Start-Process` exit `-1` or wait timeout without a screenshot/log), so the front direction was not promoted to default.
- Default transmittance direction: remains `legacy`.

## Notes

The images in this directory are evidence for the P2.6 capture and analytic harness, not final parity evidence. The next run must recapture the analytic matrix after `ba103708` or later so overlapping layers are verified before enabling front-exclusive transmittance by default.
