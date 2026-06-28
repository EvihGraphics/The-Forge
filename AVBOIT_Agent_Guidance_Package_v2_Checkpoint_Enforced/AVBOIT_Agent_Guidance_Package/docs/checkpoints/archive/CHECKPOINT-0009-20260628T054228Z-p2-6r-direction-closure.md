# CHECKPOINT-0009: P2.6R Direction Closure

UTC time: `2026-06-28T05:42:28Z`

Status: `blocked-local`

Branch: `baseline/theforge-1.58-windows-vs-dx12`

Start HEAD: `91163ff9d7956a670d8562e73376de3ad9b789db`

Evidence commit: `5bb8076a`

## Summary

P2.6R restored stable runtime auto-capture and generated overlapping DX12 analytic evidence. It did not promote the exclusive-front transmittance direction because final resolved output remains byte-identical to legacy for the paired analytic matrix.

## Commits

- `07f2357e` - runtime bootstrap logging and launcher classification.
- `fd47644c` - analytic layer filtering, overlap metadata, and metrics tooling updates.
- `5bb8076a` - visual evidence and direction-gate metrics.

No front-default commit was created.

## Evidence

Directory:

`LocalVisualResults/P2_6R_DirectionClosure_20260628T054228Z/`

Primary evidence:

- `README.md`
- `launch_matrix.tsv`
- `metrics/overlap_validation/*.json`
- `metrics/direction_dx12/dx12_direction_gate_summary.json`
- `metrics/direction_dx12/dx12_debug_weight_hashes.json`
- `metrics/debug_view_mapping.md`

## Gates

| Gate | Result | Notes |
| --- | --- | --- |
| Preflight branch/head | PASS | Started from `91163ff9` after fetch and clean tree. |
| Release build | PASS | Built `Examples\\15_Transparency` Release x64 with Windows Kits DXC. |
| Runtime auto-capture | PASS | Auto-capture runs classify as `APP_EXITED_ZERO_CAPTURED`. |
| Two-layer overlap | PASS | `12914` overlap pixels. |
| Three-layer overlap | PASS | `12914` three-way overlap pixels. |
| Debug direction plumbing | PASS | Debug views `7` and `8` differ between legacy and front. |
| Final output direction improvement | FAIL | `37 / 37` paired Debug0 legacy/front captures are byte-identical. |
| Front default promotion | FAIL | No default switch committed. |
| Vulkan/default/perf closure | NOT RUN | Stopped after DX12 direction gate failure. |

## Decision

Remain in P2.6R blocked-local state. The next work item is to explain why direction-dependent event weights do not affect final resolved color, before running wider Vulkan/default-scene/performance gates.
