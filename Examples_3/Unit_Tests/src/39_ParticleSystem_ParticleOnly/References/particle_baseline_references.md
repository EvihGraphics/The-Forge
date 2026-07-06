# AVBOIT Particle System - Ground-Truth Reference Baseline

This document contains the pixel-perfect, deterministic reference renders of the particle system captured via **The Forge** in headless mode (frame 500), isolated from opaque geometry. These images serve as the exact target for the upcoming UE5 Niagara implementation.

## Particle System Views (Frame 500)

### 0. True 039 Benchmark (Preset 0 - 1 Million Particles + Lights & Smoke)
*(This is the fully saturated, authentic 039 scene reproduction, featuring 1,000,000+ active particles, including the original point-light emitting embers and shadow-casting smoke volumes. 901,935 non-black pixels.)*
![Preset 0 - Original 039 Authentic](C:\Users\l3d\.gemini\antigravity\brain\f6295296-be2b-4fff-b26a-1978c7c6769a\artifacts\ParticleOnly_Ref_Preset0.png)

### 1. Default Particle Sequence (Preset 3)
![Preset 3 - Full Scene](C:\Users\l3d\.gemini\antigravity\brain\f6295296-be2b-4fff-b26a-1978c7c6769a\artifacts\ParticleOnly_Ref_Preset3.png)

### 2. Ember Only (Preset 1)
![Preset 1 - Ember Only](C:\Users\l3d\.gemini\antigravity\brain\f6295296-be2b-4fff-b26a-1978c7c6769a\artifacts\ParticleOnly_Ref_Preset1.png)

### 3. Fog Only (Preset 2)
![Preset 2 - Fog Only](C:\Users\l3d\.gemini\antigravity\brain\f6295296-be2b-4fff-b26a-1978c7c6769a\artifacts\ParticleOnly_Ref_Preset2.png)

---

### Implementation Details
* **Renderer**: The Forge (D3D12, 1920x1080)
* **Capture Trigger**: Headless sequential execution, strict early-exit at frame 505, exact screenshot capture at frame 500 (16.666 seconds elapsed time). This ensures all 10,000 particles per emitter have spawned.
* **Geometry**: Fully decoupled (Opaque mesh draw calls disabled via `--particle-only-reference`).
* **Simulation Determinism**: The missing particle bug was resolved by normalizing the simulation variables across runs. `deltaTime` is hardcoded to `0.033333f` and `Seed` is hardcoded to ensure identical initial particle placements and progression across the high-framerate headless simulation.
* **Validation Criteria**: UE5 execution MUST match these structural formations and volumetric densities pixel-for-pixel at equivalent frame time.

> [!NOTE]
> The generated reference captures now successfully represent a fully saturated, deterministic slice of the particle simulation in isolation, completely detached from the San Miguel geometry. They are ready for Niagara validation.
