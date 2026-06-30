# P2.7A XY/Z Resolution Attribution Matrix

## Scope

P2.7A adds startup-time CLI configuration for `--avboit-downsample-factor=` and `--avboit-depth-slices=`, then runs a controlled single-variable experiment matrix to determine whether the default-scene darkening residual (Coverage MAE ≈ 0.148, signed luma ≈ -0.077 from P2.6T) is caused by XY undersampling, Z depth quantisation, or a mixture of both.

This phase does NOT modify colour math, transmittance direction, Resolve formulas, event-weight formulas, depth-mapping formulas, or scene content. The only free parameters are Volume XY resolution and Volume Z slice count.

## Current Evidence

From CHECKPOINT-0011 / P2.6T baseline:

| Metric | Value |
|---|---|
| Branch | baseline/theforge-1.58-windows-vs-dx12 |
| HEAD | 8d94c9caf2f4a6abb54ebbf81967f8a84e5b5b9c |
| DX12 analytic front MAE | 0.006449 |
| Vulkan analytic front MAE | 0.004592 |
| DX12/Vulkan cross-API MAE | ~0.000000205 |
| Default scene Coverage MAE | 0.148402 |
| Default scene signed luma | ≈ -0.077 |
| Outside-coverage opacity pixels | 0 |
| DX12 smoke time | 0.576665 ms |
| Vulkan smoke time | 0.520906 ms |
| Depth mapping | reverse_correct |
| Transmittance direction | front |
| Downsample factor | 8 |
| Depth slices | 64 |

## Hypotheses

1. **XY dominant**: The 1/8 downsample means a single volume voxel covers 64 screen pixels. For a large transparent panel, one voxel's extinction approximates the entire 64-pixel footprint. At D4 or D2 this is 16 or 4 pixels, which reduces aliasing at object boundaries and improves weight locality.

2. **Z dominant**: With 64 depth slices, fragments separated by less than 1/64 of the log-depth range land in the same slice and share weight. For closely stacked panels this creates quantisation error. Z=128 or Z=256 reduces this.

3. **Mixed**: Both axes contribute and improvements are partially additive.

4. **Resolution cannot explain residual**: If neither D4/D2 nor Z128/Z256 achieves ≥15% coverage MAE improvement, the residual is caused by Resolve/Accumulation semantics, not Volume resolution.

## Implementation Boundary

Allowed changes:

- `--avboit-downsample-factor=2|4|8` (runtime startup config, default 8)
- `--avboit-depth-slices=32|64|128|256` (runtime startup config, default 64)
- Budget check: refuse configs exceeding 1536 MiB AVBOIT volume
- Logging: screen/volume dims, voxel count, bytes per resource, total MiB
- 64-bit arithmetic for voxel count and byte calculations
- Shader: AVBOIT_MAX_VOLUME_DEPTH expanded to 256 to support Z=256

Forbidden changes:

- gAVBOITMultiplier
- Transmittance math
- Depth-mapping math
- Resolve formula
- Weight formula
- Scene content
- Mode 0 sort order
- Bilinear XY reconstruction
- Coverage-aware reconstruction
- Linear Z splat
- Depth warp
- UE / Niagara / Substrate

## Experiment Matrix

### A. Regression Baseline

| Config | API | Purpose |
|---|---|---|
| D8 Z64 | DX12 | Confirm no default behaviour change |
| D8 Z64 | Vulkan | API parity check |

### B. XY Resolution Axis (fixed Z=64)

| Config | API |
|---|---|
| D8 Z64 | DX12 |
| D4 Z64 | DX12 |
| D2 Z64 | DX12 |
| D8 Z64 | Vulkan (if trend clear) |
| D4 Z64 | Vulkan (if trend clear) |
| D2 Z64 | Vulkan (if trend clear) |

### C. Z Resolution Axis (fixed D=8)

| Config | API |
|---|---|
| D8 Z32 | DX12 |
| D8 Z64 | DX12 (baseline shared) |
| D8 Z128 | DX12 |
| D8 Z256 | DX12 (if budget/stability allow) |
| D8 Z32 | Vulkan (key 3) |
| D8 Z64 | Vulkan (key 3) |
| D8 Z128 | Vulkan (key 3) |

### D. Combination Gate (only if both axes show significant improvement)

| Config | API |
|---|---|
| D4 Z128 | DX12 |

## Metrics

Per configuration:

1. Full-image RGB MAE
2. Coverage-only RGB MAE
3. Coverage-only RMSE
4. Signed luminance error
5. Absolute luminance error
6. Mode 5 darker-pixel ratio
7. Mode 5 brighter-pixel ratio
8. Outside-coverage changed pixel count
9. Coverage pixel count
10. DX12/Vulkan cross-API MAE
11. GPU smoke time (ms)
12. AVBOIT memory (MiB)

ROIs:

- left_blue_plane_stack
- particle_cluster
- center_small_transparent_boxes
- front_large_transparent_panels
- opaque_control_region

## Gates

| Gate | Criterion |
|---|---|
| Default Behaviour | No new args → D8 Z64 created; metrics within P2.6T tolerance |
| Build | Release x64 MSBuild succeeds |
| DX12 Runtime | All mandatory configs run without crash |
| Vulkan Runtime | Baseline and key candidates run; API confirmed as Vulkan |
| Analytic | front analytic MAE not meaningfully worse; analytic scene gates hold |
| Coverage | Outside-coverage changed pixels = 0 for all configs |
| Determinism | Two captures of same config produce coverage-identical frames |
| Attribution | Exactly one conclusion among XY-dominant, Z-dominant, mixed, or resolution-cannot-explain |
| Performance Scope | Smoke test only; no 300-frame benchmark |

## Attribution Rules

Relative improvement = (baseline_mae - candidate_mae) / baseline_mae.

Significant = relative_improvement ≥ 0.15 AND |signed_luma| improvement ≥ 0.15 AND both repeat captures agree AND outside-coverage unchanged.

- **XY dominant**: D4/D2 significant AND best-XY improvement ≥ 1.5 × best-Z improvement
- **Z dominant**: Z128/Z256 significant AND best-Z improvement ≥ 1.5 × best-XY improvement
- **Mixed**: Both significant AND |best-XY - best-Z| < 50% of best-Z AND D4 Z128 further improves
- **Resolution cannot explain**: Neither best-XY nor best-Z achieves 15% relative improvement

## Evidence Layout

```
LocalVisualResults/TempResults/P2_7A_XYZAttribution_<UTC>/
    captures/
    logs/
    metrics/
        config_matrix.csv
        config_matrix.json
        roi_matrix.csv
        determinism_gate.json
        regression_gate.json
        attribution_decision.json
        final_summary.md
    metadata/
    README.md
```

Promote to KeyResults after all gates pass.

## Explicit Non-Goals

- No Bilinear XY reconstruction
- No Coverage-aware XY reconstruction
- No Linear Z splat
- No Depth warp
- No Resolve formula change
- No weight formula change
- No 300-frame full benchmark
- No cross-card or sandstorm sequence frames
- No UE / Niagara / Substrate

## Next-Phase Decision Rules

| Attribution Conclusion | Next Phase |
|---|---|
| XY dominant | P2.7B Coverage-Aware XY Reconstruction |
| Z dominant | P2.7B Linear Z Splat / Depth Resolution |
| Mixed | P2.7B — choose smallest-change axis first |
| Resolution cannot explain | P2.7B Accumulation / Resolve Semantics Attribution |
