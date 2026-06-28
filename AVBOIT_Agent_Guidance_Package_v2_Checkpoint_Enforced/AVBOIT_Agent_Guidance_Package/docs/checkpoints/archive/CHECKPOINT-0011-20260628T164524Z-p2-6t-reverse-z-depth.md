# CHECKPOINT-0011 P2.6T Reverse-Z Depth Mapping

## Status

`passed-local`

## Branch And Head

- Branch: `baseline/theforge-1.58-windows-vs-dx12`
- Start HEAD: `dbeb4094409c34f2bf67721d93aa727ef4e073da`
- Result root: `LocalVisualResults/P2_6T_ReverseZDepth_20260628T164524Z/`

## Summary

P2.6T confirmed the renderer uses reverse-Z device depth, centralized corrected depth mapping, and fixed the 1/8 XY AVBOIT volume over-extinction by normalizing splat extinction by `downsampleFactor^2`. Explicit layer IDs and simultaneous legacy/front LUT diagnostics now prove selected-weight propagation.

Validated defaults after this checkpoint:

- Depth mapping: `reverse_correct`
- Transmittance direction: `front`

Both can still be overridden by command line.

## Key Results

- DX12 reverse-Z raw target slices:
  - slice48: `47.988`
  - slice32: `31.992`
  - slice16: `15.996`
  - far_3500: `0.9998`
- DX12 analytic direction matrix:
  - Legacy average MAE: `0.247543`
  - Front average MAE: `0.006449`
  - Improvement: `97.39%`
  - Front better groups: `26/26`
- Vulkan minimal direction matrix:
  - Legacy average MAE: `0.153734`
  - Front average MAE: `0.004592`
  - Improvement: `97.01%`
  - Created API: Vulkan for all Vulkan captures.
- Forced weight A/B:
  - Final coverage RGB MAE: `0.298213`
  - Raw average-color MAE: `0.400000`
- Coverage invariant:
  - DX12 outside coverage opacity pixels: `0`
  - Vulkan outside coverage opacity pixels: `0`
- Performance smoke:
  - DX12 reverse+front Mode5: `0.576665 ms`
  - Vulkan reverse+front Mode5: `0.520906 ms`

## Gates

- Reverse-Z Device Depth Gate: PASS
- Reverse-Z Linearization Gate: PASS
- CPU/GPU Projection Gate: PASS
- Target Slice Gate: PASS
- Splat/Accumulate Slice Consistency Gate: PASS
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
- Performance Gate: PASS smoke; full 300-frame benchmark not run
- Renderer Validation Gate: NOT RUN
- P2.6T Final Gate: PASS-local with validation-layer gap

## Remaining Error Classification

Default scene remains darker than Mode0 in transparent coverage. This is no longer classified as reverse-Z direction failure or selected-weight propagation failure. The remaining error is attributed to low-resolution volume/resolve approximation and should be handled in a later reconstruction/resolve phase.
