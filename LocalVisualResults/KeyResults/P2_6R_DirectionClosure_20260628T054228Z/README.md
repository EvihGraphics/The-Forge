# P2.6R Direction Closure Results

Timestamp: `20260628T054228Z`

Branch: `baseline/theforge-1.58-windows-vs-dx12`

Start HEAD: `91163ff9d7956a670d8562e73376de3ad9b789db`

Capture/code HEAD: `fd47644c98ea05a31bb3cde8a0b201c80f8256fc`

## What This Directory Contains

- `launch_matrix.tsv`: runtime launcher matrix with process creation, timeout, exit, and capture classification.
- `analytic/`: DX12 frame-60 analytic captures, metadata sidecars, per-layer coverage captures, and direction debug captures.
- `metrics/overlap_validation/`: generated two-layer and three-layer combined/overlap masks.
- `metrics/direction_dx12/`: direction gate summary and debug-view hash comparison.
- `metrics/debug_view_mapping.*`: current shader/UI debug-view mapping used by this result.

Forge `.log` files and launcher stdout/stderr text logs are intentionally not part of the committed evidence. The useful runtime signal is summarized in `launch_matrix.tsv` and the JSON/MD metrics.

## Runtime Result

Runtime capture is unblocked. Auto-capture launches create the process, write screenshots and JSON metadata, and exit cleanly with `APP_EXITED_ZERO_CAPTURED`.

Bare no-auto-capture launches are classified as `APP_HUNG_OR_CAPTURE_TIMEOUT` because the app remains open without an auto-exit request. That is not a renderer crash.

## Analytic Result

Overlap validation passes:

- Two-layer overlap: `12914` pixels, threshold was `> 10000`.
- Three-way overlap: `12914` pixels, threshold was `> 5000`.

Single-layer Mode5 vs Mode0 passes the PNG max-difference gate (`<= 1/255`) but does not pass the stricter linear-RGB gate in this result summary.

Direction validation fails:

- `37 / 37` paired `Debug0` final legacy/front captures are byte-identical.
- `Debug7` and `Debug8` legacy/front captures differ, proving the direction switch reaches shader debug output.
- Because all paired final outputs are identical, front transmittance has `0%` final-output improvement over legacy.

Decision: do not promote `front` as the default direction. Vulkan/default-scene/performance closure was stopped by the DX12 direction gate.
