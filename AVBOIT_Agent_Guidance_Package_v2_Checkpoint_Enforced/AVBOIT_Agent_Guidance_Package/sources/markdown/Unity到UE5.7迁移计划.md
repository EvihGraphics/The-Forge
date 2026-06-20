找到了。**最值得作为 AVBOIT 对比实验场的不是最早的 1.16，而是 The Forge Release 1.58。**

## 已确认的历史版本

The Forge 在 **Release 1.16，2018 年 9 月 21 日**首次加入 `15_Transparency` OIT 对比测试，当时明确包含：

- 普通 Alpha Blend
- McGuire Weighted Blended OIT
- Volition 版 Weighted Blended OIT
- Intel 基于 Rasterizer Ordered Views 的 Adaptive OIT

官方还说明该单元测试附带独立文档和对比，并在 DX12、Vulkan、Metal/iOS 上展示了运行结果。fileciteturn20file0L5-L23

对应历史锚点为：

```text id="7a0mpi"
Release 1.16
Merge commit:
9ec216b40968365299362b305c0fed2f97d4be1b
```

不过，**实际研发建议固定到：**

```text id="58kshm"
Release 1.58
Merge commit:
2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d
Date:
2024-06-17
```

这是我目前验证到的较新版本中，仍然完整保留 `15_Transparency` 对比试验场的版本。fileciteturn51file1L5-L10 `15_Transparency.cpp` 在该提交中确实存在。fileciteturn52file0L1-L7

我检查了随后的 Release 1.59，原来的 `15_Transparency` 路径已经找不到，因此不建议直接从当前 master 或 1.59 之后的版本开始。Release 1.59 本身发布于 2024 年 9 月。fileciteturn53file1L7-L12

## 为什么推荐 1.58

1.58 里的实验场已经不只是早期的三种 OIT。源码中可以确认它保留了：

| 对比路径 | 用途 |
|---|---|
| Sorted Alpha Blend | 正确排序参考与传统基线 |
| Weighted Blended OIT | 低成本近似基线 |
| Volition WBOIT | 面向游戏 VFX 的权重版本 |
| Phenomenological Transparency | 更完整的视觉透明模型 |
| Intel Adaptive OIT | 有界片元存储／排序方案 |
| AVBOIT | 我们计划新增的目标方案 |

源码同时保留了普通透明对象和粒子系统场景，因此以后可以从几何面片逐步过渡到大量透明 VFX，而不必立刻进入 UE 或 Niagara。fileciteturn54file0L77-L136

现有 Alpha Blend、WBOIT 和 Volition 参数也集中在同一套测试框架里。fileciteturn54file0L192-L231 Phenomenological Transparency 与 AOIT 也已经作为独立渲染路径存在。fileciteturn54file0L233-L244 fileciteturn54file0L258-L284

## 一个重要的名称区别

The Forge 里的：

```text id="uo0yrm"
Adaptive OIT / AOIT
```

指的是 Intel 的、依赖 Rasterizer Ordered Views 的 Adaptive OIT。

我们要实现的是：

```text id="tda0i4"
Adaptive Voxel-Based OIT / AVBOIT
```

两者不是同一算法。

因此正确做法不是用 AVBOIT 覆盖原来的 AOIT，而是把它作为新的第六种透明后端：

```text id="q4nvqb"
同一场景与透明数据
        ↓
┌──────────────────────────────┐
│ Sorted Alpha                 │
│ WBOIT                        │
│ Volition WBOIT               │
│ Phenomenological Transparency│
│ Intel AOIT                   │
│ Activision AVBOIT            │
└──────────────────────────────┘
        ↓
统一截图、误差和性能比较
```

## 建议的抽象实验架构

整个对比工程只需要保持四个稳定层次：

```text id="2wy9wh"
统一测试内容
RGB 面片 / 交叉卡片 / 序列帧沙暴片
        ↓
统一透明输入
几何、颜色、Alpha、深度
        ↓
可切换透明后端
现有算法 + AVBOIT
        ↓
统一评估
图像、稳定性、GPU 时间、显存
```

这样比较才公平：所有算法使用同一相机、同一批透明对象、同一纹理、同一光照和同一提交顺序。

## 推荐推进顺序

### 阶段 A：恢复原始试验场

先确保 Release 1.58 的现有五种透明模式都能够正常切换和运行。此时不修改场景，也不加入 AVBOIT。

### 阶段 B：加入 AVBOIT 基础路径

使用三张红绿蓝透明面片：

- 固定物理深度关系；
- 随机改变提交顺序；
- 与 Sorted Alpha 参考结果比较。

Sorted Alpha 应作为图像正确性的 Ground Truth，而不是 WBOIT。

### 阶段 C：序列帧沙暴卡片

把测试内容替换为多张重叠沙暴序列帧卡片，比较：

- 前后层次保持能力；
- 大面积低 Alpha 积累；
- 提交顺序变化时的闪烁；
- 相机运动时的稳定性；
- 高深度复杂度下的性能变化。

### 阶段 D：再迁移到 UE

在 The Forge 中验证的是：

```text id="lup3d6"
AVBOIT 算法是否正确
与其他 OIT 相比是否值得
参数和资源预算如何选择
```

UE 插件阶段只负责回答：

```text id="yayepk"
如何把已验证算法接进 UE
```

这样就能把“算法错误”和“UE 渲染管线接入错误”彻底分开。

## 最终建议

将两个版本都保存为参考：

```text id="3fescm"
The Forge 1.16
用于研究最原始、最简洁的 OIT 对比实现

The Forge 1.58
作为实际新增 AVBOIT 的开发基线
```

**主开发基线选 1.58，提交固定为 `2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d`，不要跟随 master。** 这条路线比直接在 UE 插件里一边实现算法、一边排查引擎耦合问题稳得多。