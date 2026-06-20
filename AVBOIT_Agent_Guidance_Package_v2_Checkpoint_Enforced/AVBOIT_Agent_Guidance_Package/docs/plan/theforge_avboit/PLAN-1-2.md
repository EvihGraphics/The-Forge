# PLAN-1-2：恢复现有模式并关闭基线 Checkpoint

## 前置条件

`PLAN-1-0.md` 与 `PLAN-1-1.md` 已通过。

## 目标

确认现有透明模式能够切换、运行并生成可比较证据，形成 AVBOIT 开发前的不可变基线。

## 交付物

- 每种现有后端的截图与模式名称；
- 同一场景、相机、分辨率下的基线性能记录；
- 已知平台差异；
- 未修改基线的 commit/tag；
- Checkpoint 总结与是否进入 `PLAN-2-0.md` 的结论。

## 验收

现有后端均可识别，比较条件一致，结果可重复。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
