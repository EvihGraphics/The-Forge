# Current Work State

## Route

Primary skill: `docs/skill/avboit-learning-development-skill-v1/SKILL.md`

Checkpoint skill: `docs/skill/checkpoint-archive-skill/SKILL.md`

Current lab skill: `docs/skill/theforge-avboit-lab-skill/SKILL.md`

## Active Branch

`baseline/theforge-1.58-windows-vs-dx12`

Verified P2.6R start point: `91163ff9d7956a670d8562e73376de3ad9b789db`

## Latest Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0009-20260628T054228Z-p2-6r-direction-closure.md`

Status: `blocked-local`

## Latest State

P2.6R restored runtime auto-capture and captured overlapping DX12 analytic evidence in `LocalVisualResults/P2_6R_DirectionClosure_20260628T054228Z/`.

Overlap validation passes (`12914` two-layer overlap pixels and `12914` three-way overlap pixels). Direction plumbing is visible in debug views `7` and `8`, but all `37 / 37` paired `Debug0` final legacy/front captures are byte-identical. The default direction remains `legacy`; no front-default commit was made.

## Current Plan

`docs/plan/phase_p2_6r_runtime_direction_closure.md`

## Validation Snapshot

- Build: PASS with Release x64 MSBuild after setting `FSL_COMPILER_DXC` to Windows Kits `10.0.26100.0\x64`.
- Runtime auto-capture: PASS.
- Two-layer and three-layer overlap: PASS.
- Direction debug plumbing: PASS.
- Direction final-output improvement: FAIL, final legacy/front outputs are byte-identical.
- Front-default switch: NOT COMMITTED.
- Vulkan analytic, default scene, cross-API, coverage, and performance gates: NOT RUN after the DX12 direction gate failed.

## Resume Entry

1. Stay on branch `baseline/theforge-1.58-windows-vs-dx12`.
2. Confirm latest local P2.6R commits with `git log -8 --oneline`.
3. Use `LocalVisualResults/P2_6R_DirectionClosure_20260628T054228Z/metrics/direction_dx12/dx12_direction_gate_summary.json` as the current blocked evidence.
4. Investigate why direction-dependent weights alter debug views but not final resolved Debug0 output.
5. Do not switch default direction to `front` until final output improves against Mode0 and the Vulkan/default/perf gates run.
