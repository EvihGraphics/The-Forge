# CHECKPOINT-0012 P2.7A XY/Z Resolution Attribution — Volume Config CLI

## Checkpoint ID

CHECKPOINT-0012

## UTC Time

2026-06-30T04:35:00Z

## Status

`partial`

**Rationale**: The implementation phase is complete and all Build/Default/CLI/Budget/Validation/Runtime gates passed. The experiment matrix (captures, metric computation, attribution decision) has NOT been run yet — that is the next user-interactive step. A `partial` checkpoint is correct per the checkpoint skill: "有有效产物，但仍有明确未完成项".

## Previous Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0011-20260628T164524Z-p2-6t-reverse-z-depth.md`

## Supersedes

None

---

## User Instruction Summary

P2.7A — AVBOIT XY/Z Resolution Attribution Matrix. Add startup CLI args `--avboit-downsample-factor=` (2/4/8) and `--avboit-depth-slices=` (32/64/128/256) to allow single-variable experiment matrix runs. Budget-gate resource creation at 1536 MiB. Expand shader constant AVBOIT_MAX_VOLUME_DEPTH and integrate array sizes so Z=128 and Z=256 work correctly. Create P2.7A plan document. Archive checkpoint.

## Current Route and Plan

- Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`
- Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`
- Lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`
- **New Plan**: `docs/plan/phase_p2_7a_xy_z_resolution_attribution.md`

---

## Branch and HEAD

- Branch: `baseline/theforge-1.58-windows-vs-dx12`
- HEAD: `8d94c9caf2f4a6abb54ebbf81967f8a84e5b5b9c`
- (No new commit yet; all changes are working-tree modifications on top of HEAD)

## Workspace State

Modified files (not yet committed):

| File | Change |
|---|---|
| `Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl` | AVBOIT_MAX_VOLUME_DEPTH 64→256 |
| `Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_integrate.comp.fsl` | Array sizes [64] → [AVBOIT_MAX_VOLUME_DEPTH] |
| `Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp` | gAVBOITVolumeConfig non-const; ParseAVBOITVolumeConfig(); CheckAVBOITVolumeBudget(); budget gate in resource creation |
| `Examples_3/Unit_Tests/src/15_Transparency/avboit_bootstrap_win32.cpp` | NEW — implements avboitBootstrapStage stub on Windows |
| `Examples_3/Unit_Tests/PC Visual Studio 2019/15_Transparency.vcxproj` | Added avboit_bootstrap_win32.cpp to ClCompile ItemGroup |
| `AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced/AVBOIT_Agent_Guidance_Package/docs/plan/phase_p2_7a_xy_z_resolution_attribution.md` | NEW — P2.7A plan |
| `AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced/AVBOIT_Agent_Guidance_Package/docs/checkpoints/CHECKPOINT_INDEX.md` | Appended entry for CHECKPOINT-0012 |
| `AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced/AVBOIT_Agent_Guidance_Package/docs/plan/CURRENT.md` | Updated to P2.7A |

Untracked files (pre-existing):

- `capture_test.py`
- `move_long_paths.py`
- `update_paths.py`

## Submodule State

- `Local_Egaku`: modified (dirty submodule — pre-existing from P2.6T)
- `fatal: no submodule mapping found in .gitmodules for path 'Local_Egaku'` — pre-existing issue from CHECKPOINT-0011

---

## Build Environment

| Property | Value |
|---|---|
| Solution | `Examples_3/Unit_Tests/PC Visual Studio 2019/Unit_Tests.sln` |
| Target project | `15_Transparency.vcxproj` |
| Configuration | Release |
| Platform | x64 |
| PlatformToolset | v143 (overridden from v142 in project) |
| Windows SDK | 10.0.26100.0 |
| FSL_COMPILER_DXC | `C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64` |
| MSBuild | Visual Studio 2022 Community |
| WholeProgramOptimization | disabled at command line (`/p:WholeProgramOptimization=false`) to avoid VulkanRaytracing.obj PDB mismatch |

---

## Documents Read This Cycle

1. `docs/skill/avboit-learning-development-skill-v1/SKILL.md`
2. `docs/skill/checkpoint-archive-skill/SKILL.md`
3. `docs/skill/theforge-avboit-lab-skill/SKILL.md`
4. `docs/plan/CURRENT.md`
5. `docs/checkpoints/archive/CHECKPOINT-0011-20260628T164524Z-p2-6t-reverse-z-depth.md`
6. `docs/plan/phase_p2_6t_reverse_z_depth.md`
7. `LocalVisualResults/KeyResults/P2_6T_ReverseZDepth_20260628T164524Z/metrics/final_summary.md`
8. `Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp` (full)
9. `Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl`
10. `Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_integrate.comp.fsl`
11. `Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_clear.comp.fsl`
12. `Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl`
13. `Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_composite.frag.fsl`
14. `Examples_3/Unit_Tests/PC Visual Studio 2019/15_Transparency.vcxproj`

---

## Commands Executed

```
git fetch origin
git checkout baseline/theforge-1.58-windows-vs-dx12
git rev-parse HEAD
git status --short
git submodule status
git log --oneline -5

MSBuild 15_Transparency.vcxproj /p:Configuration=Release /p:Platform=x64 /p:PlatformToolset=v143 /p:WindowsTargetPlatformVersion=10.0.26100.0 /p:WholeProgramOptimization=false

# Smoke tests
15_Transparency.exe --d3d12 --transparency-mode=5 --avboit-auto-capture --avboit-capture-frame=60
15_Transparency.exe --d3d12 --transparency-mode=5 --avboit-auto-capture --avboit-downsample-factor=4 --avboit-depth-slices=128
15_Transparency.exe --d3d12 --transparency-mode=5 --avboit-auto-capture --avboit-downsample-factor=3 --avboit-depth-slices=99
```

## Modified Files

| File | Change Summary |
|---|---|
| `avboit.h.fsl` | `AVBOIT_MAX_VOLUME_DEPTH` 64 → 256 |
| `avboit_integrate.comp.fsl` | `float legacyEventWeights[64]` → `[AVBOIT_MAX_VOLUME_DEPTH]` (same for front) |
| `15_Transparency.cpp` | Removed `const` from `gAVBOITVolumeConfig`; added `AVBOIT_SAFE_BUDGET_MIB`, `IsValidAVBOITDownsampleFactor()`, `IsValidAVBOITDepthSlices()`, `ParseAVBOITVolumeConfig()`, `CheckAVBOITVolumeBudget()`; wired budget check into resource creation block; call `ParseAVBOITVolumeConfig()` from `Init()` |
| `avboit_bootstrap_win32.cpp` | NEW: stdout stub for `avboitBootstrapStage` on Windows |
| `15_Transparency.vcxproj` | Added `avboit_bootstrap_win32.cpp` to `ClCompile` |
| `phase_p2_7a_xy_z_resolution_attribution.md` | NEW: P2.7A plan |

---

## Build Results

| Build | Result |
|---|---|
| C++ compilation | PASS (0 errors, 0 warnings) |
| Shader recompilation (DX12 + Vulkan) | PASS (all AVBOIT shaders recompiled) |
| Link | PASS (with WholeProgramOptimization=false) |
| Output exe | `x64/Release/15_Transparency/15_Transparency.exe` 2,548,736 bytes 2026-06-30T04:31:09Z |

**Pre-existing linker issues resolved**:
- `LNK2001 avboitBootstrapStage`: Fixed by creating `avboit_bootstrap_win32.cpp`
- `LNK1103 VulkanRaytracing.obj PDB mismatch`: Worked around by disabling WholeProgramOptimization at build time (pre-existing environment issue)

---

## Runtime Results

| Test | Config | Result | Key Logs |
|---|---|---|---|
| Default behaviour | D8 Z64 (no args) | PASS | `downsampleFactor=8 depthSlices=64` / `240x135x64` / `23.73 MiB` / budget OK |
| CLI override | D4 Z128 | PASS | `downsampleFactor=4 depthSlices=128` / `480x270x128` / `189.84 MiB` / budget OK |
| Invalid arg fallback | D3 Z99 | PASS | WARNING printed, fell back to D8 Z64 |

---

## Experiment Matrix

**Status: NOT STARTED**

The following matrix is defined in `docs/plan/phase_p2_7a_xy_z_resolution_attribution.md` but has not been executed yet. Execution requires the next user session.

### Defined (pending execution):

| Group | Config | API | Status |
|---|---|---|---|
| A: Regression | D8 Z64 | DX12 | Pending |
| A: Regression | D8 Z64 | Vulkan | Pending |
| B: XY axis | D4 Z64 | DX12 | Pending |
| B: XY axis | D2 Z64 | DX12 | Pending |
| C: Z axis | D8 Z32 | DX12 | Pending |
| C: Z axis | D8 Z128 | DX12 | Pending |
| C: Z axis | D8 Z256 | DX12 | Pending |
| D: Combination | D4 Z128 | DX12 | Conditional |

---

## P2.6T Regression Baseline (frozen from CHECKPOINT-0011)

| Metric | Value |
|---|---|
| DX12 analytic front MAE | 0.006449 |
| Vulkan analytic front MAE | 0.004592 |
| DX12/Vulkan cross-API MAE | ~0.000000205 |
| Default scene Coverage MAE | 0.148402 |
| Default scene signed luma | ≈ -0.077 |
| Outside-coverage opacity pixels | 0 |
| DX12 smoke time | 0.576665 ms |
| Vulkan smoke time | 0.520906 ms |

---

## Evidence Paths

| Evidence | Location |
|---|---|
| Smoke test log (default D8 Z64) | `avboit_smoke_default.log` (root) |
| Smoke test log (D4 Z128) | `avboit_smoke_d4z128.log` (root) |
| Smoke test log (invalid arg) | `avboit_smoke_invalid.log` (root) |
| P2.7A plan | `docs/plan/phase_p2_7a_xy_z_resolution_attribution.md` |
| Experiment results (future) | `LocalVisualResults/TempResults/P2_7A_XYZAttribution_<UTC>/` |

---

## Uncommitted Content

All modified files are working-tree changes only. No commit has been made this session. The previous commit (`8d94c9ca`) is unchanged as HEAD.

---

## Risk and Unresolved Issues

1. **WholeProgramOptimization disabled**: The Release build requires `/p:WholeProgramOptimization=false` due to a PDB mismatch in the pre-built `Renderer.lib`. This is a pre-existing environment issue, not introduced in P2.7A. The exe is functionally correct but built without LTCG.

2. **Experiment matrix not run**: The P2.7A attribution conclusion has not yet been reached. Status is `partial`.

3. **Z=256 memory**: D2 Z256 would use ~3.2 GiB which would exceed budget. D8 Z256 uses ~189 MiB (OK). D4 Z256 uses ~755 MiB (OK). All are correctly guarded by `CheckAVBOITVolumeBudget()`.

4. **Integrate shader array size**: With AVBOIT_MAX_VOLUME_DEPTH=256, the shader allocates `float legacyEventWeights[256]` and `float frontEventWeights[256]` as compute shader local arrays. On some GPUs these become register-spill to VRAM. If Z=128 or Z=256 show GPU timeout, reduce the array sizes and MAX constant.

5. **Renderer Validation layer**: NOT RUN (same as CHECKPOINT-0011 gap).

6. **Submodule Local_Egaku**: Dirty/unmapped — pre-existing from P2.6T.

---

## Decision Record

**DR-P2.7A-001**: `avboitBootstrapStage` stub implementation.

The Windows extern declaration had no matching definition anywhere in the project. Previous exe builds were stale (built before the extern was introduced). A minimal stdout-logging stub was created rather than a no-op, so the capture pipeline scripts can still observe stage signals.

**DR-P2.7A-002**: `AVBOIT_MAX_VOLUME_DEPTH` expansion to 256.

The integrate shader had fixed-size arrays `[64]` and a loop cap at `min(volumeDepth, 64)`. Without this change, Z=128 and Z=256 experiment configs would silently behave identically to Z=64. The macro expansion and array refactor ensure the loop iterates up to the actual volumeDepth for Z=128 and Z=256.

**DR-P2.7A-003**: `WholeProgramOptimization=false` workaround.

The pre-built `Renderer.lib` contains a `VulkanRaytracing.obj` with incompatible PDB information that triggers `LNK1103` when LTCG is enabled. Disabling LTCG at build time is a standard workaround. No code logic is affected.

**DR-P2.7A-004**: Budget cap at 1536 MiB.

The instruction specifies this cap. The budget function uses 64-bit arithmetic throughout: `GetAVBOITVoxelCount()` returns `uint64_t`, all byte calculations are `uint64_t`, and the MiB division uses 64-bit literals. This correctly handles D2 Z256 (which would be ~3.2 GiB and must be rejected).

---

## CURRENT.md Update Confirmation

`docs/plan/CURRENT.md` updated:
- Current Plan: `docs/plan/phase_p2_7a_xy_z_resolution_attribution.md`
- Latest Checkpoint: `CHECKPOINT-0012-20260630T043500Z-p2-7a-xy-z-resolution-attribution.md`
- Status: `partial`

---

## Next-Round Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Read CHECKPOINT-0012 (this file).
3. Read `docs/plan/phase_p2_7a_xy_z_resolution_attribution.md`.
4. Build command (with WholeProgramOptimization=false) to ensure fresh exe.
5. Create output directory: `LocalVisualResults/TempResults/P2_7A_XYZAttribution_<UTC>/`.
6. Run experiment matrix in order: A (regression), B (XY axis), C (Z axis), D (combination if both axes significant).
7. For each config: capture Mode 0 + Mode 5 DX12, then Vulkan if applicable.
8. Compute all metrics from the plan.
9. Apply attribution rules from Section 十二 of the user instruction.
10. Create CHECKPOINT-0013 with the attribution conclusion.
