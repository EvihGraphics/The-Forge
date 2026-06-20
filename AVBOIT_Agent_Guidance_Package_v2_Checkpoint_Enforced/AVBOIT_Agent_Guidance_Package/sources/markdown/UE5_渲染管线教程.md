我对照了当前文档库，排除了已经上传的《在 UE5 外部模块中扩展复杂渲染管线实践》及其中的 Scene Proxy、Mesh Draw Pipeline、RDG、插件部署内容，也没有重复 Unreal Fest、GDC、SIGGRAPH、Inside Unreal 汇总里的课程；已有的天气与体渲染案例报告同样没有再次列入。fileciteturn1file0 fileciteturn1file2 fileciteturn1file4 fileciteturn1file10 fileciteturn0file0

筛选后的结论是：**目前公开资料中，几乎没有一套视频能从 `UPrimitiveComponent` 一直讲到 RDG、Shader、Mesh Pass 和 RHI。最系统的方案是“一套整帧总览 + 一套七篇源码实践 + 两个专项实验”。**

## 最值得学习的教程

| 优先级 | 教程 | 形式与版本 | 主要价值 |
|---|---|---|---|
| **S** | **UE5 レンダリングフロー総おさらい（2024）基礎編** | Epic Games Japan，日文超长讲义，基于 UE 5.5 | 当前最完整的 **UE5 整帧渲染流程总览** |
| **S** | **Advanced Graphics Programming in Unreal** | 英文七篇博客 + GitHub，UE 5.3–5.5 | 当前最系统的 **自定义 UE 渲染编程课程** |
| **A** | **UnrealEngine レンダリングシステムとその拡張** | 日文讲义，UE5 | 建立 Game Thread、Render Thread、Scene、View、RDG 的架构关系 |
| **A** | **SceneViewExtension によるレンダリング改造の紹介** | 日文视频 + 讲义 + 示例源码 | 真正动手把自定义 Pass 插进 UE 管线 |
| **A** | **单一 Static Mesh Renderer／自定义 Mesh Pass 系列** | 日文博客，UE 5.3 | 深入 Shader、Vertex Factory、MeshBatch、MeshPassProcessor |
| **B** | **Rendering Pipeline UE5** | 英文博客，2025 | 一张图掌握实际 GPU Pass 顺序，适合作为源码导航图 |

---

## 1. UE5 整帧渲染流程总览

### UE5 レンダリングフロー総おさらい（2024）基礎編

这是我最推荐你首先看的资料。它不是只介绍 Nanite 或 Lumen，而是按照一帧的实际顺序讲解：

```text id="506lrq"
CPU：InitViews / 可见性筛选
              ↓
GPU：PrePass
              ↓
BasePass → GBuffer
              ↓
Direct Lighting / Indirect Lighting / Lumen
              ↓
Translucency
              ↓
Post Process
              ↓
TSR / Upscale
```

讲义还覆盖：

- Deferred、Forward、Path Tracing 的职责区别
- Frustum Culling 与 Occlusion Culling
- Draw Call 与 Auto Instancing
- 普通 Mesh 和 Nanite 如何汇入同一个 GBuffer
- Material、Shading Model 与 Shader Compilation
- 直接光、阴影、VSM
- Lumen Scene、Screen Trace、时域更新
- 半透明、后处理和放大

它明确把 `InitViews → BasePass → Lighting → Translucency → PostProcess/Upscale` 作为主干，并解释 Nanite 的 Visibility Buffer 最终如何写入并合并到 GBuffer。([docswell.com](https://www.docswell.com/s/EpicGamesJapan/5QRL3V-ue5-renderingflow-2024-basic))

**定位：**整帧地图。  
**不足：**偏原理和功能层，不会逐函数追踪 `FDeferredShadingSceneRenderer`。

---

## 2. 最系统的 UE5 渲染编程系列

### Advanced Graphics Programming in Unreal

这套七篇系列比大多数零散的 SceneViewExtension 教程系统得多，而且附带插件与演示工程。作者以一个包含初始化、Mesh Pass、Compute Pass、显示 Pass 的 Game of Life 效果贯穿整套课程。([medium.com](https://medium.com/%40manning.w27/advanced-graphics-programming-in-unreal-part-1-10488f2e17dd))

七篇顺序如下：

| 篇章 | 内容 | 对你的价值 |
|---|---|---|
| Part 1 | 工程、插件、Shader 目录和 RenderDoc 调试环境 | 建立源码实验工程 |
| Part 2 | **RHI、RDG、渲染线程、代理对象** | 理解 UE 图形抽象层 |
| Part 3 | **Scene、View、ViewFamily、SceneViewExtension** | 理解管线入口和 View 数据 |
| Part 4 | Global Shader | 编写全屏／Compute Pass |
| Part 5 | 简单 Material Shader | 接入材质编译结果 |
| Part 6 | 高级 Material Shader | 扩展材质表达与 Shader 数据 |
| Part 7 | **Mesh-Material Shader 与 Mesh Pass** | 自定义几何绘制管线 |

Part 2 对渲染线程、RHI Thread、`ENQUEUE_RENDER_COMMAND`、Game/Render Thread 数据代理、RHI 与 RDG 的层级关系讲得很清楚。([medium.com](https://medium.com/%40manning.w27/advanced-graphics-programming-in-unreal-part-2-abf8237491c1))

Part 3 则把核心对象组织为：

```text id="bztsc4"
FScene
  └─ FSceneRenderer
       └─ FSceneViewFamily
            └─ FSceneView / FViewInfo
```

并实际使用 SceneViewExtension 获取 Scene Texture、GBuffer 和 View Uniform Buffer，向 RDG 注册 Pass。([medium.com](https://medium.com/%40manning.w27/advanced-graphics-programming-in-unreal-part-3-f37f4d4407d7))

后四篇进一步进入 Global Shader、Material Shader、Mesh-Material Shader 和自定义 Mesh Pass。([medium.com](https://medium.com/%40manning.w27/advanced-graphics-programming-in-unreal-part-4-c89d6fb98b59))

**定位：**主课程。  
**与你的 OIT 目标最相关：**Part 2、3、4、7。  
**版本注意：**作者针对 UE 5.3–5.5，较新版本可能出现函数签名或私有头文件位置变化，但架构主线仍有价值。

---

## 3. UE 渲染架构的中间桥梁

### UnrealEngine レンダリングシステムとその拡張

这份资料适合放在整帧总览和源码实践之间。它重点解释了 UE 为什么要在 Render Thread 建立一个 Game Thread 世界的“渲染镜像”：

| Game Thread | Render Thread |
|---|---|
| `UWorld` | `FScene` |
| `UPrimitiveComponent` | `FPrimitiveSceneProxy` |
| Actor／Component 状态 | `FPrimitiveSceneInfo` |
| 玩家和相机 | `FSceneView` / `FViewInfo` |
|  | `FSceneRenderer` |

资料还介绍了 RDG 位于 RHI 上层，负责资源生命周期、Pass 调度、并行记录、依赖和调试，并给出了从 Blueprint 调用到 Render Thread、创建 `FRDGBuilder`、注册清屏 Pass、执行 Graph 的完整小案例。([docswell.com](https://www.docswell.com/s/strvert/K38NEM-rendering-system-and-extensions-in-unrealengine))

**定位：**架构图和术语手册。  
**优势：**比直接打开 `DeferredShadingRenderer.cpp` 更容易建立对象关系。

---

## 4. SceneViewExtension 实战课程

### SceneViewExtension によるレンダリング改造の紹介

这一课提供了：

- 讲义
- 视频录像
- GitHub 示例工程
- RDG Compute Shader
- SceneColor、Depth、GBuffer 读取
- 中间纹理创建
- 跨帧 History Texture
- 自定义 Pass 合成
- 修改 GBuffer 数据的实验

讲义从 `BasePass → Lighting → Translucency → PostProcess` 的基本流程出发，展示如何通过 SceneViewExtension 在不同位置插入 `CustomProcess`，以及如何把若干 Compute Pass 组织为一条 RDG 子管线。([docswell.com](https://www.docswell.com/s/leon-gameworks/ZL1JL3-2024-10-20-225343))

完整活动录像中，这一节大约从 **2:08:01** 开始；公开页面同时给出了讲义和录像入口。([youtube.com](https://www.youtube.com/watch?v=Z6OSqWo2UxI&utm_source=chatgpt.com))

示例源码也已公开，包含 `ViewExtensionSample`。([aniz.tistory.com](https://aniz.tistory.com/411))

**推荐实验：**

```text id="s9ryra"
SceneColor
   ↓
高亮提取 Pass
   ↓
模糊 Pass
   ↓
合成 Pass
   ↓
写回 SceneColor
```

完成后，把高亮提取替换成透明片元数据采集或透射率缓冲，就能开始接近 OIT 原型。

---

## 5. 自定义 Mesh Pass 深入教程

### 单一 Static Mesh Renderer／自定义 Mesh Pass 系列

这篇的标题看起来只是“渲染一张 Static Mesh”，实际上前置知识部分非常完整，覆盖：

- `FGlobalShader`
- `FMaterialShader`
- `FMeshMaterialShader`
- Shader Permutation
- `FVertexFactory`
- `FRDGBuilder`
- RDG Texture、Buffer、SRV、UAV
- `FPrimitiveSceneProxy`
- `FMeshBatch`
- `FMeshPassProcessor`
- `FMaterialRenderProxy`
- `FMaterialResource`

([strv.dev](https://strv.dev/blog/unrealengine--lets-implement-a-single-mesh-renderer-2/))

其中最有价值的是把 Mesh Pass 数据流连接了起来：

```text id="0jt14h"
PrimitiveSceneProxy
        ↓
     FMeshBatch
        ↓
 FMeshPassProcessor
        ↓
 BuildMeshDrawCommands
        ↓
  FMeshDrawCommand
        ↓
        RHI
```

相比你库里的 Single Volume 讲义，这个系列会从更基础的 Shader 类型、Vertex Factory 和材质编译关系开始解释，因此可以作为互补，而不是重复。

---

## 6. 一张图看懂 UE5 GPU Pass

### Rendering Pipeline UE5 — Taras Tereshchenko

这是一篇较短的 2025 年博客，核心价值是提供一张基于 UE5 RenderDoc／RDG 观察整理的整帧流程图，包含：

- PrePass
- Nanite VisBuffer 与 Depth Merge
- Lumen Scene Update
- BasePass
- Diffuse Indirect 与 AO
- Shadow Depth / VSM
- Deferred Lighting
- Single Layer Water
- Sky Atmosphere / Fog / Volumetric Cloud
- 多阶段 Translucency
- Post Process

([teres4enko.blogspot.com](https://teres4enko.blogspot.com/2025/03/rendering-pipeline-ue5.html))

**定位：**挂在旁边随时对照的“地图”。  
**不适合作为主课程：**它告诉你 Pass 的顺序，但不深入解释 CPU 如何生成这些 Pass。

---

# 针对你目标的学习顺序

## 阶段一：先认识一帧

1. 阅读 **UE5 Rendering Flow 2024**
2. 对照 **Rendering Pipeline UE5** 总图
3. 在一个简单场景里执行 `ProfileGPU`
4. 把实际 Pass 按下面结构重新画一遍：

```text id="nu5d3w"
Visibility
├─ PrePass
├─ Nanite
└─ InitViews / Culling

Opaque
├─ BasePass
├─ GBuffer
├─ Lighting
└─ Shadows

Environment
├─ Lumen
├─ Atmosphere
├─ Fog
└─ Clouds

Transparency
├─ Before DOF
├─ After DOF
└─ Distortion

Output
├─ Post Process
└─ TSR
```

## 阶段二：理解 CPU 如何生成 GPU 工作

阅读：

- Rendering System and Extensions
- Advanced Graphics Programming Part 2–3

需要能够解释这条链：

```text id="09afew"
Game Thread
UPrimitiveComponent
        │ CreateSceneProxy
        ▼
FPrimitiveSceneProxy
        │
Render Thread
        ▼
FScene / FPrimitiveSceneInfo
        │
InitViews / Visibility
        ▼
FMeshBatch
        │
FMeshPassProcessor
        ▼
FMeshDrawCommand
        │
RDG / RHI
        ▼
GPU
```

## 阶段三：先插入一个全屏 Pass

学习：

- Advanced Graphics Programming Part 4
- SceneViewExtension 实战

验收目标：

- 插件中注册 SceneViewExtension
- 从正确的渲染回调取得 `FRDGBuilder`
- 读取 SceneColor 或 SceneDepth
- 创建 RDG 中间纹理
- Dispatch Compute Shader
- 合成回 SceneColor
- 用 RDG Insights 检查资源生命周期

## 阶段四：进入 Mesh Pass

学习：

- Advanced Graphics Programming Part 5–7
- 自定义 Static Mesh Renderer 系列

验收目标：

- 自定义 `FMeshMaterialShader`
- 编写 `FMeshPassProcessor`
- 从 `FMeshBatch` 生成 `FMeshDrawCommand`
- 使用材质和 Vertex Factory
- 把特定透明 Mesh 绘制到自定义 MRT／UAV

## 阶段五：针对 AVBOIT

你的 AVBOIT 可以拆成三个可测试边界：

```text id="7xh7bg"
透明几何收集
    │
    ▼
Voxel / Transmittance 数据构建
    │
    ▼
透明着色与 Resolve
    │
    ▼
SceneColor
```

对应教程重点：

| AVBOIT 模块 | 重点学习内容 |
|---|---|
| 透明对象进入自定义管线 | Mesh Pass、`FMeshPassProcessor`、材质 Shader |
| Voxel／透射率缓冲 | RDG Buffer、UAV、Compute Shader |
| Resolve 与合成 | SceneViewExtension、SceneColor、全屏 Pass |
| 游戏线程参数下发 | Proxy、Render Command、Render Thread 数据副本 |
| 与 UE 原生透明管线整合 | `FDeferredShadingSceneRenderer` 和 Translucency 源码 |

需要特别注意：**SceneViewExtension 很适合原型、附加 Pass 和 Resolve，但它不一定能完整替换 UE 原生透明对象的收集、分类和绘制流程。** 要让所有透明材质进入新的 AVBOIT Mesh Pass，最终大概率仍需要 Renderer 源码改造，或者至少使用较深的私有 Renderer 接口。这一点要根据你使用的具体 UE 版本实测，而不能只凭插件教程判断。([medium.com](https://medium.com/%40manning.w27/advanced-graphics-programming-in-unreal-part-3-f37f4d4407d7))

## 不建议作为主线的旧教程

很多 UE4 教程仍围绕旧的 `DrawingPolicy` 和 RDG 之前的立即式调用展开。UE 后续引入了以 `FMeshDrawCommand`、`FMeshPassProcessor` 和缓存为核心的 Mesh Drawing Pipeline，场景 Pass 也已迁移到 RDG，因此旧资料更适合了解历史，不适合直接照着实现 UE5 管线。([dev.epicgames.com](https://dev.epicgames.com/documentation/unreal-engine/mesh-drawing-pipeline-in-unreal-engine?utm_source=chatgpt.com))

**最终推荐主线：**

```text id="18od23"
UE5 Rendering Flow 2024
        ↓
Advanced Graphics Programming Part 1–3
        ↓
SceneViewExtension 实战
        ↓
Advanced Graphics Programming Part 4–7
        ↓
自定义 Mesh Renderer
        ↓
AVBOIT 三阶段原型
        ↓
UE Translucency 源码整合
```

这套组合比单独看某一场 Unreal Fest 演讲更系统，也正好补上你当前文档库里“已经展示了实现结果，但缺少从整帧架构到各抽象层循序建立认知”的部分。