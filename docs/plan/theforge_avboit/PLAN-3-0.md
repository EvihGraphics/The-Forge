# PLAN-3-0：AVBOIT 理论与参考实现学习

## 目标

在写 AVBOIT 代码前，形成一份不依赖 The Forge API 的算法契约。

## 必读资料

- `sources/pdf/AVBOIT_SIG2025_MDROBOT-final.pdf`
- `sources/reference_code/EgakuRenderPipeline.zip`
- `docs/knowledge/01_algorithm/AVBOIT_READING_GUIDE.md`
- `docs/knowledge/03_reference_implementations/EGAKU_GUIDE.md`

## 交付物

- AVBOIT 抽象阶段图；
- 每阶段输入、输出和不变量；
- Alpha、消光、透射率定义；
- 深度表示与映射约定；
- 正式 PDF 与 Egaku 的一致点和差异；
- 第一版最小实现范围；
- 暂不支持功能清单。

## 验收

用户能够解释 AVBOIT 为什么不是粒子系统、为什么需要低分辨率预通路，以及它与 WBOIT、AOIT 的本质差异。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
