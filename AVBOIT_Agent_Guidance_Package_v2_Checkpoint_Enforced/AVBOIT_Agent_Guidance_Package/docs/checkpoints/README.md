# Checkpoint Archive

该目录保存 Agent 驱动工程的连续状态历史。

## 文件职责

```text
docs/checkpoints/
├─ README.md                 # 归档说明
├─ CHECKPOINT_INDEX.md       # 按序号追加的索引
└─ archive/                  # 不可变 checkpoint
```

- `docs/plan/CURRENT.md`：唯一的“当前状态指针”，允许更新。
- `archive/*.md`：每轮用户指令结束后的不可变状态快照，禁止覆盖。
- `CHECKPOINT_INDEX.md`：只允许追加或通过新记录纠正，不回写历史行。

完整强制协议见：

`docs/skill/checkpoint-archive-skill/SKILL.md`

## 恢复原则

新的 Agent 或新会话不能只读 `CURRENT.md`。必须同时打开它指向的最新 checkpoint，并核验真实仓库状态。若两者不一致，先归档状态漂移，再继续执行任务。
