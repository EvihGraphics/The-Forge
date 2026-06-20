# PLAN-0-0：项目基线与学习规约

## 目标

固定版本、资料和职责边界，避免 Agent 在错误分支或错误目标上开发。

## 完成项

- The Forge 主基线锁定为 Release 1.58 / `2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d`；
- Release 1.16 / `9ec216b40968365299362b305c0fed2f97d4be1b` 只作为历史参考；
- AVBOIT 与 AOIT 名称边界已定义；
- The Forge、UE、Niagara 三阶段已分开；
- SingleVolume 源码已列入排除清单。

## 退出条件

指导包、Prompt、Current Plan 和资料目录可被 Agent 正确读取。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
