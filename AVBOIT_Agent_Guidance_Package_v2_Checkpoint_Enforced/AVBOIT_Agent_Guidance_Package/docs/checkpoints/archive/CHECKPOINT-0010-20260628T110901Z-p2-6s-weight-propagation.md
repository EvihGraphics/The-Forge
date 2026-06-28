# CHECKPOINT-0010: P2.6S Weight Propagation

UTC time: `2026-06-28T11:09:01Z`

Status: `blocked-local`

Branch: `baseline/theforge-1.58-windows-vs-dx12`

Start HEAD: `4120b7e5b8c79f843086e7ed6b83c1e6075959e0`

End HEAD: `1022f43f`

## Commits

- `5f194ef1` - `test(avboit): place analytic layers at explicit volume slices`
- `8482cd69` - `test(avboit): trace selected weights through raw accumulation`
- `cc625c64` - `test(avboit): keep raw accumulation dump filenames short`
- `1022f43f` - `test(avboit): normalize z slice diagnostic output`

## Evidence

`LocalVisualResults/P2_6S_WeightPropagation_20260628T110901Z/`

Primary metric files:

- `metrics/p2_6s_weight_propagation_metrics.json`
- `metrics/p2_6s_weight_propagation_metrics.md`

## Gates

| Gate | Result | Notes |
|---|---|---|
| Build | PASS | Release x64 `Examples\15_Transparency` built after normal MSBuild and shader generation. |
| Runtime capture | PASS | PNG/JSON/bin evidence written. Launcher exit code remains noisy, but bootstrap reaches capture/write/exit. |
| Slice separated placement | FAIL | GPU debug zIndex is `63` for expected target slices `48`, `32`, and `16`. |
| Selected-weight diagnostics | FAIL | Current layer filter changes the LUT; debug `16/17` are not simultaneous true legacy/front weights. |
| Raw MRT stage trace | PASS | Legacy/front first differ at `AVBOITAccumColorWeight`; `AVBOITAccumExtinction` remains hash-identical. |
| Forced constant sensitivity | PASS | Constant weights normalize away; final RGB MAE is `0.0`. |
| Forced layer-id sensitivity | FAIL | Raw ColorWeight changes, but final overlap RGB MAE is `0.0`. |
| DX12 direction matrix | NOT RUN | Blocked by prior gates. |
| Vulkan analytic parity | NOT RUN | Blocked by prior gates. |
| Front default switch | NOT COMMITTED | Default remains `legacy`. |

## Recovery Notes

Continue from `1022f43f` on `baseline/theforge-1.58-windows-vs-dx12`.

Use `LocalVisualResults/P2_6S_WeightPropagation_20260628T110901Z/metrics/p2_6s_weight_propagation_metrics.json` as the latest evidence. Do not proceed to P2.7/P3 or default-front promotion until:

- analytic target-slice placement produces distinct GPU zIndex values,
- the selected/legacy/front diagnostic can observe all three weights without altering the LUT contents under test,
- layer-id A/B forced weights alter the final resolve in the overlap ROI or the resolve math is explicitly classified as intentionally invariant.
