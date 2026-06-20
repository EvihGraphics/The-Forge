# Current Work State

## 总路线

`docs/skill/avboit-learning-development-skill-v1/SKILL.md`

## 状态归档 Skill

`docs/skill/checkpoint-archive-skill/SKILL.md`

## 当前专用 Skill

`docs/skill/theforge-avboit-lab-skill/SKILL.md`

## 当前 Checkpoint 范围

`docs/plan/theforge_avboit/PLAN-1-*.md`

## 最新归档 Checkpoint

`docs/checkpoints/archive/CHECKPOINT-0001-20260619T123200Z-PACKAGE-checkpoint-policy.md`

## 最新状态

`passed` — 指导包已经加入“每条用户指令结束后必须归档当前状态”的强制门禁。该状态不代表 The Forge 已经构建。

## 当前目标

固定并恢复 The Forge Release 1.58 的 `15_Transparency` 对比实验场，确认现有透明后端能够构建、运行和切换；建立代码地图、运行证据和学习笔记。在完成这些工作前，不实现 AVBOIT，不修改测试场景，不迁移到 UE。

## 当前计划

`docs/plan/theforge_avboit/PLAN-1-0.md`

## 当前完成定义

- 仓库 HEAD 精确固定到 `2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d`；
- `15_Transparency` 成功构建并运行；
- 已确认现有透明模式及其切换入口；
- 已保存基线截图、GPU 标记或捕获证据、构建命令和环境信息；
- 用户能够解释该实验场的输入、透明后端和评估输出三层关系；
- 当前 Instruction Cycle 已归档新 checkpoint、追加索引并更新本文件。

## 下一轮精确恢复入口

1. 阅读最新归档 checkpoint；
2. 执行 `PLAN-1-0.md`；
3. 核验真实 The Forge 仓库与目标 commit；
4. 回复用户前创建下一份不可变 checkpoint。
