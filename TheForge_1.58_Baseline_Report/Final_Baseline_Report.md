# Final Baseline Report

Generated: 2026-06-20T01:50:11+08:00

## Execution Summary
- Fixed version checkout: PASS, HEAD is 2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d.
- Visual Studio solution: PASS, checked-in VS2019 Unit_Tests.sln was used.
- Whole Unit Tests solution build attempted: YES.
- Final executable production: 19/19 counted Unit Test executables present.
- Visual record: 18 accepted PNG screenshots; 36_AlgorithmsAndContainers is non-visual/automation-limited.
- Primary Graphics Backend: DX12.
- AVBOIT implementation: NOT PERFORMED.

## Environment Summary
| Field | Value |
|---|---|
| OS | Windows 11 Pro 10.0.26200 |
| Visual Studio original target | VS2019/v142, SDK 10.0.17763.0 |
| Visual Studio used for final output | VS2022 Community 17.13, v143 |
| SDK used | 10.0.22621.0 |
| GPU | NVIDIA GeForce RTX 4060 Ti |
| Driver | WMI 32.0.15.9186 / NVIDIA 591.86 |
| DX12 | PASS |
| Vulkan | NOT_TESTED; runtime present, validation layer missing |
| Primary API | DX12 |
| Build Configuration | Release|x64 |

## Repository Summary
| Field | Value |
|---|---|
| Fork | https://github.com/EvihGraphics/The-Forge |
| Upstream | https://github.com/ConfettiFX/The-Forge |
| Commit | 2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d |
| Release | 1.58 |
| Date | 2024-06-17 |

## Build Statistics
| Metric | Count |
|---|---:|
| Discovered Unit Tests | 19 |
| Successful executable builds | 19 |
| Build failed compile/link | 0 |
| Post-build copy failures | 2 projects |
| Missing/generated Project | 0 |
| Warning total | 0 compiler warnings counted in final accepted compile log |
| Error total | 0 compile/link errors after adaptation; solution exit code remains 1 due post-build xcopy failures |

## Runtime Statistics
| Metric | Count |
|---|---:|
| PASS | 13 |
| PASS_WITH_WARNINGS | 5 |
| MANUAL_INTERACTION_REQUIRED | 1 |
| Launch failed | 0 |
| Runtime failed | 0 blocking crashes observed |
| Visual invalid | 0 accepted screenshots |
| Platform unsupported | 0 |
| Screenshots | 18 accepted PNGs |

## Backend Conclusion
Primary Graphics Backend: DX12

Fallback Backend: DX12

Fallback Reason: Vulkan runtime and driver are present, but VK_LAYER_KHRONOS_validation was not visible. DX12 was selected as the official first-pass backend and completed the visual baseline.

Vulkan Validation: NOT_TESTED

Cross-Backend Validation: NOT_PERFORMED

## 15_Transparency Conclusion
- Existing modes: Alpha blended, Weighted Blended OIT, Volition Weighted Blended OIT, Phenomenological Transparency, Intel Adaptive OIT.
- Default runtime visual: PASS_WITH_WARNINGS under DX12, accepted screenshot captured.
- AOIT status: present and enabled by runtime GPU settings because RasterOrderViewSupport == 1 on RTX 4060 Ti/DX12.
- Particle/transparent geometry: visible in the default 15_Transparency scene.
- Per-mode screenshots: incomplete; UI/script automation attempts did not reliably switch the regular build mode.
- AVBOIT status: absent, as required for the original baseline.
- Before comparing a new AVBOIT path, capture a clean per-mode visual set with reliable official automation or manual controlled UI interaction.

## Modifications And Patches
- Source modified: YES, one toolchain adaptation in Common_3/Application/Config.h.
- Shader modified: NO.
- Build scripts modified: NO.
- Transparency/OIT algorithms modified: NO.
- UI modified: NO.
- Patch file: Patches/toolchain_vs2022_1938_whitelist.patch.
- Patch type: toolchain adaptation for VS2022/MSVC 1938 only.
- Original baseline attempts and logs were preserved before patching.

## Final Judgment
READY_WITH_LIMITATIONS

The baseline is usable for beginning AVBOIT development on DX12 because the fixed commit, resources, build outputs, runtime logs, 18 visual screenshots, and 15_Transparency source/mode inventory are all recorded. The limitations are important: the run required a VS2022 toolchain patch, the final solution still has post-build resource-copy errors, Vulkan was not validated, and 15_Transparency per-mode screenshots were not fully captured.
