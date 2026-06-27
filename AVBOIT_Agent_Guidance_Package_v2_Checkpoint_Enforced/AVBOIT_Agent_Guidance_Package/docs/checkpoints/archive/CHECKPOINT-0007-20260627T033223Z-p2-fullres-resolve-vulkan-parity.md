# CHECKPOINT-0007 - P2 Full-Resolution Resolve and Vulkan Parity

Timestamp: `20260627T033223Z`

Branch: `baseline/theforge-1.58-windows-vs-dx12`

Start HEAD: `7dfd798d4d987dd7e7a980b1b595461729098c32`

## Result

Status: `passed-local`

P2 changed AVBOIT from low-resolution full-screen background modulation to full-resolution transparent accumulation plus premultiplied resolve. Vulkan runtime selection was verified in a normal Release executable.

## Implementation Summary

- Platform: normal Release builds parse `--d3d12` and `--vulkan`; requested API is compared against created API after renderer initialization.
- AVBOIT resources: added two full-resolution RGBA16F render targets for color/weight and extinction/coverage diagnostics.
- AVBOIT shaders: `avboit_forward.frag.fsl` now accumulates full-resolution transparent events; `avboit_composite.frag.fsl` now resolves premultiplied color/opacity and exposes debug views.
- AVBOIT pass order: `Clear`, `Splat`, `Integrate`, `Accumulate`, `Resolve`.
- Diagnostics: added `--avboit-debug-view=N`, `--avboit-capture-hide-ui`, and `tools/avboit_coverage_invariant.py`.
- Defaults: AVBOIT multiplier default is `1.0`; `2.5` remains a diagnostic comparison value only.

## Gates

- Baseline branch/head guard: PASS.
- Worktree clean before implementation: PASS.
- Build Release x64: PASS.
- DX12 shader generation: PASS after setting `FSL_COMPILER_DXC` to Windows Kits DXC.
- Vulkan shader generation: PASS.
- Release `--d3d12` creates D3D12: PASS.
- Release `--vulkan` creates Vulkan: PASS.
- DX12 Mode 0 startup smoke: PASS.
- Vulkan Mode 0 startup smoke: PASS.
- DX12 Mode 5 auto-capture smoke: PASS.
- Vulkan Mode 5 auto-capture smoke: PASS.
- Coverage invariant DX12: PASS, `outsideCoverageNonZeroOpacityPixelCount = 0`.
- Coverage invariant Vulkan: PASS, `outsideCoverageNonZeroOpacityPixelCount = 0`.
- Visual ROI SSIM/MAE matrix: PENDING.
- Multi-resolution screenshot matrix: PENDING.

## Local Measurements

Machine: NVIDIA GeForce RTX 4060 Ti, driver `591.86`.

1920x1080 resources:

- AVBOIT volume: `240x135x64`.
- Extinction buffer: `7.91 MiB`.
- Transmittance LUT: `15.82 MiB`.
- Full-resolution accumulation RTs: `31.64 MiB`.

Mode 5 auto-capture GPU dumps:

- DX12 final debug view 0: about `0.493 ms`.
- DX12 coverage/opacity debug views: about `0.500-0.504 ms`.
- Vulkan coverage/opacity debug views: about `0.532-0.543 ms`.

Coverage invariant output:

```json
{
  "coveragePixelCount": 404948,
  "resolveNonZeroOpacityPixelCount": 404948,
  "outsideCoverageNonZeroOpacityPixelCount": 0,
  "outsideCoverageMaxOpacity": 0.0,
  "threshold": 1.5259021896696422e-05,
  "width": 1920,
  "height": 1080,
  "status": "PASS"
}
```

## Notes

- The repo-local DXC directory contained `dxc.exe` but did not provide `dxcompiler.dll` for shader generation. The successful build used Windows Kits `10.0.26100.0\x64` via `FSL_COMPILER_DXC` and `PATH`; no DLL was copied into the repo.
- The final DX12 capture no longer shows the P1 black/dark 8x8 expansion outside transparent coverage. Some stepping remains inside transparent covered surfaces because the event weight still comes from the 1/8 XY volume; this is not the uncovered-background defect.
- `ReloadServer` port-in-use log entries appeared during local smoke tests and were not renderer validation failures.

## Next Required Work

- Capture and archive the full 1920x1080, 1600x900, and 1280x720 visual matrix for DX12 and Vulkan.
- Run global SSIM/MAE and edge ROI SSIM/MAE against the HIVE Mode 0 reference.
- Do not start Depth Warp, occupancy, sparse memory, async compute, or later-stage algorithms until edge/manual gates pass.
