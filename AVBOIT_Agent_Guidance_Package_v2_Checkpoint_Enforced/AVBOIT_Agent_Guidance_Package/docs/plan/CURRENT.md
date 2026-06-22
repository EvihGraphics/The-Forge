# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

Base: `origin/baseline/theforge-1.58-windows-vs-dx12` @ `c2b643ae770aa3bc7fc8fd5e4a06d5e3fed6eafc`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0005-20260621T153700Z-PLAN-4-0-grayscale-resolved.md`

Status: `passed-local`

## Latest State

The AVBOIT grayscale rendering bug was successfully resolved. The root cause was identified as a missing `LightUniformBlock` descriptor binding in the AVBOIT forward pass, which caused the lighting calculation to output `(0, 0, 0)` for RGB colors while maintaining alpha-based extinction. The descriptor updates were corrected (4 params for splat, 5 params for forward). Mode 5 now renders full RGB colors on transparent panels, matching the Mode 0 ground truth pixel-for-pixel on the sample panels, achieving an overall SSIM of 0.955. The remaining MAE (0.028) is an expected algorithmic property of AVBOIT (lack of intra-voxel occlusion ordering).

## Visual References

- User AVBOIT reference: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_5.png`
- User baseline reference: `LocalVisualResults/HIVE_4090x2/VisualResults/Screenshots/UT_15_Transparency_DX12_Mode_0.png`

## Current Goal

Review and refine AVBOIT performance metrics, and prepare to advance to the next planning stage defined in `ROADMAP.md` (e.g., OIT Comparative Experiments or Unreal Engine migration preparations).

## Current Plan

`docs/plan/theforge_avboit/PLAN-4-0.md`

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Read `CHECKPOINT-0005-20260621T153700Z-PLAN-4-0-grayscale-resolved.md`.
3. Validate AVBOIT performance and transition to OIT Comparison or UE migration based on user guidance.
