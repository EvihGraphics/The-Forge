# P2.6T Final Summary

- Branch: baseline/theforge-1.58-windows-vs-dx12
- Start HEAD: dbeb4094409c34f2bf67721d93aa727ef4e073da
- Result root: LocalVisualResults/P2_6T_ReverseZDepth_20260628T164524Z
- Default after validation: depth mapping reverse_correct, transmittance direction front

## Key Numeric Results

- DX12 reverse-Z raw z slices: slice48 47.988, slice32 31.992, slice16 15.996; far_3500 approximately 1.000; legacy remains collapsed to 63 for mid/far samples.
- Slice validation reverse_correct PNG-linear medians: front 47.913, middle/same 32.060, back 16.012.
- Forced A/B final coverage RGB MAE: 0.298213; raw average-color MAE: 0.400000.
- Dual selected legacy/front average-color MAE: 0.222005; simultaneous G/B gate: True.
- DX12 analytic front average MAE: 0.006449 vs legacy 0.247543; improvement 97.39%; front better groups 26/26.
- Vulkan minimal front average MAE: 0.004592 vs legacy 0.153734; improvement 97.01%; created API all Vulkan: True.
- Cross-API front average MAE: 0.000000205.
- Default scene DX12 coverage MAE reverse+front: 0.148402; outside opacity pixels: 0.
- Default scene Vulkan coverage MAE reverse+front: 0.148402; outside opacity pixels: 0.
- Performance smoke DX12 reverse+front: 0.576665 ms; Vulkan reverse+front: 0.520906 ms.

## Gates

- Reverse-Z Device Depth Gate: PASS
- Reverse-Z Linearization Gate: PASS
- CPU/GPU Projection Gate: PASS
- Target Slice Gate: PASS
- Splat/Accumulate Slice Consistency Gate: PASS (shared helper; slice validation uses accumulate and calibration uses splat+integrate path)
- Explicit Layer ID Gate: PASS
- Forced Weight Sensitivity Gate: PASS
- Dual Direction Diagnostic Gate: PASS
- Selected Weight Gate: PASS
- Mode 0 Ground Truth Gate: PASS for analytic matrix
- Draw Order Independence Gate: PASS for tested permutations
- DX12 Direction Improvement Gate: PASS
- Vulkan Analytic Gate: PASS minimal
- Cross-API Gate: PASS minimal
- Default Scene Color Gate: PASS with residual darkening classified
- Coverage Invariant Gate: PASS
- Performance Gate: PASS smoke, full 300-frame benchmark not run
- Renderer Validation Gate: NOT RUN
- P2.6T Final Gate: PASS-local with validation-layer gap

## Remaining Error Classification

Default scene remains darker than Mode0 in transparent coverage (DX12 signed luma about -0.077). Because analytic direction, slice, coverage, and cross-API gates pass, the remaining error is classified as low-resolution volume/resolve approximation rather than depth direction or selected-weight propagation.
