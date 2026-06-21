# The Forge AVBOIT Lab Skill

## 角色

这是 The Forge 阶段的专用 Skill。目标是在既有 `15_Transparency` 对比实验场中学习透明算法工程，并新增独立 AVBOIT 后端。

## 稳定抽象

```text
统一测试内容
RGB 面片 / 交叉卡片 / 序列帧沙暴片
        ↓
统一透明输入
几何 / 颜色 / Alpha / 深度
        ↓
可切换透明后端
Sorted Alpha / WBOIT / Volition WBOIT /
Phenomenological / Intel AOIT / Activision AVBOIT
        ↓
统一评估
图像 / 顺序稳定性 / GPU 时间 / 显存
```

## 专用开发原则

- 先恢复原实验场，再新增后端。
- 所有算法必须共享相机、内容、纹理、光照和提交序列。
- 非交叉 RGB 面片阶段，Sorted Alpha 可作为 Ground Truth。
- 交叉几何阶段不能盲目把对象级 Sorted Alpha 当作逐像素真值。
- WBOIT 是近似基线，不是正确性真值。
- 每增加一个 AVBOIT 阶段，都必须提供可视化或捕获证据。
- 性能比较必须在相同分辨率、场景与采样条件下进行。

## Agent 的自主空间

Agent 可根据 Release 1.58 实际源码决定：

- AVBOIT 如何接入现有透明后端选择机制；
- 资源创建、同步和 Shader 组织方式；
- 如何复用或隔离现有场景数据；
- 如何构建调试视图和性能标记；
- 如何在目标 API 上实现必要能力。

这些决策必须写入 Decision Record，并说明替代方案与选择理由。

## 阶段退出条件

进入 UE 前必须形成：

- 算法阶段契约；
- Alpha／消光／透射率约定；
- 深度映射约定；
- 质量档位；
- 显存和 GPU 时间预算；
- RGB、交叉卡片和沙暴卡片结果；
- 已知误差与限制；
- 与具体图形 API 解耦的迁移说明。

## Checkpoint 继承规则

本阶段无条件继承 `checkpoint-archive-skill`：每次用户指令结束后，无论是否修改渲染代码、是否构建成功，都必须归档当前仓库与实验状态。任何性能数字、截图或捕获若未写入对应 checkpoint，不得作为已冻结结论。
