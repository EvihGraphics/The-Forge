# Checkpoint Archive Skill v1

## 使命

确保 Agent 驱动开发可以在任意一次中断、失败、换人或换会话后，从**可验证的当前状态**继续，而不是依赖聊天记忆或模糊描述。

本 Skill 是跨阶段强制规约，优先级高于各阶段 Plan 的普通流程要求。The Forge、UE 插件和未来 Niagara 阶段均必须遵守。

## Instruction Cycle 定义

每次收到用户的一条新指令，即开始一个新的 **Instruction Cycle**。无论该指令最终属于以下哪种情况，都必须在回复用户之前归档一次 checkpoint：

- 完成了代码或文档修改；
- 只完成了调查、阅读、构建或性能测试；
- 没有产生文件修改；
- 任务只完成了一部分；
- 因环境、权限、编译或运行问题被阻塞；
- 任务失败、取消或用户改变方向。

**无改动不等于无 checkpoint。失败也必须归档。**

## 不可绕过的完成门禁

一轮指令只有同时满足以下条件，才允许被描述为“完成”：

1. 已捕获真实仓库与环境状态；
2. 已生成新的、不可变的 checkpoint 文件；
3. 已把该 checkpoint 追加到 `docs/checkpoints/CHECKPOINT_INDEX.md`；
4. 已更新 `docs/plan/CURRENT.md`，使其指向最新 checkpoint；
5. 已验证 checkpoint 中引用的关键证据路径存在，或明确标记为外部证据；
6. 最终回复中明确给出 checkpoint 路径和本轮状态。

缺少任意一项时，不得声称本轮完成。必须报告 `checkpoint-finalization-blocked` 以及阻塞原因。

## 归档目录与命名

所有不可变 checkpoint 放置在：

```text
docs/checkpoints/archive/
```

推荐命名：

```text
CHECKPOINT-<递增序号>-<UTC时间>-<PLAN或阶段>-<简短主题>.md
```

示例：

```text
CHECKPOINT-0007-20260620T031500Z-PLAN-1-0-baseline-build.md
```

规则：

- 序号单调递增；
- 文件一经归档禁止覆盖、删除或就地修正；
- 发现错误时创建新的 checkpoint，并通过 `Supersedes` 指向旧文件；
- `CURRENT.md` 是可变指针，`archive/` 中的 checkpoint 是不可变历史。

## 每轮开始协议

Agent 在执行任何修改前必须：

1. 读取总路线 Skill；
2. 读取本 Checkpoint Skill；
3. 读取当前阶段专用 Skill；
4. 读取 `docs/plan/CURRENT.md`；
5. 打开 `CURRENT.md` 指向的最新归档 checkpoint；
6. 读取当前 Plan；
7. 核验 checkpoint 描述与真实仓库状态是否一致；
8. 若不一致，先归档一份“状态漂移 checkpoint”，再继续工作。

不得仅依据聊天中的“上次做到哪里”恢复工作。

## 每轮结束协议

在向用户发送最终回复之前，严格按以下顺序执行：

1. **捕获状态**：仓库路径、分支、HEAD、工作区、子模块、依赖、构建配置、工具链、图形 API、GPU；
2. **总结指令**：记录用户原始目标、本轮实际范围和未执行范围；
3. **记录动作**：阅读、命令、修改文件、构建、运行、捕获和测试；
4. **记录结果**：`passed`、`partial`、`blocked`、`failed` 或 `no-change`；
5. **记录证据**：日志、截图、捕获、测试输出、性能结果和对应路径；
6. **记录未提交状态**：未提交文件、生成文件、临时补丁和需要清理的内容；
7. **记录恢复入口**：下一轮应读取的 Plan、第一条命令或第一项检查；
8. 写入新的 checkpoint；
9. 追加 `CHECKPOINT_INDEX.md`；
10. 更新 `CURRENT.md`；
11. 重新打开上述文件，验证路径和状态一致；
12. 最终回复用户。

## Checkpoint 必填字段

每份 checkpoint 至少包含：

- Checkpoint ID、UTC 时间、状态；
- Previous Checkpoint、Supersedes（如适用）；
- 用户指令摘要；
- 当前路线、阶段、Plan；
- 仓库、分支、HEAD、工作区和子模块状态；
- 环境与构建配置；
- 本轮读取的源码与资料；
- 执行过的命令及其结果；
- 修改文件清单；
- 构建、运行和验证结果；
- 证据路径；
- Decision Record；
- 风险、阻塞和未解决问题；
- 当前可复现状态；
- 下一轮精确恢复入口；
- `CURRENT.md` 更新确认。

## 状态语义

| 状态 | 含义 |
|---|---|
| `passed` | 当前指令范围与验收均完成 |
| `partial` | 有有效产物，但仍有明确未完成项 |
| `blocked` | 因外部条件不能继续 |
| `failed` | 执行过但结果未达到要求 |
| `no-change` | 完成了调查或确认，但没有修改工程文件 |

状态必须如实填写。不得用 `passed` 掩盖未运行、未验证或仅静态推断的结果。

## Git 与提交边界

- Checkpoint 归档不等于自动创建 Git commit；是否提交由用户或当前 Plan 决定。
- 若本轮需要提交代码，checkpoint、`CHECKPOINT_INDEX.md` 与 `CURRENT.md` 应与对应修改一起进入提交，除非用户明确要求分离。
- 不允许为了得到“干净工作区”而擅自丢弃用户现有改动。

## 最终回复门禁格式

最终回复必须包含一个简短状态块：

```text
Checkpoint: docs/checkpoints/archive/<filename>.md
Status: passed | partial | blocked | failed | no-change
CURRENT: updated
Resume: <下一轮精确入口>
```

若 checkpoint 无法写入，则必须明确写：

```text
Checkpoint: NOT ARCHIVED
Status: checkpoint-finalization-blocked
```

此时不得声称任务完成。
