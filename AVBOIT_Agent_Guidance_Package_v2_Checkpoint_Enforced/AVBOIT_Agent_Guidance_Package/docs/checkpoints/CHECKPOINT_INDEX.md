# Checkpoint Index

> Append-only checkpoint archive. The latest recovery pointer is `docs/plan/CURRENT.md`.

| Seq | Checkpoint | UTC Time | Status | Plan / Stage | Summary |
|---:|---|---|---|---|---|
| 0001 | [`CHECKPOINT-0001-20260619T123200Z-PACKAGE-checkpoint-policy.md`](archive/CHECKPOINT-0001-20260619T123200Z-PACKAGE-checkpoint-policy.md) | 2026-06-19T12:32:00Z | passed | Guidance Package / PLAN-1-0 pending | Added mandatory checkpoint archive protocol. |
| 0004 | [`CHECKPOINT-0004-20260621T055006Z-PLAN-4-0-clean-avboit-checkpoint.md`](archive/CHECKPOINT-0004-20260621T055006Z-PLAN-4-0-clean-avboit-checkpoint.md) | 2026-06-21T05:50:06Z | passed-local | PLAN-4-0 | Clean AVBOIT source checkpoint with Art, screenshots, local results, and scratch files ignored. |
| 0005 | [`CHECKPOINT-0005-20260621T153700Z-PLAN-4-0-grayscale-resolved.md`](archive/CHECKPOINT-0005-20260621T153700Z-PLAN-4-0-grayscale-resolved.md) | 2026-06-21T15:40:00Z | passed-local | PLAN-4-0 | AVBOIT grayscale rendering resolved (LightUniformBlock binding fix). SSIM 0.955 achieved. |
| 0007 | [`CHECKPOINT-0007-20260627T033223Z-p2-fullres-resolve-vulkan-parity.md`](archive/CHECKPOINT-0007-20260627T033223Z-p2-fullres-resolve-vulkan-parity.md) | 2026-06-27T03:32:23Z | passed-local | P2 full-res resolve | Full-resolution AVBOIT accumulation/resolve, Release Vulkan selection, and coverage invariant passed locally. |
| 0008 | [`CHECKPOINT-0008-20260627T112835Z-p2-6-color-parity.md`](archive/CHECKPOINT-0008-20260627T112835Z-p2-6-color-parity.md) | 2026-06-27T11:28:35Z | blocked-local | P2.6 color parity | Deterministic capture and analytic direction harness implemented; front-default switch blocked by incomplete overlapping analytic runtime captures. |
