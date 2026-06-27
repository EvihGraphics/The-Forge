# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

Verified P2.6 start point: `83b3f8e4e47e7272441a9fb53f6cfc7fd4eda4af`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0008-20260627T112835Z-p2-6-color-parity.md`

Status: `blocked-local`

## Latest State

P2.6 implemented deterministic capture controls, JSON metadata sidecars, analytic test scenes, unlit analytic material output, `legacy|front` transmittance direction selection, and extended AVBOIT debug views. The default direction remains `legacy` because the analytic direction gate did not complete after the overlap fix.

The first two-layer analytic captures were invalidated because layers did not overlap on screen. The scene was corrected to place layers along the camera ray, but subsequent local runtime auto-capture became unstable (`exit -1` or wait timeout without screenshot/log). Do not promote `front` to default until the overlapping analytic matrix is recaptured and passes.

## Current Plan

`docs/plan/phase_p2_6_transmittance_direction_color_parity.md`

## Validation Snapshot

- Build: PASS with Release x64 MSBuild after setting `FSL_COMPILER_DXC` to Windows Kits `10.0.26100.0\x64`.
- Deterministic capture/metadata: PARTIAL PASS.
- Single-layer analytic smoke: PASS within PNG quantization, but non-discriminating.
- Two-layer direction gate: BLOCKED after overlap correction due local runtime no-log/no-screenshot launch instability.
- Front-default switch: NOT COMMITTED.
- Default scene, cross-API, coverage, and performance gates: NOT RUN for P2.6.

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Confirm latest local P2.6 commits with `git log -6 --oneline`.
3. Ensure no stale `15_Transparency.exe` process is running before runtime tests.
4. Rebuild with `FSL_COMPILER_DXC` pointed at a Windows Kits DXC directory if the repo-local DXC cannot load `dxcompiler.dll`.
5. Resolve the no-log/exit-`-1` auto-capture blocker, then recapture overlapping analytic cases from `ba103708` or later.
6. Commit front-default direction only after analytic, default-scene, cross-API, coverage, and performance gates pass.
