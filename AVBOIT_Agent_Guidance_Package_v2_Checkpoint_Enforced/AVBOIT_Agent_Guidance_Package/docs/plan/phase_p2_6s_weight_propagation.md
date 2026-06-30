# P2.6S Slice-Separated Weight Propagation

## Scope

P2.6S started from `4120b7e5b8c79f843086e7ed6b83c1e6075959e0` on `baseline/theforge-1.58-windows-vs-dx12`.

The phase asks why direction-dependent LUT/debug views can differ while final Debug0 output remains effectively neutralized. It explicitly avoids Depth Warp, XY reconstruction, occupancy, sparse memory, broad Vulkan performance work, and default front promotion unless the diagnostic gates pass.

## Implementation

Commits:

- `5f194ef1` - `test(avboit): place analytic layers at explicit volume slices`
- `8482cd69` - `test(avboit): trace selected weights through raw accumulation`
- `cc625c64` - `test(avboit): keep raw accumulation dump filenames short`
- `1022f43f` - `test(avboit): normalize z slice diagnostic output`

No `fix(avboit): propagate selected transmittance weight correctly` commit was made because the evidence did not isolate a propagation bug. No `fix(avboit): make exclusive front transmittance the default` commit was made because the hard gates failed.

## Evidence

Result directory:

`LocalVisualResults/KeyResults/P2_6S_WeightPropagation_20260628T110901Z/`

Key files:

- `README.md`
- `launch_matrix.tsv`
- `launch_matrix_slice_z_rerun.tsv`
- `metrics/p2_6s_weight_propagation_metrics.json`
- `metrics/p2_6s_weight_propagation_metrics.md`
- `raw_mrt/raw_*_AVBOITAccumColorWeight.bin`
- `raw_mrt/raw_*_AVBOITAccumExtinction.bin`
- `forced_weight/raw_*_AVBOITAccumColorWeight.bin`
- `forced_weight/raw_*_AVBOITAccumExtinction.bin`

## Results

- Build: PASS, Release x64 `Examples\15_Transparency`.
- Runtime capture: PASS enough for evidence. The process still reports nonzero in the launcher, but bootstrap logs show `CAPTURE_WRITTEN` and `APP_EXITED`, and PNG/JSON/bin outputs are present.
- Slice gate: FAIL. After fixing debug6 normalization, all different-slice cases still captured GPU zIndex `63` instead of expected `48/32/16`.
- Selected-weight gate: FAIL. The layer-filter path changes the LUT under test, so it cannot prove simultaneous selected/legacy/front weights. Debug views `16/17` should be treated as current-direction proxies until a true diagnostic path is added.
- Raw MRT gate: PASS. Legacy/front first differ at `AVBOITAccumColorWeight`; final Debug0 RGB MAE is `0.00350683`.
- Forced-weight gate: FAIL. Constant `0.25/0.75` final output is identical as expected, layer-id A/B raw accumulation differs, but final overlap RGB MAE remains `0.0`.

## Decision

Status: `blocked-local`.

Default transmittance direction remains `legacy`.

The next phase should first repair analytic target-slice placement against the actual GPU depth mapping and add a diagnostic mechanism that can compare selected, legacy, and front weights without rebuilding the low-res LUT differently for each layer.
