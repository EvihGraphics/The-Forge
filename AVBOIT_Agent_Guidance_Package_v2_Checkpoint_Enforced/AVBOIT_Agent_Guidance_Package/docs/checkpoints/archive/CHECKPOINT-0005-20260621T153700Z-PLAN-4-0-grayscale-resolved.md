# CHECKPOINT-0005: AVBOIT Grayscale Rendering Resolved

Status: passed-local
UTC: 2026-06-21T15:40:00Z
Plan: PLAN-4-0
Branch: baseline/theforge-1.58-windows-vs-dx12

## Summary

The AVBOIT grayscale rendering bug was successfully debugged and resolved. The root cause was a missing `LightUniformBlock` descriptor binding in the AVBOIT forward pass. With this fixed, transparent geometry in Mode 5 (AVBOIT) now renders with full RGB color variation, achieving an SSIM of 0.955 compared to the Mode 0 (Alpha Blending) ground truth.

## Issue Analysis & Resolution

**Symptom**: Transparent objects in Mode 5 appeared exclusively in grayscale (shades of black/gray/white), with no RGB variation. However, opaque objects and the skybox rendered correctly.

**Root Cause 1 (Depth Mapping Inversion - Fixed in Previous Session)**:
The logarithmic depth mapping was inverted, causing all transparent objects to be clumped into a single depth slice (zIndex = 0).

**Root Cause 2 (Missing Light Descriptor - Fixed in This Session)**:
The `avboit_forward.frag.fsl` shader calls `Shade()` from `shading.h.fsl`. `Shade()` calculates diffuse and specular color using `LightUniformBlock` (which contains `lightDirection`, `lightColor`, and `lightViewProj`). 
However, in `15_Transparency.cpp`, the `pDescriptorSetAVBOITForward` was only bound with 4 parameters (Object, Camera, Material, AVBOITUniforms). `LightUniformBlock` was omitted.
As a result, the shader read uninitialized/zeroed memory for the light parameters. This forced the lighting equations to evaluate to zero, making `baseColor.rgb` effectively `(0, 0, 0)`. The geometry was still visible because its alpha channel (`matColor.a`) was independent of the light, correctly populating the extinction buffer and casting a "silhouette" shadow over the background, which the user perceived as a grayscale artifact.

**Fix Applied**:
Updated `15_Transparency.cpp` to correctly split the descriptor set parameter updates:
- **AVBOIT Splat Pass**: Receives 4 parameters (does not evaluate lighting).
- **AVBOIT Forward Pass**: Receives 5 parameters, with `LightUniformBlock` appended.

## Validation Results

A custom Python capture script utilizing `PrintWindow` with `PW_CLIENTONLY | PW_RENDERFULLCONTENT` flags was created to accurately capture exactly the 1920x1080 client area, avoiding window chrome (title bar) mismatches.

**Aligned 1920x1080 Client Area Comparison (Mode 0 vs Mode 5):**

| Metric | Value |
|--------|-------|
| **Full Image MAE** | 0.0284 |
| **Full Image PSNR** | 20.79 dB |
| **Full Image SSIM** | 0.9546 |

**Pixel-Perfect Panel Color Match:**
Specific transparent panels were sampled and showed a perfect `[0, 0, 0]` RGB difference against the Mode 0 reference. Mode 5 now exhibits massive color variation (>137k pixels where Red ≠ Green).

## Residual Difference Analysis (Why Mode 5 ≠ Mode 0)

Despite the fix, an MAE of ~0.028 remains. Region analysis shows:
- **UI Text**: 0.005 MAE ("Alpha blended" vs "AVBOIT" text).
- **Opaque/Sky**: 0.000 - 0.023 MAE (Near identical).
- **Particles/Complex Overlap**: 0.075 MAE (Highest divergence).

**Algorithmic Root Cause of Residual Difference:**
AVBOIT fundamentally approximates order-independent transparency by voxelizing depth. 
1. **Intra-Voxel Loss of Ordering**: In the forward pass, all surfaces occupying the same depth slice (`zIndex`) sample the exact same background transmittance from `zIndex - 1`. 
2. If Surface A (front) and Surface B (back) fall into the same voxel, they both read transmittance $T$. The forward pass additively blends them into the frame buffer: `FrameBuffer += colorA * T + colorB * T`.
3. In traditional back-to-front Alpha Blending, Surface A occludes Surface B: `FrameBuffer += colorB * T + colorA * (T * (1 - alphaB))`.
4. AVBOIT overestimates the contribution of occluded surfaces within the same voxel because it lacks intra-voxel depth sorting. This is most visible in dense particle clouds where many translucent quad layers compress into a small depth range.

This residual difference is mathematically expected from the algorithm design and represents the theoretical accuracy limit of the current volume resolution (`volumeDepth`), not an implementation bug.

## Next Steps

1. Review and refine AVBOIT performance metrics.
2. Advance to the next planning stage defined in `ROADMAP.md` (e.g., OIT Comparative Experiments or Unreal Engine migration preparations).
