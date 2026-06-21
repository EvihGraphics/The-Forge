# Project Charter

## 当前主目标

在 The Forge 1.58 的透明算法对比试验场中实现和验证 Activision AVBOIT，并以序列帧沙暴卡片验证其项目价值。

## 长期目标

把验证后的算法迁移为 UE 插件：先独立 Flipbook Sandstorm Player，再接入 Niagara。

## 状态连续性强约束

每次用户指令结束后，Agent 必须在回复前归档一份不可变 checkpoint，并同步更新 `CHECKPOINT_INDEX.md` 与 `CURRENT.md`。该要求适用于成功、部分完成、阻塞、失败和无改动回合。

## 非目标

- 当前不实现完整天气系统；
- 当前不实现流体、VDB 或体积 Ray March；
- 当前不修改 UE；
- 当前不对接 Niagara；
- 不复制 SingleVolume 源码；
- 不把 The Forge AOIT 当成 AVBOIT。
