# UE AVBOIT Migration Skill（Deferred）

## 状态

当前禁用。只有 `PLAN-8-0.md` 的 The Forge 算法冻结契约通过后才能启用。

## 目标

把已经在 The Forge 中验证的算法契约迁移为 UE 插件，而不是在 UE 中重新发明或重新调参 AVBOIT。

## 边界

- 第一产品目标：独立的 AVBOIT 序列帧沙暴卡片播放器；
- Niagara 只是未来实例数据来源；
- 优先插件扩展点，必要时才评估更深层 Renderer 集成；
- 不把 AVBOIT 写入 GBuffer；
- 不以 SingleVolume 源码作为实现参考；其 PDF 仅提供宏观插件工程经验；
- 具体 UE 接口和目录由迁移时的真实引擎版本决定。

## Checkpoint 继承规则

启用本阶段后，每条用户指令仍必须执行 `checkpoint-archive-skill`。Checkpoint 还必须额外记录 UE 精确版本、源码/Launcher 构建、目标平台、Renderer 配置、插件加载状态、Shader 编译状态以及是否存在 Engine Patch。
