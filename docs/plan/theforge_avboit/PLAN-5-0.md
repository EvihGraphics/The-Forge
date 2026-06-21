# PLAN-5-0：统一 OIT 对比实验

## 目标

在公平条件下比较现有透明后端与 AVBOIT。

## 测试维度

- 非交叉透明面片；
- 交叉卡片；
- 透明层数和屏幕覆盖率；
- Alpha 分布；
- 相机移动；
- Draw 提交顺序；
- 图像误差；
- GPU 时间与显存。

## 重要限制

交叉几何中，对象级 Sorted Alpha 不再自动视为逐像素 Ground Truth。实验报告必须区分正确性参考、近似基线和产品视觉评价。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
