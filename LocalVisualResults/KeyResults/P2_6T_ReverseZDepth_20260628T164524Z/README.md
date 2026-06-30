# P2.6T Reverse-Z Depth Results

Result root for P2.6T reverse-Z depth mapping and explicit weight closure.

## Contents

- `depth_calibration/`: DX12 and Vulkan raw device-depth and z-slice calibration captures.
- `slice_validation/`: DX12 per-layer target-slice debug captures.
- `forced_weight/`: explicit analytic layer-id A/B sensitivity captures and raw MRT dumps.
- `dual_direction/`: simultaneous legacy/front selected-weight raw diagnostics.
- `direction_matrix/`: DX12 analytic Mode0/legacy/front matrix plus Vulkan minimal matrix.
- `default_scene/`: DX12/Vulkan default-scene smoke captures, coverage, opacity, and default runtime smoke.
- `metrics/`: parsed JSON/CSV/MD gate results.

## Headline Results

- Reverse-Z mapping is confirmed: near device depth is high, far device depth is low.
- Corrected z slices hit target slices 48/32/16 on DX12 and Vulkan.
- Low-res extinction splat is normalized by `downsampleFactor^2`, fixing over-extinction in the 1/8 XY event-weight volume.
- DX12 analytic front direction improves average object-mask MAE by about 97.4% versus legacy.
- Vulkan minimal direction gate improves average object-mask MAE by about 97.0% versus legacy.
- Coverage outside opacity is zero in default-scene smoke captures.
- Defaults after validation: `reverse_correct` depth mapping and `front` transmittance direction.

See `metrics/final_summary.md` for the gate table and remaining error classification.
