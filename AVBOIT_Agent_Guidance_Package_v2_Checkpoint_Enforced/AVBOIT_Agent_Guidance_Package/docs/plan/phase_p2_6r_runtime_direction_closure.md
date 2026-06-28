# P2.6R Runtime Capture Unblock and Direction Gate Closure

## Scope

P2.6R starts from `91163ff9d7956a670d8562e73376de3ad9b789db` on `baseline/theforge-1.58-windows-vs-dx12`.

The phase goal is to unblock deterministic runtime capture, validate overlapping analytic scenes, compare `legacy` and `front` transmittance directions, and promote `front` only if the direction gate passes.

## Implementation

Commits:

- `07f2357e` - `fix(test): stabilize avboit runtime capture startup`
- `fd47644c` - `test(avboit): validate overlapping analytic direction cases`
- `5bb8076a` - `test(avboit): archive p2 6r direction evidence`

No `fix(avboit): make exclusive front transmittance the default` commit was created because the direction gate failed.

## Evidence

Result directory:

`LocalVisualResults/P2_6R_DirectionClosure_20260628T054228Z/`

Key files:

- `README.md`
- `launch_matrix.tsv`
- `metrics/overlap_validation/two_a050_050_overlap.json`
- `metrics/overlap_validation/three_a050_050_050_overlap.json`
- `metrics/direction_dx12/dx12_direction_gate_summary.json`
- `metrics/direction_dx12/dx12_debug_weight_hashes.json`
- `metrics/debug_view_mapping.md`

## Runtime Result

Runtime auto-capture is unblocked.

The launcher records `APP_EXITED_ZERO_CAPTURED` for auto-capture runs. Bare no-auto-capture launches are classified as `APP_HUNG_OR_CAPTURE_TIMEOUT`, which is expected for a process left open without an auto-exit request.

Bootstrap logs were useful locally, but `.log` files remain ignored. The committed runtime evidence is the TSV classification plus screenshots and JSON metadata.

## Analytic Result

Overlap validation passes:

- Two-layer overlap: `12914` pixels.
- Three-way overlap: `12914` pixels.

The direction gate does not pass:

- `37 / 37` paired `Debug0` final legacy/front captures are byte-identical.
- `Debug7` and `Debug8` change with `--avboit-transmittance-direction`, so the direction switch reaches shader debug output.
- Since final output is identical across all paired captures, `front` has `0%` final-output improvement over `legacy`.

Single-layer Mode5 vs Mode0 passes the PNG max-difference gate, but the strict linear-RGB threshold is not satisfied in the summary metrics.

## Decision

Status: `blocked-local`.

Default transmittance direction remains `legacy`.

Vulkan analytic closure, default-scene color parity, coverage parity, and performance closure were not run after the DX12 direction gate failed. The next phase should inspect why direction-dependent weights are neutralized before the final resolve rather than moving directly to P2.7 or P3.
