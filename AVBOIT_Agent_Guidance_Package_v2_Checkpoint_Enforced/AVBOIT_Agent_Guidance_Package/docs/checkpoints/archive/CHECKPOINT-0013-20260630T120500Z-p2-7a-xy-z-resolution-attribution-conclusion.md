# CHECKPOINT-0013
# Date: 2026-06-30T12:05:00Z
# Stage: passed-local
# Context: P2.7A XY/Z Attribution Conclusion

## State Description

The P2.7A Resolution Attribution Matrix has been fully executed. A suite of 11 configurations spanning D8-D2 (spatial resolution) and Z32-Z256 (depth resolution) was captured via the `--avboit-auto-capture` mechanism against a Ground Truth Mode 0 rendering.

**Key Findings:**
1. **XY Resolution Scaling**: Increasing spatial resolution from D8 to D2 resulted in a marginal *regression* in visual parity (Relative MAE change: -0.09%).
2. **Z Resolution Scaling**: Expanding the volume depth buffer from 64 to 256 slices yielded a statistically insignificant improvement in visual parity (Relative MAE change: +0.76%).
3. **Attribution Decision**: The data conclusively demonstrates that volumetric resolution (XY or Z) cannot explain the persistent default-scene darkening residual (Coverage MAE ≈ 0.023). The problem is entirely uncoupled from spatial or depth undersampling.
4. **Vulkan Deprecation Note**: The testing matrix revealed that The Forge Release 1.59 has removed Vulkan support from the Windows runtime. All Vulkan configurations safely fell back to the DX12 codepath, avoiding runtime crashes.

The next necessary phase of development is **P2.7B Accumulation / Resolve Semantics Attribution**, which will shift focus away from memory/resolution scaling and directly target the mathematical composition logic in the integration and resolve passes.

## Verified Evidence
- `LocalVisualResults/TempResults/P2_7A_XYZAttribution_20260630T113700Z/metrics/config_matrix.json` (Full metric suite for all configs)
- `LocalVisualResults/TempResults/P2_7A_XYZAttribution_20260630T113700Z/metrics/attribution_decision.json` (Formal gate evaluation)
- `LocalVisualResults/TempResults/P2_7A_XYZAttribution_20260630T113700Z/metrics/final_summary.md` (Human-readable matrix results)

## Pending Blockers
- None. The P2.7A scope is complete.

## Recovery Instructions
1. Checkout `baseline/theforge-1.58-windows-vs-dx12`.
2. Review the conclusion in `LocalVisualResults/TempResults/P2_7A_XYZAttribution_20260630T113700Z/metrics/final_summary.md`.
3. Proceed with planning P2.7B.
