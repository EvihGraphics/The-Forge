# P2 - Full-Resolution AVBOIT Resolve and Native Vulkan Runtime Parity

## Summary

P2 replaces the P1 low-resolution full-screen background modulation with a full-resolution transparent accumulation and resolve path. The 1/8 XY, 64-slice AVBOIT volume remains responsible for extinction prepass and transmittance integration, but its LUT is now used as an event weight for real full-resolution transparent fragments. Pixels without full-resolution transparent coverage output zero resolve opacity.

Implementation baseline:

- Branch: `baseline/theforge-1.58-windows-vs-dx12`
- Start HEAD: `7dfd798d4d987dd7e7a980b1b595461729098c32`
- P2 platform commit: `fix(platform): allow renderer api selection in release builds`
- HIVE reference image policy: read-only, not modified

## Runtime And Shader Changes

- Release builds now parse `--d3d12`, `--vulkan`, and enabled `--d3d11` outside `AUTOMATED_TESTING`; multiple API flags fail. Startup logs print requested, selected-before-init, created API, and selected GPU.
- AVBOIT uniforms remain 32 bytes and now include `avboitDebugView`; default multiplier is `1.0`. Legacy multiplier values such as `2.5` are diagnostic only.
- AVBOIT adds two full-resolution `R16G16B16A16_SFLOAT` render targets:
  - `AVBOITAccumColorWeight`: RGB stores `sum(color * alpha * eventWeight)`, A stores `sum(alpha * eventWeight)`.
  - `AVBOITAccumExtinction`: R stores `sum(-log(1-alpha))`, A stores full-resolution coverage count for diagnostics.
- Pass order is now `Clear AVBOIT`, `Splat AVBOIT`, `Integrate AVBOIT`, `Accumulate AVBOIT`, `Resolve AVBOIT`.
- Resolve outputs premultiplied color and opacity, blended as `ONE, ONE_MINUS_SRC_ALPHA`; zero coverage produces zero opacity, so low-resolution voxels no longer darken uncovered background pixels.
- Debug views are available through `--avboit-debug-view=N` and UI: `0 Final`, `1 Low-res total transmittance`, `2 Full-res coverage`, `3 Full-res extinction`, `4 Denominator`, `5 Resolve opacity`.
- `--avboit-capture-hide-ui` hides profiler/UI overlays for debug screenshot analysis.

## Validation

Build command used:

```powershell
$env:FSL_COMPILER_DXC="C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64"
$env:PATH="$env:FSL_COMPILER_DXC;$env:PATH"
MSBuild.exe "Examples_3\Unit_Tests\PC Visual Studio 2019\Unit_Tests.sln" /m /t:"Examples\15_Transparency" /p:Configuration=Release /p:Platform=x64 /p:PlatformToolset=v143 /p:WindowsTargetPlatformVersion=10.0.26100.0 /v:m
```

Gate results:

- Build: PASS. DX12 and Vulkan AVBOIT shaders generated after pointing FSL DXC at the Windows Kits DXC directory.
- Release API selection: PASS. `--d3d12` created D3D12; `--vulkan` created Vulkan; Mode 0 and Mode 5 initialized for both APIs.
- Coverage invariant: PASS. DX12 and Vulkan debug captures both reported `outsideCoverageNonZeroOpacityPixelCount = 0` at threshold `1/65535`.
- Resource size at 1920x1080: volume `240x135x64`, extinction `7.91 MiB`, LUT `15.82 MiB`, full-res accumulation RTs `31.64 MiB`.
- Local RTX 4060 Ti Mode 5 auto-capture GPU dumps: DX12 `0.49-0.51 ms`, Vulkan `0.53-0.56 ms`.
- Manual visual sanity: PASS for removal of coverage-outside black/dark 8x8 expansion in the captured final DX12 image. Remaining visible stepping is inside transparent covered geometry and is not the P1 uncovered-background defect.

## Invariant Script

Run the coverage/resolve-alpha invariant on debug captures:

```powershell
python "AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced\AVBOIT_Agent_Guidance_Package\tools\avboit_coverage_invariant.py" `
  --coverage "Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\Screenshots\AVBOIT_AutoCapture_Mode5_Debug2.png" `
  --opacity "Examples_3\Unit_Tests\PC Visual Studio 2019\x64\Release\15_Transparency\Screenshots\AVBOIT_AutoCapture_Mode5_Debug5.png" `
  --json
```

Expected hard gate: `status = PASS` and `outsideCoverageNonZeroOpacityPixelCount = 0`.

## Follow-Up

- Capture the full visual matrix at 1920x1080, 1600x900, and 1280x720 when an interactive review session is available.
- Add ROI SSIM/MAE comparison against the HIVE Mode 0 reference before treating visual parity as final.
- Do not proceed to Depth Warp, occupancy, sparse memory, or other later-stage algorithms unless edge ROI/manual gates remain acceptable.
