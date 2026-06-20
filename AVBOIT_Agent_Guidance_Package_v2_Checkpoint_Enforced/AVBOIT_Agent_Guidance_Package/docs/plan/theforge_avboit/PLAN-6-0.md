# PLAN-6-0：序列帧沙暴卡片实验

## 目标

把抽象 OIT 测试推进到项目目标内容：多张重叠、动态播放的沙暴 Flipbook 卡片。

## 关注点

- 大面积低 Alpha 累积；
- 前后层次保持；
- 动画帧变化；
- 卡片提交顺序变化；
- 相机运动稳定性；
- 高深度复杂度；
- 与现有粒子场景的可比性。

## 边界

此阶段仍在 The Forge，不涉及 UE 播放器或 Niagara。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
