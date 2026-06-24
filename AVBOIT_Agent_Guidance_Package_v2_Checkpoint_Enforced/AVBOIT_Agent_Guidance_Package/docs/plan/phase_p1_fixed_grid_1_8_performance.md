# AVBOIT P1 Fixed Grid 1/8 Performance

## Scope

Baseline branch: `baseline/theforge-1.58-windows-vs-dx12`

Implementation base: `6c06d6c1`

Expected baseline attachment: `39046051` was an ancestor of the implementation base.

This phase only changes the AVBOIT fixed-grid implementation. It does not change the scene, transparent object count, particle count, material alpha, depth slice count, log-depth mapping, packing scale, LUT format, color integration model, Alpha Blend, WBOIT, PT, or AOIT algorithms.

## Before Profile

Profile source: `Examples_3/Unit_Tests/PC Visual Studio 2019/x64/Release/15_Transparency/profile`

At 1600x900, VSync off:

| API | Mode | Graphics Avg | Clear Avg | Integrate Avg |
| --- | --- | ---: | ---: | ---: |
| DX12 | Alpha Blend | ~0.226 ms | n/a | n/a |
| Vulkan | Alpha Blend | ~0.224 ms | n/a | n/a |
| DX12 | AVBOIT | ~49.99 ms | ~23.59 ms | ~25.77 ms |
| Vulkan | AVBOIT | ~4.33 ms | ~1.85 ms | ~2.14 ms |

## Fixed Grid Formula

AVBOIT now uses one shared size source:

```text
volumeWidth  = ceil(screenWidth / 8)
volumeHeight = ceil(screenHeight / 8)
volumeDepth  = 64
voxelCount   = volumeWidth * volumeHeight * volumeDepth
```

Uniform ABI:

```text
uint  volumeWidth
uint  volumeHeight
uint  volumeDepth
uint  downsampleFactor
float avboitMultiplier
float padding[3]
```

## Resource Budget

| Resolution | Volume | Extinction R32_UINT | LUT RGBA16F | Total |
| --- | --- | ---: | ---: | ---: |
| 1280x720 | 160x90x64 | 3.52 MiB | 7.03 MiB | 10.55 MiB |
| 1600x900 | 200x113x64 | 5.52 MiB | 11.04 MiB | 16.55 MiB |
| 1920x1080 | 240x135x64 | 7.91 MiB | 15.82 MiB | 23.73 MiB |

## Implemented Changes

- Centralized AVBOIT dimensions and uniform upload in `15_Transparency.cpp`.
- Replaced screen-sized AVBOIT resources with the 1/8 XY fixed grid.
- Mapped full-resolution fragment pixels to low-resolution volume coordinates in splat, forward, and composite shaders.
- Decoupled AVBOIT shader, root signature, descriptor set, resource, and pipeline lifetime from `gGpuSettings.mEnableAOIT`.
- Kept AVBOIT visible in the UI even when AOIT is unsupported.
- Removed the unused duplicate `AdaptiveVoxelBasedOITPass`.
- Changed AVBOIT clear to a one-dimensional 256-thread buffer clear of only `VolumeExtinctionBufferUAV`.
- Removed the redundant clear-time `VolumeTransmittanceLutUAV` binding; integrate remains responsible for writing the complete LUT.

## Verification Plan

Build:

```powershell
MSBuild.exe "Examples_3\Unit_Tests\PC Visual Studio 2019\Unit_Tests.sln" /m /t:"Examples\15_Transparency" /p:Configuration=Release /p:Platform=x64 /p:PlatformToolset=v143 /p:WindowsTargetPlatformVersion=10.0.26100.0 /v:m
```

Smoke targets:

```powershell
Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe --d3d12 --no-auto-exit --transparency-mode=0
Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe --d3d12 --no-auto-exit --transparency-mode=5
Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe --vulkan --no-auto-exit --transparency-mode=0
Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\15_Transparency.exe --vulkan --no-auto-exit --transparency-mode=5
```

Visual captures requested:

| API | Mode | Multiplier | Resolution |
| --- | --- | ---: | --- |
| DX12 | Alpha Blend sorted | n/a | 1600x900 |
| DX12 | AVBOIT | 1.0 | 1600x900 |
| DX12 | AVBOIT | 2.5 | 1600x900 |
| Vulkan | Alpha Blend sorted | n/a | 1600x900 |
| Vulkan | AVBOIT | 1.0 | 1600x900 |
| Vulkan | AVBOIT | 2.5 | 1600x900 |

Additional smoke resolutions: 1280x720 and 1920x1080.

## After Profile

Local verification on 2026-06-24:

- Release build passed with amd64 MSBuild after a clean single-process rebuild. The first PATH MSBuild lookup failed, and the first non-clean build hit stale/corrupt PDB state (`LNK1103`), then rebuilt cleanly.
- DX12 and Vulkan AVBOIT shader outputs were generated (`AVBOIT`, `avboit_clear`, `avboit_integrate`, `avboit_composite`, `avboit_forward`).
- DX12 AVBOIT auto-capture smoke passed at 1920x1080 with volume `240x135x64`, resource total `23.73 MiB`, and `OIT Performance Dump [Mode 5]: 0.503005 ms`.
- Vulkan runtime auto-smoke is pending in this checkout because `--vulkan` is parsed only under `AUTOMATED_TESTING` in `WindowsBase.cpp`; the normal Release executable fell back to D3D12 even when launched with `--vulkan`. Vulkan shader generation was still verified.

Pending full benchmark capture. Required counters:

| API | Graphics Avg | Graphics P95 | Graphics Max | Clear Avg | Splat Avg | Integrate Avg | Composite Avg | Forward Avg |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DX12 | pending | pending | pending | pending | pending | pending | pending | pending |
| Vulkan | pending | pending | pending | pending | pending | pending | pending | pending |

Stop condition: if DX12 `Clear + Integrate > 20 ms` after this 1/8 fixed-grid change, do not proceed to depth warp, occupancy, async compute, or other approximations. Record the actual volume, byte counts, dispatch groups, barrier order, call chain, and DX12/Vulkan difference before continuing.

## Risks

- Coarser XY voxels can increase local over-occlusion in dense particle regions; visual comparison must focus on particles, transparent planes, right/bottom edges, and cross-API structure.
- `ceil(width / 8)` dimensions require the shader-side `min(fullResPixel / downsampleFactor, volumeDims - 1)` clamp to avoid right and bottom edge out-of-bounds access.
- Clear no longer writes identity transmittance to the LUT; integrate must write every LUT voxel each frame before composite and forward passes sample it.
