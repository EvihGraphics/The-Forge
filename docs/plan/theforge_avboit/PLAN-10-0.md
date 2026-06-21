# PLAN-10-0：Niagara Adapter（Deferred）

只有独立 UE Flipbook Player 稳定后启用。

Niagara 负责产生粒子实例与动画数据，AVBOIT 继续只负责透明合成。不得把 AVBOIT 改造成粒子模拟器。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
