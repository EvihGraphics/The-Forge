# PLAN-7-0：性能、显存与质量档位冻结

## 目标

确定 AVBOIT 是否值得迁移到 UE，并形成产品可用的预算结论。

## 交付物

- 质量档位；
- 各档图像差异；
- GPU Pass 成本；
- 显存与中间资源预算；
- 分辨率与深度复杂度敏感性；
- 目标内容建议；
- 不适用场景与失败条件。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
