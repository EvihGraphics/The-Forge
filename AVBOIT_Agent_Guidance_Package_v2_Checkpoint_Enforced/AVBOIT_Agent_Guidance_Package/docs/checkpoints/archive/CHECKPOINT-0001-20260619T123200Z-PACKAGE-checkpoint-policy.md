# CHECKPOINT-0001：指导包加入强制归档协议

## Metadata

- **Checkpoint ID**：`CHECKPOINT-0001`
- **UTC Time**：`2026-06-19T12:32:00Z`
- **Status**：`passed`
- **Previous Checkpoint**：`none`
- **Supersedes**：`none`

## 用户指令摘要

为 AVBOIT Agent 指导包增加强约束：每次用户指令结束后，必须归档 checkpoint，即当时的完整当前状态。

## 当前路线与计划

- 总路线：`docs/skill/avboit-learning-development-skill-v1/SKILL.md`
- 状态归档 Skill：`docs/skill/checkpoint-archive-skill/SKILL.md`
- 当前专用 Skill：`docs/skill/theforge-avboit-lab-skill/SKILL.md`
- 当前 Plan：`docs/plan/theforge_avboit/PLAN-1-0.md`

## 本轮实施

- 新增跨阶段 `Checkpoint Archive Skill v1`；
- 新增 checkpoint 目录、索引和模板；
- 将“每条用户指令都必须归档”写入总路线、专用 Skill、全部现有 Plan、Prompt 和报告模板；
- 将归档动作设为最终回复前的完成门禁；
- 规定成功、部分、阻塞、失败和无改动均必须归档；
- 更新 `CURRENT.md` 指向本 checkpoint；
- 保持 The Forge 1.58、AVBOIT 路线和 SingleVolume 源码排除规则不变。

## 工程状态

本 checkpoint 记录的是指导包文档自身的更新，不代表 The Forge 仓库已经拉取、构建或运行。

- The Forge 目标版本：Release 1.58
- 目标 commit：`2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d`
- 当前实际 The Forge HEAD：尚未由开发 Agent 核验
- 当前 Plan 状态：等待执行 `PLAN-1-0`

## 修改与新增文件

- `README.md`
- `docs/knowledge/00_project/PROJECT_CHARTER.md`
- `docs/plan/CURRENT.md`
- `docs/plan/theforge_avboit/PLAN-*.md`
- `docs/plan/theforge_avboit/ROADMAP.md`
- `docs/skill/avboit-learning-development-skill-v1/SKILL.md`
- `docs/skill/theforge-avboit-lab-skill/SKILL.md`
- `docs/skill/ue-avboit-migration-skill/SKILL.md`
- `docs/skill/checkpoint-archive-skill/SKILL.md`
- `docs/checkpoints/README.md`
- `docs/checkpoints/CHECKPOINT_INDEX.md`
- `docs/templates/CHECKPOINT_TEMPLATE.md`
- `docs/templates/PLAN_TEMPLATE.md`
- `docs/templates/SESSION_REPORT_TEMPLATE.md`
- `prompt/AGENT_PROMPT_FULL.md`
- `prompt/AGENT_PROMPT_COMPACT.md`

## 验证结果

- 强制协议已进入完整版和精简版 Prompt；
- 所有现有阶段 Plan 均包含 checkpoint 归档门禁；
- `CURRENT.md` 已指向本文件；
- 本 checkpoint 已加入索引；
- 包内仍不包含 `SingleVolume.zip`。

## 风险与未解决问题

- 真正开发 The Forge 时，Agent 需要使用真实仓库命令补全 branch、HEAD、submodule、toolchain、GPU 和运行证据；
- 当前 checkpoint 仅归档指导包状态，不能替代 `PLAN-1-0` 的首个仓库基线 checkpoint。

## 当前可复现状态

指导包已经具备“读取旧状态 → 执行指令 → 归档新状态 → 更新 CURRENT → 回复用户”的闭环规约。

## 下一轮精确恢复入口

1. 读取 `docs/plan/CURRENT.md`；
2. 读取本 checkpoint；
3. 执行 `docs/plan/theforge_avboit/PLAN-1-0.md`；
4. 核验 The Forge 真实仓库状态；
5. 无论结果如何，在回复前创建 `CHECKPOINT-0002`。

## CURRENT 更新确认

- `docs/plan/CURRENT.md`：已更新
- `docs/checkpoints/CHECKPOINT_INDEX.md`：已追加
