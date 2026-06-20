# SIGGRAPH Advances in Real-Time Rendering in Games 2023—2026 课程总结

> 资料范围：SIGGRAPH **Advances in Real-Time Rendering in Games** 年度课程，而不是 SIGGRAPH 全部 Technical Papers、Talks 或其他 Course。  
> 年份为最高层级；每年按照技术主题拆成若干表格。表格沿用 Unreal Fest Bali 版格式：**序号｜课程｜主要内容｜课题关联度**。  
> “课题关联度”针对当前研究方向：**UE 渲染管线、环境 VFX、体积天气、沙暴／雪崩、透明合成、GPU Compute、性能和插件扩展**。  
> 关联度含义：**高**＝可直接进入当前方案；**中高**＝可迁移关键模块；**中**＝提供重要底层背景；**低**＝关联较间接。

## 年度官方页面

- 2023：<https://advances.realtimerendering.com/s2023/index.html>
- 2024：<https://advances.realtimerendering.com/s2024/index.html>
- 2025：<https://advances.realtimerendering.com/s2025/>
- 2026：截至 2026-06-17，SIGGRAPH 2026 已确认继续举办 Part 1 与 Part 2，但详细课程题目和讲义尚未在 Advances 年度页面公开。

---

# 2023

2023 年的主线是：**移动端渲染架构、可进入体积的体素云、超大地形虚拟化、统一分层材质，以及主机级角色与混合光追**。课程数量不多，但每门都提供了相对完整的生产方案。

## 一、渲染架构、体积与大尺度环境

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**HypeHype Mobile Rendering Architecture**](https://advances.realtimerendering.com/s2023/AaltonenHypeHypeAdvances2023.pdf) | HypeHype 从零设计面向 Vulkan、Metal 和 WebGPU 的移动渲染器。课程讨论图形 API 抽象、资源描述、渲染任务组织、面向性能的数据结构、低 CPU 开销以及移动端功耗约束。其价值不在某个单独 Shader，而在于展示如何围绕跨平台、可维护性和低端硬件重新设计一整套渲染架构。 | **中高**：适合参考自定义 UE 渲染模块的资源生命周期、Pass 组织与多平台边界。 |
| 2 | [**Nubis³: Methods (and Madness) to Model and Render Immersive Real-Time Voxel-Based Clouds**](https://advances.realtimerendering.com/s2023/Nubis%20Cubed%20%28Advances%202023%29.pdf) | Guerrilla 将过去的 2.5D 云层方案推进为可近距离进入和穿越的体素云。核心包括压缩 SDF 辅助跳空、基于流体思想的云体建模、低带宽稠密体素上采样、光照采样加速，以及暗边、内发光等云特定近似。它同时服务地面天空盒、动态时间和空中穿云玩法。 | **高**：是沙暴墙、粉雪 plume 和局部异构体积最直接的 shipping 级参照。 |
| 3 | [**Large-Scale Terrain Rendering in Call of Duty**](https://advances.realtimerendering.com/s2023/Etienne%28ATVI%29-Large%20Scale%20Terrain%20Rendering%20with%20notes%20%28Advances%202023%29.pdf) | 讲解《Call of Duty》的大尺度地形制作与渲染：One Material Per Vertex、Adaptive Virtual Texture、Virtual Height Map、GPU Feedback、运行时压缩、地形与 Mesh 融合、雪与冰材质附加通道，以及动态脚印、履带和大地图事件对虚拟页的局部更新。方案覆盖移动端到高端 PC。 | **高**：与沙地／雪地材质、积累、足迹和局部破坏反馈直接相关。 |

## 二、材质系统、角色与混合光追

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Authoring Materials That Matter — Substrate in Unreal Engine 5**](https://advances.realtimerendering.com/s2023/2023%20Siggraph%20-%20Substrate.pdf) | Epic 介绍 Substrate 的设计目标：以 Slab 作为统一物质构件，通过图结构完成 BSDF 混合与分层；运行时对材质拓扑进行量化和打包，并通过转换规则在电影级路径追踪、主机高帧率和移动端之间重定向。重点是让材质复杂度由固定 Shading Model 转向可组合的物质表达。 | **高**：可用于积雪、湿雪、沙尘覆盖、冰层和地表状态混合。 |
| 2 | [**The Rendering of The Callisto Protocol**](https://advances.realtimerendering.com/s2023/SIGGRAPH2023-Advances-The-Rendering-of-The-Callisto-Protocol-JimenezPetersen.pdf) | 围绕照片级角色和主机光追展开：数字替身与照片参考校准、BRDF 作者工具、Realis 外观匹配，以及全灯光／多表面的光追阴影、反射和透射。课程还讨论部分预计算可见性、时空与感知驱动的可变速率光追、Tile 分类、透明表面反射、体积整合、异步追踪和寄存器压力控制。 | **中高**：对透明体、体积与 RT 光照的统一，以及“按感知分配射线预算”很有价值。 |

## 2023 年结论

| 方向 | 最值得吸收的方案 |
|---|---|
| 局部体积密度与穿越效果 | **Nubis³：体素密度场 + 跳空／压缩采样 + 上采样** |
| 地表积雪／沙地反馈 | **Call of Duty Terrain：虚拟纹理页局部更新 + 动态 Decal** |
| 雪、冰、湿润和覆盖材质 | **Substrate：Slab 分层与跨平台材质重定向** |
| 自定义渲染架构 | **HypeHype：面向低开销和跨平台重构渲染器** |
| RT 与透明／体积协同 | **The Callisto Protocol：混合光追的分级与调度** |

---

# 2024

2024 年的主线是：**机器学习改造预计算光照、移动端高密度几何、Shader 工程化、Visibility Buffer/VRS、动态 GI、半球光照编码和 GPU 自适应细分**。这一年明显从“单项效果”转向“渲染基础设施”。

## 一、全局光照、机器学习与光照表示

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Neural Light Grid: Modernizing Irradiance Volumes with Machine Learning**](https://advances.realtimerendering.com/s2024/index.html#neural_light_grid) | Activision 回顾多次机器学习实验，最终用轻量神经网络修正 Irradiance Volume 的漏光、接缝和低频表达不足。方案强调在低端移动 GPU 上运行、保持传统 Probe 方案的固定成本，并支持跨平台共享内容，而不是依赖高端专用推理硬件。 | **高**：适合给大范围雾、沙尘和雪暴提供低成本、跨平台的间接光缓存。 |
| 2 | [**Shipping Dynamic Global Illumination in Frostbite**](https://advances.realtimerendering.com/s2024/content/EA-GIBS2/Apers_Advances-s2024_Shipping-Dynamic-GI.pdf) | Frostbite 对 2021 年 GIBS Surfel GI 的生产化复盘。内容包括动态 Surfel 生成与缓存、半分辨率计算、标量化加载、空间更新和在《Skate》《College Football 25》等实际项目中的作者效率、质量与 60 FPS 约束。 | **高**：可参考局部动态天气体积如何共享世界级辐照缓存。 |
| 3 | [**Hemispherical Lighting Insights from the Call of Duty Production Lessons**](https://advances.realtimerendering.com/s2024/content/Roughton/SIGGRAPH%20Advances%202024%20-%20Hemispheres%20Presentation%20Notes.pdf) | 研究半球光照和可见性编码：AHD、IrradZ、半球／圆锥遮蔽与体积球谐光照的组合，目标是在低运行时成本下改善 AO、减少漏光，并让预计算光照更好地响应局部遮蔽。 | **中高**：对体积雾、粒子云和局部遮蔽方向性编码有方法论价值。 |

## 二、GPU 驱动几何、Visibility Buffer 与可扩展渲染

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Seamless Rendering on Mobile: The Magic of Adaptive LOD Pipeline**](https://advances.realtimerendering.com/s2024/content/Cao-NanoMesh/AdavanceRealtimeRendering_NanoMesh0810.pdf) | 腾讯提出面向移动端的 Cluster 渲染管线：离线构建多层 Cluster、GPU HZB/视锥/背面剔除、动态 Streaming、32-bit Visibility Buffer、按材质 Tile 分类，以及无 Bindless 条件下的材质重放。还结合分层体素 Brick GI 和低精度 Shadow Geometry，在移动设备展示高三角形规模。 | **高**：适合研究沙暴／雪崩大场景中“高端统一资产、低端自动回退”的组织方式。 |
| 2 | [**Variable Rate Shading with Visibility Buffer Rendering**](https://advances.realtimerendering.com/s2024/index.html#hable) | John Hable 从 Quad 利用率、小三角形成本和 Primitive ID 编码出发，构建 Visibility Buffer，并将几何采样率与着色采样率解耦。课程包含 Leading Vertex、Mesh Pool、导数重建、边界检测、稀疏像素选择、重建和固定内存 OIT 的实验。 | **高**：对自定义体积／透明 Pass 的低分辨率计算、边缘重建和固定预算设计很有价值。 |
| 3 | [**Achieving Scalable Performance for Large-Scale Components with CBTs**](https://advances.realtimerendering.com/s2024/content/Intel/large_scale_cbt_slides_siggraph_advances_2024.pdf) | Intel 将 Concurrent Binary Tree 从方形地形扩展到任意多边形网格，以 Half-edge Bisector 表达 GPU 自适应细分，并把 CBT 作为并发内存池，支持行星尺度几何和更深的细分层级。核心是 GPU 端增删细分单元、裂缝一致性与固定数据结构开销。 | **中高**：可用于大尺度雪面、沙丘或动态表面细分，但与体积主路径相对间接。 |

## 三、Shader 工程与开放生产数据

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Flexible and Extensible Shader Authoring in Frostbite with Serac**](https://advances.realtimerendering.com/s2024/index.html#serac) | Frostbite 为解决 HLSL 在性能、复用和可扩展性之间的矛盾，构建了 Serac 这一 HLSL 领域专用包装层。课程讨论语言能力、编译与代码生成、引擎集成、Shader 作者工作流，以及在多个项目部署后暴露出的维护经验。 | **高**：对 UE 自定义 Shader、公共介质函数库和跨多个 Pass 的一致参数体系有直接参考。 |
| 2 | [**Announcing the Call of Duty Open-Source USD Caldera Data Set**](https://advances.realtimerendering.com/s2024/index.html#caldera) | Activision 发布来自《Warzone Caldera》的生产级 OpenUSD 场景数据，面向学术研究和非商业实验。其价值在于提供高复杂度环境几何、材质和真实生产分布，可用于测试剔除、Streaming、GI、可见性和几何表示算法。 | **中高**：适合为自定义渲染器、体积遮挡和性能测试建立真实压力场景。 |

## 2024 年结论

| 方向 | 最值得吸收的方案 |
|---|---|
| 低成本世界光照 | **Neural Light Grid + Hemispherical Lighting** |
| 动态大世界 GI | **Frostbite GIBS：Surfel 缓存与动态更新** |
| 跨平台高密度场景 | **Seamless Mobile Rendering：Cluster + VisBuffer + Streaming** |
| 自定义 Pass 降采样 | **Visibility Buffer/VRS：计算分辨率与最终像素解耦** |
| Shader 体系维护 | **Serac：统一介质函数、编译和多 Pass 作者接口** |
| 大尺度表面几何 | **CBT：GPU 自适应细分和固定结构预算** |

---

# 2025

2025 年的主线是：**透明合成、大世界光追 GI、全 Strand 头发、实时 GI 取代 Bake、移动到 PC 的固定成本随机光照、实时 SSS，以及 UE MegaLights**。这一年最鲜明的趋势是把固定预算的随机采样、时空重用和统一管线推向 shipping 级应用。

## 一、透明、半透明与高密度表示

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Adaptive Voxel-Based Order-Independent Transparency**](https://advances.realtimerendering.com/s2025/content/AVBOIT_SIG2025_MDROBOT-final.pdf) | Activision 回顾《Call of Duty》从手工排序、A-Buffer、Weighted OIT、Moment/Wavelet OIT 到 AVBOIT 的演进。新方案先在较低分辨率估计沿深度的透射率函数，再用自适应体素层表达关键遮挡，之后以任意绘制顺序完成全分辨率透明合成；重点满足烟雾遮挡的 Gameplay 正确性、彩色玻璃、远距离稳定性、固定内存和多分辨率。 | **高**：直接解决沙尘、雪粉、烟雾和透明卡片的排序、闪烁与遮挡稳定性。 |
| 2 | [**Strand-Based Hair and Fur Rendering in Indiana Jones and the Great Circle**](https://advances.realtimerendering.com/s2025/content/Strand%20Hair%20in%20IJGC%20-%20Final%20Slides%20%28Post-Conference%29.pdf) | MachineGames 以 Strand 作为全部人类头发的唯一表示，并在 60 Hz 目标下优化。内容涉及 Strand 数据与 LOD、预计算可见性、低阶 SH、自遮挡、体积化头发阴影、代理 Shadow Mesh、透明排序、Motion Vector 和复杂场景中的多透明层组合。 | **中高**：虽然对象是头发，但体积阴影、稀疏可见性与透明排序可迁移到细粒雪、沙和纤维状介质。 |

## 二、大世界光追与实时全局光照

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Ray Tracing the World of Assassin’s Creed Shadows**](https://advances.realtimerendering.com/s2025/content/Advances%202025%20-%20Raytracing%20the%20world%20of%20Assassin%27s%20Creed%20Shadows.pdf) | Ubisoft 讲解 Anvil 在大尺度动态开放世界中的 RTGI：按像素追踪、Probe Volume 二次命中缓存、季节和植被状态、半透明几何、薄墙、小窗、密集植被和镜面反射。重点是如何避免统一 Probe 分布的内存爆炸，并在动态时间和季节内容中维持更新效率。 | **高**：对天气、季节、植被、半透明和 GI 的整帧一致性最有价值。 |
| 2 | [**Fast as Hell: idTech8 Global Illumination**](https://advances.realtimerendering.com/s2025/content/SOUSA_SIGGRAPH_2025_Final.pdf) | id Software 用实时 GI 替代 idTech7 的 Lightmap、Irradiance Volume 和多套 Bake 依赖。方案通过分层 Probe／局部 Volume、射线命中触发的 World Radiance Cache、空间哈希、异步计算、低分辨率 Final Gather、双边与时域过滤完成统一动态照明，并服务静态、动态和透明对象。 | **高**：展示如何把数小时 Bake 和大磁盘数据压缩为实时缓存，适合天气频繁变化的世界。 |
| 3 | [**Stochastic Tile-Based Lighting in HypeHype**](https://advances.realtimerendering.com/s2025/content/s2025_stb_lighting_v1.1_notes.pdf) | 面向 UGC 和低端移动 GPU 的固定成本局部光照：大 Tile 使用分层 Reservoir Sampling 收集候选灯，小 Tile 再采样以提升相关性和 GPU 一致性；随后依赖 TAA 去噪，并以 Samples Per Pixel、候选池规模和分辨率控制质量。 | **中高**：适合需要大量动态局部灯、但必须跨手机到 PC 运行的环境效果。 |
| 4 | [**MegaLights: Stochastic Direct Lighting in Unreal Engine 5**](https://advances.realtimerendering.com/s2025/content/MegaLights_Stochastic_Direct_Lighting_2025.pdf) | Epic 以固定每像素射线预算替代“灯越多成本越高”的传统 Deferred Lighting。系统包含 Light Importance Sampling、短距离 Screen Trace、硬件／软件 Ray Trace、统一直接光照与阴影、Ray Guiding、时空去噪，以及当前主机上的性能与质量权衡；同时可为 Volumetric Fog 提供灯光与阴影。 | **高**：与 UE 中体积雾、沙暴和雪暴接受大量动态灯光直接相关。 |

## 三、材质光传输与实时 SSS

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Real-Time Subsurface Scattering via Hybrid ReSTIR Path Tracing and Diffusion**](https://advances.realtimerendering.com/s2025/content/sss-siggraph-2025-advances-published.pdf) | NVIDIA 将单次散射的体积路径追踪与新的物理扩散模型结合，并以 ReSTIR 在空间和时间上复用样本，目标是在交互帧率获得接近路径追踪的半透明材质质量，同时减少传统扩散近似的形状和边界伪影。 | **中高**：对粉雪、冰、皮下式透射和高密度散射介质的光照模型有研究启发，但直接移植成本较高。 |

## 2025 年结论

| 方向 | 最值得吸收的方案 |
|---|---|
| 近景粒子与透明稳定性 | **AVBOIT：低分辨率透射率结构 + 自适应深度体素 + 全分辨率合成** |
| 大世界动态天气照明 | **AC Shadows RTGI + idTech8 实时 GI** |
| UE 多灯体积照明 | **MegaLights：固定射线预算和统一 Volumetric Fog 光照** |
| 低端跨平台灯光 | **HypeHype STB Lighting：Tile Reservoir + TAA** |
| 粉雪／冰的散射外观 | **Hybrid ReSTIR SSS：单散射路径追踪 + 多散射扩散** |
| 细粒介质的稀疏表示 | **Indiana Jones Strand：预计算可见性 + 体积阴影 + 透明合成** |

---

# 2026

## 一、当前公开状态

> 截至 **2026-06-17**，SIGGRAPH 2026 官网已经确认 Natalya Tatarchuk 将组织并参与 **Advances in Real-Time Rendering in Games, Part 1 与 Part 2**。SIGGRAPH 2026 将于 **2026 年 7 月 19—23 日**在洛杉矶举行。  
> 但官方 Advances `s2026` 年度页面、课程题目、讲者清单和讲义尚未公开或尚未被公开索引，因此本稿不虚构 2026 课程。

| 序号 | 已确认项目 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Advances in Real-Time Rendering in Games, Part 1** | SIGGRAPH 2026 已确认该课程继续举办；详细 Talk 题目、讲者与资料待官方发布。 | 待定 |
| 2 | **Advances in Real-Time Rendering in Games, Part 2** | SIGGRAPH 2026 已确认下午／第二部分课程；详细议程尚未公开。 | 待定 |
| 3 | **2026 年度 Advances Materials Page** | 截至整理日期尚无可核验的完整 `s2026` 课程材料页。正式资料通常会在会议前后逐步上线。 | 待定 |

## 二、2026 发布后应重点追踪的类别

下表是**资料追踪清单，不是已公布课程**。

| 序号 | 追踪类别 | 为什么值得关注 | 对当前课题的价值 |
|---:|---|---|---|
| 1 | **实时体积、透明与 OIT 后续** | 2025 的 AVBOIT 已建立透明 VFX 新基线，2026 若有后续，很可能涉及更低内存、更强遮挡或体积／粒子统一合成。 | **高** |
| 2 | **神经渲染与可训练光照缓存** | 2024 Neural Light Grid、2025 多种时空重用方案显示 ML 正在进入固定预算渲染基础设施。 | **高** |
| 3 | **动态世界模拟与 60 Hz 交互** | 2025 课程回顾中已明确把 Simulation 视为下一阶段竞争点。 | **高** |
| 4 | **GPU 驱动几何和新型工作提交** | 2023—2025 连续出现 VisBuffer、Cluster、CBT 和 GPU 缓存方案，仍可能继续向更统一的 Compute 管线演进。 | **中高** |
| 5 | **跨手机、主机和 PC 的同一内容路径** | HypeHype、Tencent、Activision 都在解决 author once 与平台碎片化问题。 | **高** |

---

# 2023—2025 技术趋势对比

| 维度 | 2023 | 2024 | 2025 |
|---|---|---|---|
| 核心问题 | 如何建立新的体积、材质和环境表示 | 如何把表示变成可维护的渲染基础设施 | 如何以固定预算处理复杂光照、透明与动态世界 |
| 体积／天气 | Nubis³ 体素云成为局部异构体范式 | 重点转向 GI、可见性和跨平台缓存 | AVBOIT、MegaLights、RTGI 开始解决体积与整帧合成 |
| 几何 | 大地形虚拟化、移动渲染架构 | Cluster、Visibility Buffer、CBT | 几何本身减少，重点转向其与 RT、透明和缓存的协同 |
| 材质 | Substrate 统一分层 BSDF | Shader 语言与作者工程化 | SSS、头发、透明等复杂光传输的固定预算实现 |
| 光照 | 混合光追与照片级校准 | Neural Probe、Surfel GI、半球编码 | 实时 GI 取代 Bake、随机多灯与开放世界 RTGI |
| 工程方向 | 新系统原型 | Shipping 化、跨项目复用和真实数据集 | 统一路径、固定成本、异步计算和跨平台质量分级 |

---

# 面向沙暴／雪崩的组合方案

这些课程并不是要求完整照搬，而是可拼成一个更稳的 **Weather Volume Enhancement Layer**。

| 模块 | 推荐课程 | 可提取的核心方案 | UE 中的现实落点 |
|---|---|---|---|
| A. 宏观密度与局部体积 | **Nubis³** | 体素密度、压缩 SDF 跳空、上采样、局部光照近似 | 自定义 Volume Pass；第一阶段可先用 Niagara Grid／Volume Texture 验证 |
| B. 世界光照缓存 | **Neural Light Grid、GIBS、idTech8 GI、AC Shadows** | Probe／Surfel／Radiance Cache 的动态更新与跨尺度组织 | 先复用 Lumen／Volumetric Fog；源码阶段再接自定义缓存 |
| C. 近景透明合成 | **AVBOIT** | 透射率预通路、自适应深度体素、固定内存 OIT | Renderer 源码级；可先实现 AVBOIT-lite 或分层 Weighted OIT |
| D. 多灯与体积光照 | **MegaLights、STB Lighting** | 固定射线／样本预算、重要性采样、时空过滤 | UE MegaLights + Volumetric Fog；低端设备使用简化 Tile Lighting |
| E. 地表积累与形变 | **Call of Duty Terrain、Substrate** | 虚拟页局部更新、动态脚印、材质分层和雪／冰附加通道 | Runtime Virtual Texture、Render Target、Nanite Tessellation／WPO |
| F. 几何与性能分级 | **HypeHype、Seamless Mobile、VisBuffer/VRS、CBT** | Cluster、GPU Culling、低分辨率着色、自动 LOD 和跨平台回退 | Device Profile、Scalability、自定义 Compute Pass、Nanite／HLOD |
| G. Shader 与插件维护 | **Serac** | 公共 Shader DSL／函数层、参数一致性、编译和部署经验 | UE Shader Library、Global Shader、SceneViewExtension、RDG 插件 |

## 优先观看顺序

| 优先级 | 课程 | 原因 |
|---|---|---|
| S | **Nubis³** | 当前课程中最直接的 shipping 级局部体积方案。 |
| S | **Adaptive Voxel-Based OIT** | 直接解决沙尘、粉雪和烟雾卡片的透明合成问题。 |
| S | **Large-Scale Terrain Rendering in Call of Duty** | 衔接雪／沙地表、积累、脚印和大地图事件。 |
| S | **Ray Tracing the World of Assassin’s Creed Shadows** | 建立天气、季节、植被、半透明和 GI 的系统级一致性。 |
| S | **Fast as Hell: idTech8 Global Illumination** | 展示如何从 Bake 转向动态世界光照，并给出完整缓存与性能链路。 |
| A | **MegaLights** | 直接关联 UE、多灯、体积雾和固定预算光照。 |
| A | **Neural Light Grid** | 适合研究低端平台上的世界间接光与漏光修正。 |
| A | **Substrate** | 用于雪、冰、湿润、沙尘覆盖等表面状态统一。 |
| A | **Visibility Buffer Rendering with VRS** | 为自定义体积 Pass 的降分辨率与边缘重建提供方法。 |
| A | **Flexible Shader Authoring with Serac** | 对长期维护 UE 自定义介质 Shader 和多 Pass 代码很关键。 |
| B | **Shipping Dynamic GI in Frostbite** | 适合作为 Surfel GI 和动态缓存的补充方案。 |
| B | **Real-Time SSS via Hybrid ReSTIR** | 更偏研究型，可用于粉雪和冰的高质量散射模型。 |

---

# 总结

从 2023—2025 的课程可以看出，工业实时渲染并没有走向“用一种高级体积格式替代所有效果”，而是逐步形成以下分层：

1. **宏观异构体**使用体素密度场、跳空和低带宽采样；
2. **世界光照**使用 Probe、Surfel 或 Radiance Cache；
3. **透明 VFX**使用专门的透射率／OIT 合成层；
4. **地表天气反馈**使用虚拟纹理、动态页更新和分层材质；
5. **跨平台**依靠固定样本预算、Cluster、低分辨率计算和质量回退；
6. **工程维护**依靠统一 Shader 接口、数据验证和清晰的 Pass 边界。

因此，对 UE 沙暴／雪崩项目更稳妥的落地顺序是：

> **UE 原生天气与材质编排 → Niagara／Render Target 局部模拟 → 地表积累反馈 → Nubis-lite 局部体积 → AVBOIT-lite 透明合成 → 自定义世界光照缓存。**

这样可以先形成可运行的完整系统，再逐层替换画质和性能瓶颈，而不是一开始就承担全套 Renderer 重写风险。
