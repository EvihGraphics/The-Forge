# P2.6S Weight Propagation Metrics

- Result root: `LocalVisualResults\P2_6S_WeightPropagation_20260628T110901Z`
- Slice gate: FAIL
- Selected-weight gate: FAIL - P2.6S simultaneous selected/legacy/front diagnostic was not proven because layer filter rebuilds the LUT and debug16/17 remain current-direction proxies.
- Raw MRT gate: PASS; first differing stage `accumulation_color_weight`; final RGB MAE `0.00350683`
- Forced-weight gate: FAIL
- Constant 0.25 vs 0.75 final RGB MAE: `0.00000000`
- Layer A/B overlap RGB MAE: `0.00000000`
- Stop decision: `STOP_BEFORE_DIRECTION_MATRIX`

## Slice Z

- same_slice layer 0: expected 32, captured 63, pixels 15007, FAIL
- same_slice layer 1: expected 32, captured 63, pixels 15007, FAIL
- three_layer layer 0: expected 48, captured 63, pixels 824338, FAIL
- three_layer layer 1: expected 32, captured 63, pixels 15007, FAIL
- three_layer layer 2: expected 16, captured 63, pixels 15007, FAIL
- two_layer layer 0: expected 48, captured 63, pixels 824338, FAIL
- two_layer layer 1: expected 16, captured 63, pixels 15007, FAIL

## Selected-Weight Diagnostic Limitation

P2.6S simultaneous selected/legacy/front diagnostic was not proven because layer filter rebuilds the LUT and debug16/17 remain current-direction proxies.

## Selected Captures

- front layer 0 debug15: observed 0.992967; Selected weight under layer-filtered LUT.
- front layer 1 debug15: observed 1.000000; Selected weight under layer-filtered LUT.
- legacy layer 0 debug15: observed 0.992996; Selected weight under layer-filtered LUT.
- legacy layer 1 debug15: observed 1.000000; Selected weight under layer-filtered LUT.
- front layer 0 debug16: observed 0.000088; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
- front layer 1 debug16: observed 0.000201; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
- legacy layer 0 debug16: observed 0.992996; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
- legacy layer 1 debug16: observed 1.000000; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
- front layer 0 debug17: observed 0.992967; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
- front layer 1 debug17: observed 1.000000; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
- legacy layer 0 debug17: observed 0.000087; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
- legacy layer 1 debug17: observed 0.000201; Layer filter affects the LUT; debug16/17 are current-direction LUT proxies, not simultaneous legacy/front truth.
