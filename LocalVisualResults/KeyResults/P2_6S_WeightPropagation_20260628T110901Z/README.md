# P2.6S Weight Propagation Evidence

Status: `blocked-local`

Branch: `baseline/theforge-1.58-windows-vs-dx12`

Start HEAD: `4120b7e5b8c79f843086e7ed6b83c1e6075959e0`

End HEAD: `1022f43f`

## Summary

P2.6S added explicit analytic target-slice placement, selected-weight debug views `15..20`, forced analytic weight sources, and raw full-resolution accumulation dumps.

The phase stops before the DX12 direction matrix, Vulkan runs, default-scene parity, and front-default promotion because hard gates did not pass.

## Evidence

- `slice_validation/`: per-layer coverage and z-slice debug captures.
- `selected_weight/`: debug views `15..17` for layer-filtered two-layer analytic cases.
- `raw_mrt/`: legacy/front raw `AVBOITAccumColorWeight` and `AVBOITAccumExtinction` dumps.
- `forced_weight/`: constant and layer-id forced-weight captures plus raw dumps.
- `metrics/p2_6s_weight_propagation_metrics.json`
- `metrics/p2_6s_weight_propagation_metrics.md`
- `launch_matrix*.tsv`

## Gate Result

- Slice gate: `FAIL`. All target-slice captures report GPU zIndex `63`, including expected target slices `48`, `32`, and `16`.
- Selected-weight gate: `FAIL`. The current layer-filter capture path rebuilds the LUT with only the filtered layer, and debug `16/17` remain current-direction LUT proxies rather than simultaneous true legacy/front weights.
- Raw MRT gate: `PASS`. Legacy/front differ first at `AVBOITAccumColorWeight`; final Debug0 RGB MAE is `0.00350683`.
- Forced-weight gate: `FAIL`. Constant weights normalize away as expected, and layer-id A/B raw ColorWeight hashes differ, but final overlap RGB MAE remains `0.0`.

## Decision

Default transmittance direction remains `legacy`.

Do not enter P2.7/P3 from this evidence. The next step should fix analytic target-slice placement against the actual GPU depth path and add a diagnostic path that can observe selected, legacy, and front weights without changing the LUT contents being tested.
