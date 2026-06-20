# PLAN-4-0：在 The Forge 新增 AVBOIT 基础后端

## 目标

把 AVBOIT 作为第六种独立透明后端接入，不覆盖现有 AOIT。

## 原则

- 实现细节由 Agent 在读取 Release 1.58 实际源码后决定；
- 每个新增阶段都必须可捕获或可视化；
- 优先形成最小正确闭环，再讨论稀疏化、RGB 扩展和优化；
- 不改变其他后端的比较条件。

## 交付物

- 可切换的 AVBOIT 后端；
- RGB 面片结果；
- 阶段证据；
- 改动说明与 Decision Records；
- 已知限制。

## 退出条件

六种提交顺序下结果稳定，并能与 Ground Truth 对比。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
