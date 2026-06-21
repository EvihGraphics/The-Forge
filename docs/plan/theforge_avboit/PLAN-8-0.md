# PLAN-8-0：算法冻结与 UE 迁移契约

## 目标

把 The Forge 实现中与图形 API 和框架无关的部分冻结为 UE 可消费的规范。

## 必须冻结

- 算法阶段及顺序；
- 各阶段输入输出；
- 数学和深度约定；
- 质量参数；
- 资源预算；
- 验证场景；
- 调试视图；
- 已知限制；
- 平台能力要求。

## 不冻结

- UE 类、模块和目录；
- UE 扩展入口；
- UE Shader 组织；
- Niagara 接口。

## 退出条件

UE Agent 不阅读 The Forge 具体 API，也能依据迁移契约说明需要重建的算法数据流。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
