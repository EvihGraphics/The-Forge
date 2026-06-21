# PLAN-2-0：RGB 三面片 Ground Truth

## 目标

建立 AVBOIT 后续所有修改都必须通过的最小正确性测试。

## 核心协议

- 红、绿、蓝三张透明面片具有固定且不交叉的物理深度；
- 使用统一 Alpha；
- 循环六种 Draw 提交排列；
- Sorted Alpha 只在这一类可正确排序的场景中充当 Ground Truth；
- 比较图像、数值误差和连续切换时的闪烁。

## 学习目标

理解“物理深度顺序”和“提交顺序”的区别，以及为什么 OIT 只应对后者不敏感。

## 退出条件

测试可自动或半自动重复，基线值与误差标准被记录。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
