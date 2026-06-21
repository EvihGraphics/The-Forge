# CHECKPOINT-0002：状态漂移核验与 AVBOIT 学习导?

## Metadata
- **Checkpoint ID**：CHECKPOINT-0002
- **UTC Time**：2026-06-20T15:15:00Z
- **Status**：partial
- **Previous Checkpoint**：CHECKPOINT-0001
- **Supersedes**：
one

## 用户指令摘要
用户要求拉取最新版获取指导包，从“源码基线恢复”阶段切换到 AVBOIT 实现与验证阶段。要求先核验最新 Checkpoint 与仓库状态一致性（目标 HEAD = 2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d，且 15_Transparency 成功构建运行）。要求给出首次学习导航并输出归档。由于 HEAD 发生漂移，在此生成状态漂移 Checkpoint，不直接修改算法。

## 当前路线与计?
- 总路线：docs/skill/avboit-learning-development-skill-v1/SKILL.md
- 当前专用 Skill：docs/skill/theforge-avboit-lab-skill/SKILL.md
- 当前阶段：The Forge 中新增 AVBOIT

## 工程状?
- The Forge 目标版本：Release 1.58
- 目标 commit：2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d
- 当前实际 The Forge HEAD：c2b643ae770aa3bc7fc8fd5e4a06d5e3fed6eafc （由于新增了 baseline report 与 skill pack，发生了漂移，源码部分仍为 1.58）
- 15_Transparency 状态：上轮已确认可成功构建并在 5 种模式下正常运行（本地截取了 Mode 0-4 的基线结果）。

## 本轮实施与验?
- 成功拉取最新指导包（包含 ROADMAP 与 PROMPT）；
- 验证出 HEAD 状态漂移并执行了状态漂移记录机制；
- 输出了首次学习导航（本质差别、代码区域、最小闭环、正确性验证、复述目标）。

## 证据路径
- Git 状态证据：c2b643ae770aa3bc7fc8fd5e4a06d5e3fed6eafc 包含 update skill pack 的日志。
- 本地构建与运行证据：LocalVisualResults/HIVE_4090x2/ 内的构建日志与 18 张 Screenshots。

## 风险与未解决问题
- HEAD 与强制约定的 2f47c14 不一致，原因是引入了指导文档的 commit，并未修改 The Forge 渲染源码，此漂移属于良性。但严格遵循规范，先记录状态漂移。
- 尚未编写 RGB 三面片 Ground Truth 代码。

## 下一轮精确恢复入?
1. 读取 15_Transparency.cpp 与已有后端的 FSL Shader；
2. 阅读 AVBOIT 的 PDF 与 Egaku 源码，建立算法契约；
3. 构建 RGB 三面片并完成 6 种 draw call 顺序的数学 Ground Truth 设计；
4. 构建并归档 CHECKPOINT-0003。
