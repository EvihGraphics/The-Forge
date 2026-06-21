# PLAN-9-0：UE 插件学习与独立 Flipbook Player（Deferred）

只有 `PLAN-8-0.md` 通过后启用。

第一产品目标是独立 AVBOIT 序列帧沙暴卡片播放器。具体 UE 接入、资源、Pass 和目录，由 Agent 根据目标 UE 版本真实源码决定。本阶段不直接接入 Niagara。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
