# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced`

Base: `origin/baseline/theforge-1.58-windows-vs-dx12` @ `c2b643ae770aa3bc7fc8fd5e4a06d5e3fed6eafc`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0004-20260621T055006Z-PLAN-4-0-clean-avboit-checkpoint.md`

Status: `passed-local`

## Latest State

A clean checkpoint branch was created from the remote baseline. Only AVBOIT source, docs, and reusable scripts were restored from the local 081bf9f4 donor state. The large local `Art/` tree, screenshots, `LocalVisualResults/`, `Local_Egaku/`, scratch files, and patch/inject experiments are ignored and excluded from the checkpoint diff.

Build and runtime verification passed locally for `15_Transparency` DX12. The clean checkpoint capture confirms AVBOIT mode 5 is selected, but `PrintWindow` does not faithfully capture the DX12 swapchain. The user-supplied AVBOIT reference is the visual source of truth: skybox, ground, and opaque objects are visible, while most transparent objects are absent compared with the baseline.

## Visual References

- User AVBOIT reference: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_5_AVBOIT.png`
- User baseline reference: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Default_01.png`
- Clean checkpoint capture: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_5_AVBOIT_CleanCheckpoint.png`

## Current Goal

Continue AVBOIT development from the clean checkpoint branch. The next technical goal is to compare the baseline and current AVBOIT screenshots, then debug the AVBOIT shader/resource/render path responsible for missing transparent geometry.

## Current Plan

`docs/plan/theforge_avboit/PLAN-4-0.md`

## Resume Entry

1. Stay on branch `AVBOIT_Agent_Guidance_Package_v2_Checkpoint_Enforced`.
2. Read `CHECKPOINT-0004-20260621T055006Z-PLAN-4-0-clean-avboit-checkpoint.md`.
3. Use ignored local resources and outputs only for build/run reproduction.
4. Compare `UT_15_Transparency_DX12_Default_01.png` against `UT_15_Transparency_DX12_Mode_5_AVBOIT.png`.
5. Debug AVBOIT mode 5 until transparent geometry appears and the visual result approaches the baseline scene.
