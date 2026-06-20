# PLAN-1-0：固定并构建 The Forge 1.58

## 本轮目标

取得并固定 The Forge 1.58 的精确源码，建立可重复的构建与运行基线。暂不修改渲染算法。

## 学习目标

- 理解仓库版本、依赖与构建系统如何共同定义“可复现实验”；
- 理解为什么不能直接使用 master；
- 能说明 `15_Transparency` 在实验路线中的角色。

## Agent 任务

1. 验证仓库 HEAD 与目标 commit 完全一致；
2. 记录操作系统、编译器、图形 API、GPU、构建配置；
3. 按该版本自身说明完成依赖准备、构建和运行；
4. 定位 `15_Transparency`；
5. 保存首个未修改运行证据；
6. 所有环境修正必须单独记录，不得与算法改动混在一起。

## 禁止事项

- 不更新到新版本；
- 不加入 AVBOIT；
- 不改测试内容；
- 不重构现有透明代码；
- 不开始 UE 工作。

## 交付物

- `BASELINE_REPORT.md`；
- 精确构建命令；
- 运行截图或捕获；
- 环境问题及解决记录；
- 下一计划 `PLAN-1-1.md` 的进入建议。

## 验收

在全新或清理后的构建目录中，可按记录步骤再次成功运行 `15_Transparency`。

## 强制 Checkpoint 归档门禁

本 Plan 中每条用户指令结束时，无论结果为成功、部分完成、阻塞、失败或无改动，Agent 都必须在回复前：

1. 创建新的 `docs/checkpoints/archive/CHECKPOINT-*.md`；
2. 追加 `docs/checkpoints/CHECKPOINT_INDEX.md`；
3. 更新 `docs/plan/CURRENT.md`；
4. 在最终回复中给出 checkpoint 路径、状态和下一恢复入口。

未完成归档时，本轮不得标记为完成，也不得进入下一 Plan。
