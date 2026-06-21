# PLAN-X-Y：标题

## 前置条件

## 本轮目标

## 学习目标

## 必读源码与资料

## Agent 任务

## 禁止事项

## 交付物

## 验收标准

## Checkpoint 退出条件

## 强制 Checkpoint 归档门禁

每条用户指令结束后，无论成功、部分完成、阻塞、失败或无改动，必须在回复前：

1. 创建新的不可变 checkpoint；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在回复中报告 checkpoint 路径、状态和恢复入口。

未归档不得声称完成或进入下一 Plan。
