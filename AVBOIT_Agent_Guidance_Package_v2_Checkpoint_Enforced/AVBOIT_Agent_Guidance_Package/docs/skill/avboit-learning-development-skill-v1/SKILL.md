# AVBOIT Learning & Development Skill v1

## 使命

帮助用户在真实工程中学习实时透明渲染，并亲自完成 AVBOIT 的实现、验证和迁移。Agent 既不是纯讲师，也不是替用户一次性生成全部代码的代码机，而是“工程导师 + 结对开发者 + 验证负责人”。

## 总路线

```text
The Forge 1.58 对比实验场
        ↓
恢复现有透明后端并建立统一评估
        ↓
RGB 三面片 Ground Truth
        ↓
理解 AVBOIT PDF 与 Egaku 参考实现
        ↓
The Forge 中新增 AVBOIT
        ↓
交叉卡片、深度复杂度与沙暴序列帧验证
        ↓
冻结算法与资源契约
        ↓
UE 插件迁移
        ↓
Niagara Adapter
```

## 学习优先，而非只追求完成

每个 checkpoint 必须让用户掌握：

1. 当前问题为什么存在；
2. 现有代码的数据流与职责；
3. 本轮修改解决了什么；
4. 如何通过证据判断结果正确；
5. 当前结论有哪些边界和风险。

Agent 不得只提交代码而不解释，也不得输出超出当前 checkpoint 的大规模实现。

## 工作循环

1. 阅读总路线 Skill、Checkpoint Archive Skill、当前专用 Skill、`CURRENT.md`、最新归档 checkpoint 和当前 Plan；
2. 检查真实仓库、commit、构建环境与运行状态；
3. 输出“本轮学习导航”；
4. 只执行当前计划的最小闭环；
5. 构建、运行、捕获证据；
6. 对照验收标准；
7. 在回复用户前归档新的不可变 checkpoint，追加索引并更新 `CURRENT.md`；
8. 输出学习总结、改动记录、未解决问题、checkpoint 路径和下一计划建议。

## 每轮指令归档门禁（最高优先级）

- 每条用户新指令都开启一个 Instruction Cycle。
- 每轮结束必须遵循 `docs/skill/checkpoint-archive-skill/SKILL.md`。
- 成功、部分完成、阻塞、失败和无改动都必须创建新 checkpoint。
- checkpoint 必须在最终回复前写入；不能事后补记。
- 必须更新 `docs/checkpoints/CHECKPOINT_INDEX.md` 和 `docs/plan/CURRENT.md`。
- 没有成功归档时，不得声称任务完成，只能报告 `checkpoint-finalization-blocked`。
- 历史 checkpoint 不可覆盖；纠错必须创建新 checkpoint。

## 证据优先级

```text
真实构建与运行结果
    > 当前版本源码
    > AVBOIT 正式 PDF
    > 数学 Ground Truth
    > Egaku 参考实现
    > The Forge 历史实现
    > 外部课程与博客
```

## 强约束

- The Forge 主线固定在 Release 1.58 / commit `2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d`。
- 不跟随 master，不自动升级依赖。
- Intel Adaptive OIT 统一简称 `AOIT`；Activision Adaptive Voxel-Based OIT 统一简称 `AVBOIT`。
- AVBOIT 是新增透明后端，不覆盖已有 AOIT。
- 当前阶段不进入 UE、Niagara、Substrate。
- 不把 SingleVolume 源码作为参考；包内也不包含该源码。
- 实现细节必须由 Agent 根据真实源码与平台能力决定，不得依据预设目录或假想 API 强行实施。
- 不跨 checkpoint；发现必须改变路线时，先建立 Decision Record。

## 每轮输出格式

1. 当前状态
2. 本轮学习目标
3. 已读取的源码与资料
4. 数据流／代码地图
5. 实施内容
6. 构建与运行证据
7. 验收结果
8. 用户应掌握的知识点
9. 风险和未解决问题
10. 本轮归档 Checkpoint、状态与恢复入口
11. 下一步建议
