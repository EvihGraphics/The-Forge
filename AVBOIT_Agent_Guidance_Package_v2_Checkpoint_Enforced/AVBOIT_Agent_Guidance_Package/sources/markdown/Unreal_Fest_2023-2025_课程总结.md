# Unreal Fest 2023—2025 课程内容总结

> 整理口径：以 Unreal Engine 官方 YouTube 频道在 2023—2025 年发布的 Unreal Fest 活动播放列表与官方活动页为主。  
> 表格沿用 Bali 版格式：**课程 / 主要内容 / 课题关联度**。  
> “课题关联度”针对当前研究方向：**UE 渲染管线、Niagara、环境 VFX、体积天气、沙暴/雪崩、性能优化与插件扩展**。
>
> 说明：2023 部分按官方直播课程表完整展开；2024—2025 的大型活动课程数量极多，本稿优先整理具有明确技术内容、生产经验或可迁移价值的公开视频。开幕式拆条、重复剪辑、纯宣传片及缺少可核验课程内容的条目不重复列出。Bali 2025 保留此前的完整 51 门整理。

---

# 2023

## Unreal Fest 2023：渲染、世界构建与工程基础

官方活动页：<https://www.unrealengine.com/events/unreal-fest-2023>

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Optimizing UE5: Rethinking Performance Paradigms for High-Quality Visuals Pt.1** | 从 Nanite、Lumen 等 UE5 高质量系统出发，解释传统“面数/Draw Call 优化”思路为何需要调整，并建立面向帧预算、可见性、材质和 GPU 工作量的优化方法。 | **高** |
| 2 | **Look Development with Substrate and Lumen** | 演示早期 Substrate 分层材质与 Lumen 的协同，重点讨论复杂表面、材质混合、间接光和实时 LookDev。 | **高** |
| 3 | **Developer Iteration and Efficiency in Unreal Engine** | 梳理编译、Cook、DDC、资源加载与编辑器迭代成本，介绍缩短“修改—验证”循环的工程手段。 | **高** |
| 4 | **Procedural Content Generation Tools in UE5: Overview and Roadmap** | 系统介绍 PCG Framework 的数据模型、图结构、空间采样和未来路线，可用于大世界环境布置与规则化资产生成。 | **高** |
| 5 | **Building Bigger: Changing Your Workflow for Building Worlds instead of Scenes** | 从“单个漂亮场景”转向“可持续生产的大世界”，涉及 World Partition、数据分层、内容规则、团队协作和性能约束。 | **高** |
| 6 | **Optimizing UE5 Pt.2: Supporting Systems** | 补充分析阴影、纹理、材质、动画、物理和后台系统等支持模块，强调系统间成本叠加。 | **高** |
| 7 | **The Bright Future of Mobile Ray Tracing in Unreal Engine** | 介绍移动端实时光追的硬件条件、功能边界、渲染路径与性能权衡，适合建立跨平台高低配认知。 | 中高 |
| 8 | **Advanced Debugging in Unreal Engine** | 展示断点、调用栈、日志、断言、控制台、Visual Logger、Insights 等调试手段，强调从症状定位到根因验证。 | **高** |
| 9 | **Rendering Roadmap: More Data, More Speed, More Pixels, More Fidelity** | Unreal 渲染路线图综述，覆盖几何、材质、光照、阴影、分辨率与 GPU 管线的发展方向。 | **高** |
| 10 | **Unreal Engine Development Update** | 汇总引擎开发进展和重要模块方向，为判断后续版本的技术迁移成本提供背景。 | 中高 |
| 11 | **Creating 25 Square Miles of Fun with World Partition** | 以超大地图为例讲解 World Partition、流送单元、HLOD、编辑协作和运行时加载管理。 | **高** |
| 12 | **Features and Tips for UE in ’23** | 快速串讲当年 UE 的重要功能、编辑器技巧和生产建议，适合作为版本能力总览。 | 中高 |
| 13 | **Extending Unreal Engine to Create the StoryTech of Hogwarts Legacy** | 讲解《霍格沃茨之遗》如何扩展 UE 支撑开放世界叙事、工具链和内容生产，体现项目级引擎定制方式。 | **高** |
| 14 | **Blueprints: What, When, Why, and How?** | 讨论蓝图和 C++ 的职责边界、可维护性、性能与团队协作，帮助确定原型、工具和运行时逻辑的实现层级。 | 中高 |

## Unreal Fest 2023：UEFN、Verse 与玩法生产

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **UEFN Roadmap** | 介绍 UEFN、Verse、内容能力和生态路线图，帮助理解 Fortnite 创作平台与标准 UE 的能力差异。 | 低 |
| 2 | **Fabulous Content for Fab: Creating Assets to Sell on Fab** | 讨论面向 Fab 的资产规范、可复用性、展示方式和发布流程。 | 低 |
| 3 | **Stylization in UEFN** | 从材质、灯光、建模和后处理等方面构建脱离默认 Fortnite 观感的风格化世界。 | 中 |
| 4 | **Adding Verse to Your Creative Toolbelt** | 介绍 Verse 的基本语法、设备交互、状态管理和 UEFN 玩法脚本思路。 | 低 |
| 5 | **Unreal Editor for Fortnite as a Rapid Prototyping Tool** | 展示利用现成设备、资产和多人基础设施快速验证玩法原型。 | 低 |
| 6 | **Using Animation in a Production Environment in UE5 and UEFN** | 讲解动画资产、Control Rig、Sequencer 与 UEFN 内容生产的衔接。 | 低 |
| 7 | **Finding the Fun in Fortnite: How to Create Player-Retentive Games in UEFN** | 从循环、反馈、节奏和留存角度分析 UEFN 游戏设计。 | 低 |
| 8 | **How to Make Your UEFN Game Feel Nothing Like Fortnite Battle Royale** | 通过 UI、相机、移动、材质和玩法框架弱化默认 Fortnite 表现。 | 低 |
| 9 | **Modeling Mode: Creating Props and Buildings in UEFN** | 使用 Modeling Mode 在引擎内快速制作、修改道具与建筑，减少 DCC 往返。 | 中 |
| 10 | **Cultural Relevance: Telling Local Stories through UEFN and RealityScan** | 利用 RealityScan、在地资产与 UEFN 表达本地文化内容。 | 低 |
| 11 | **Growing Your Community** | 讨论创作者社区运营、内容传播和用户反馈循环。 | 低 |
| 12 | **Building a Business Creating the Metaverse** | 从商业与团队角度讨论实时 3D 内容服务和平台型项目。 | 低 |

## Unreal Fest 2023：影视、动画、广播与案例

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Behind the Scenes on ESPN’s ‘NHL Big City Greens Classic’ Event** | 拆解实时体育转播中角色替换、跟踪、直播合成与数据驱动动画。 | 低 |
| 2 | **ICVR’s Real-Time Pipeline** | 介绍面向影视与品牌内容的实时资产、镜头、灯光和交付管线。 | 中 |
| 3 | **How NASA Is Using Simulations and Game Engine Technologies to Help Get Us Back to the Moon** | 展示 UE 在航天仿真、可视化和任务训练中的应用。 | 中 |
| 4 | **Creating Cinematics for Games, Film, TV, and Broadcast with Unreal Engine** | 概述 Sequencer、相机、灯光和实时渲染在多行业镜头制作中的统一流程。 | 中 |
| 5 | **Unleashing the Power of Unreal Engine: Animation Pipeline for Artists and Studios** | 讨论动画工作室如何把 UE 接入角色、镜头与最终渲染生产。 | 低 |
| 6 | **Project Avalanche: a Dedicated Toolkit for Broadcast Graphics and Motion Design** | 介绍后续 Motion Design 工具的早期形态，用于动态图形、克隆器和播包装。 | 中 |
| 7 | **State of the Union: Virtual Production** | 汇总 ICVFX、LED 虚拟制片、多机位、同步与现场工作流。 | 低 |
| 8 | **Underwater ICVFX: The Making of Emancipation** | 讲解水下虚拟制片的摄影、显示、跟踪和画面匹配难题。 | 低 |
| 9 | **Reimagining the Horror: Lessons Learned from Layers of Fear** | 复盘恐怖游戏环境、灯光、叙事和 UE5 迁移经验。 | 中 |
| 10 | **Stylization in Animation and FX** | 讨论风格化动画与特效中形状语言、节奏、材质和视觉取舍。 | 中 |
| 11 | **Ascendant Studios: Building a Big-Budget UE5 Game from Scratch** | 讲解新团队从零搭建 AAA UE5 项目的技术决策、内容管线和生产风险。 | **高** |
| 12 | **Making a Movie in the Cloud: Empowering Collaborative Filmmaking** | 介绍云端资产、远程协作、版本管理和实时渲染。 | 低 |
| 13 | **Against the Trend: Using Realistic Engine for Stylized Games** | 探讨如何在以写实为默认倾向的 UE 中构建稳定的风格化渲染。 | 中 |
| 14 | **Photoreal Digital Actors from Capture to Final Render: a Blue Dot Case Study** | 从扫描、MetaHuman、动画捕捉到最终画面，梳理数字人端到端流程。 | 低 |
| 15 | **Riding the Lightning: from Previz to Final Pixel** | 介绍从预演到最终像素尽可能保留实时数据与创作决策的影视流程。 | 低 |
| 16 | **The Importance of the Art Department in Visual Storytelling** | 强调美术部门在虚拟制作中的前期设计、世界观和镜头沟通作用。 | 低 |
| 17 | **Automated Dialogue Workflows at Embark Studios** | 介绍自动化对白录制、语音资产、字幕与游戏内集成流程。 | 低 |
| 18 | **Unlocking Creativity – Panel** | 多位创作者讨论实时工具如何改变创意和团队协作。 | 低 |

---

# 2024

## Unreal Fest Gold Coast 2024：技术课程

官方播放列表：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gZK_Dt-WymqP4UrAr6pdHZ4>

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Advanced Rendering and Debugging Tips for Unreal Engine 5** | 从 Buffer Visualization、GPU 调试、阴影、Lumen/Nanite 常见问题入手，建立画面异常与性能问题的排查方法。 | **高** |
| 2 | **TSR, Nanite, Lumen, VSM: UE5 Graphics Features Insights from Japan** | 汇总日本项目使用 TSR、Nanite、Lumen 和 VSM 的实际经验，强调功能适用条件和错误配置。 | **高** |
| 3 | **Virtualize Everything: Polygons, Shadows, and Textures, Oh My!** | 解释 Nanite、Virtual Shadow Maps、Virtual Textures 等虚拟化系统如何重构资源和渲染预算。 | **高** |
| 4 | **Advanced Niagara VFX: Fluids, Simulation Stages, and More!** | 深入 Niagara Fluids、Simulation Stage、Grid 数据接口和自定义 GPU 模拟，属于环境 VFX 的核心课程。 | **高** |
| 5 | **You’re Probably Lighting Wrong: Physically Based Lighting in UE5** | 从物理曝光、光强单位、天空和相机设置纠正常见“凭感觉调灯”问题。 | **高** |
| 6 | **Advanced Blueprinting Techniques in Unreal Engine** | 讲解蓝图架构、接口、组件化、异步逻辑和可维护设计，突破简单事件图用法。 | 中高 |
| 7 | **How to Benefit from Multithreading in Your Unreal Engine Projects** | 介绍 Task Graph、Async Task、线程安全和适合并行化的工作负载。 | **高** |
| 8 | **Implementing a Quality Cloud CI System Using Horde** | 讲解 Horde 在构建、测试、远程执行和持续集成中的落地。 | 中高 |
| 9 | **A Few Good Tools: How a Small Team Can Make a Big Difference** | 展示小团队如何利用 Editor Utility、脚本与自动化工具放大生产效率。 | **高** |
| 10 | **Artist’s Guide to Editing the Editor: Automation, Validation, and Tools** | 从技术美术角度扩展编辑器、批处理资产、数据验证和美术工具。 | **高** |
| 11 | **Game Framework Extensions: Four Deep Dives in Forty Minutes** | 对 Game Framework 的若干扩展点做快速深入解析，帮助理解引擎对象之间的职责。 | 中 |
| 12 | **Exploring the New State Tree for AI** | 介绍 StateTree 的状态组织、Evaluator、Task、Transition 与大规模 AI 用法。 | 低 |
| 13 | **Exploring the Power of Control Rig for Animation in UE 5.4** | 展示 Control Rig、模块化 Rig 和引擎内角色动画制作。 | 低 |
| 14 | **Motion Matching and the Game Animation Sample in UE 5.4** | 解析 Pose Search、轨迹查询、数据库和官方 Game Animation Sample。 | 低 |
| 15 | **Optimized MetaHumans and Cloth Workflows in Talisman** | 讨论 MetaHuman、Chaos Cloth、LOD 和跨平台角色优化。 | 中 |
| 16 | **20 Things You Should Be Using in Unreal Motion Graphics** | 快速总结 UMG 的布局、失效缓存、材质、动画和复用技巧。 | 低 |
| 17 | **Learnings from The Amazing Digital Circus and Murder Drones** | 动画项目如何使用 UE 做实时场景、灯光、镜头与高频交付。 | 低 |
| 18 | **Improving Development Iterations: A Deep Dive into Unreal Engine Workflows** | 从 DDC、Cook、编译和资源管理角度优化日常迭代。 | **高** |

## Unreal Fest Prague 2024：技术课程

官方播放列表：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gZZJOmMfAsli_S2vx4mVSs7>

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **State Tree Deep Dive** | 深入 StateTree 执行模型、状态选择、并行 Task、Transition 和调试。 | 低 |
| 2 | **PCG: First Steps to Advanced Development** | 从基础节点到自定义 Element、属性流和复杂程序化规则，构建可扩展 PCG 工具。 | **高** |
| 3 | **Extending the Unreal Editor** | 涵盖 C++ 编辑器扩展、Details、自定义 Gizmo、Scriptable Tools 与专用资产编辑器。 | **高** |
| 4 | **Modular Rigging in Unreal Engine 5.4** | 介绍模块化 Control Rig 的组件、连接规则和角色 Rig 组装。 | 低 |
| 5 | **Motion Matching and the Game Animation Sample** | 通过官方示例讲解 Motion Matching 的数据库、Schema、轨迹和调试。 | 低 |
| 6 | **UE, Twinmotion, Fortnite, and BIM: Landscape Architecture at Heatherwick Studio** | 展示 BIM、Twinmotion、UE 与 Fortnite 在景观设计和沟通中的组合。 | 低 |
| 7 | **Amsterdam ZuidasDOK: A Digital Twin Platform Built on UE 5.4** | 介绍大型基础设施数字孪生中的数据接入、可视化、交互和部署。 | 中 |
| 8 | **Procedurally Generating Level Sequences** | 将 PCG/脚本用于 Sequencer 镜头和动画生成，减少重复镜头劳动。 | 中 |
| 9 | **Building Custom Tools with Geometry Script** | 使用 Dynamic Mesh、Geometry Script 和 Scriptable Tools 建立几何处理工具。 | **高** |
| 10 | **Optimizing the Game Thread** | 通过 Unreal Insights 定位 Tick、对象管理、蓝图和系统调度成本。 | **高** |
| 11 | **Using Simple Generic Materials to Improve UI Performance** | 通过统一 UI 材质和参数化减少状态切换与材质实例数量。 | 低 |
| 12 | **How Scene Graph Can Improve Your Life** | 介绍 UEFN Scene Graph 的层级、组件化与未来内容组织方向。 | 低 |
| 13 | **Building Custom Tools and Avoiding Common Pitfalls with Perforce + Unreal Engine** | 讲解 Typemap、文件锁、工作区、分支和 UE 二进制资产协作。 | 中高 |
| 14 | **Next-Generation Modular Characters** | 介绍 Modular Characters、部件组合和角色定制架构。 | 低 |
| 15 | **An Artist’s Guide to Using Nanite Tessellation** | 展示 Nanite Tessellation 在地表和材质细节中的使用、限制与性能注意事项。 | **高** |

## Unreal Fest Seattle 2024：渲染、世界与性能

官方播放列表：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gb0rxbHfn2t--7jO2gADVNT>

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Future Features in Unreal Engine: 5.5 and Beyond** | 预览 UE5.5 及后续的渲染、动画、PCG、移动端和生产工具方向。 | **高** |
| 2 | **Sneak Peek at Unreal Engine 5.5** | 汇总 5.5 的重点功能，包括渲染、动画、虚拟制作和移动端改进。 | 中高 |
| 3 | **PCG: Advanced Topics & New Features in UE 5.5** | 深入属性、多数据、递归、Grammar、Spline Mesh、Raycast 与 GPU PCG。 | **高** |
| 4 | **Geometry Scripting and Scriptable Tools** | 通过 Geometry Script、Editor Mode 和自定义 UI 制作生产级建模与布景工具。 | **高** |
| 5 | **Project Titan: Building an Open World Game in Public** | 复盘 8×8 km 开放世界样例与社区协作，涉及 World Partition、PCG 和多平台约束。 | **高** |
| 6 | **Project Atlante: Building Earth-Scale Worlds with UE Tools Only** | 研究地球尺度地理数据的分块、流送、打包和大世界可视化。 | **高** |
| 7 | **On-Target Iteration in Unreal Engine 5.5 and Beyond** | 介绍 ZenServer、Cloud DDC、Zen Snapshot 和面向设备的快速 Cook/部署。 | **高** |
| 8 | **Horde and the Unreal Build Accelerator** | 讲解分布式编译、构建自动化、测试和团队 DevOps。 | 中高 |
| 9 | **Myth-Busting “Best Practices” in Unreal Engine** | 用测量和引擎机制纠正常见但不普适的 UE 开发“最佳实践”。 | **高** |
| 10 | **50 Tips and Tricks in Modeling Mode** | 展示 Modeling Mode 的高频工具、几何修改和引擎内建模效率技巧。 | 中 |
| 11 | **Obscure Techniques for Better Development Experience and Visual Candy** | 涉及多层 Landscape 材质、Skylight Fade Volume、植被遮罩、Local Volumetric Fog 等技巧。 | **高** |
| 12 | **Where We’re Going, We Need Roads: The Tech Art of Rocket Racing** | 拆解道路材质、样条、地形融合和高速场景的技术美术方案。 | **高** |
| 13 | **Embracing Chaos: The Eternal Strands Approach** | 介绍基于 Chaos 的物理角色控制与巨型敌人交互。 | 中 |
| 14 | **Learning Agents in Unreal Engine** | 介绍强化学习/模仿学习插件在 AI、物理动画和自动测试中的潜力。 | 中 |
| 15 | **Building a Shared AAA Game Development Ecosystem at Riot** | 讲解多项目共享引擎、基础设施、工具和通用技术的组织方式。 | **高** |
| 16 | **Audio Workflows and Tips for Indie Projects** | 小团队音频资产、MetaSounds 和工程组织方法。 | 低 |
| 17 | **Building Custom Tools and Avoiding Common Pitfalls with Perforce + Unreal Engine** | 聚焦大型二进制资产项目的版本管理与自动化。 | 中高 |
| 18 | **Bringing ‘Fera: The Sundered Tribes’ to Unreal Engine** | 小团队迁移与生产案例，涵盖工具、性能和平台交付。 | 中 |
| 19 | **Practical Digital Twins** | 数字孪生的数据接入、实时可视化和企业部署案例。 | 低 |
| 20 | **Enter the Cockpit: Training Airline Pilots with UE** | 专业飞行模拟器如何使用 UE 提供高保真视觉系统。 | 中 |

## Unreal Fest Seattle 2024：动画、影视与跨行业

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Advanced Animation Techniques** | 面向专业动画师介绍引擎内动画层、曲线、Control Rig 和 Sequencer 工作流。 | 低 |
| 2 | **State of Virtual Production** | 汇总 UE5.5 虚拟制作、SMPTE 2110、多机位和 ICVFX 更新。 | 低 |
| 3 | **Unreal Engine Motion Design: Cutting-Edge Tools and Techniques** | 介绍 Motion Design、Cloner、Effector 和动态图形材质。 | 中 |
| 4 | **The World of Shōgun: History and Backstory Using Unreal Engine** | Method Studios 以 UE 构建历史短片，整合资产、镜头和实时渲染。 | 低 |
| 5 | **From VFX to VAD: Artists’ Journeys with Unreal Engine** | 传统 VFX 艺术家转向虚拟美术部门的技能与流程变化。 | 低 |
| 6 | **How to Stand Up Performance Capture in UEFN** | 复盘 JokeNite 的实时动作捕捉、远程协作与 UEFN 角色表演。 | 低 |
| 7 | **Cinematics Are Dead, Long Live TVmatics** | 将实时游戏环境与电视化叙事结合的内容形态探索。 | 低 |
| 8 | **Creating Compelling Procedural Music: Composing with UE Audio in Cycles** | 使用 MetaSounds 和游戏状态构建程序化音乐。 | 低 |
| 9 | **Mega Canvas, Infinite Resolution: Clustered Rendering** | 介绍大型多屏、集群渲染和现场体验的同步与分布式输出。 | 中 |
| 10 | **Beyond Configurators: Visualizing the BMW 5 Series** | 汽车可视化从配置器扩展到品牌、营销与交互体验。 | 低 |
| 11 | **Building Immersive Real-World Digital Twins with Unreal, Twinmotion and Cesium** | 组合现实地理数据、Twinmotion 和 UE 构建数字孪生。 | 中 |
| 12 | **Architectural Visualization for Design Strategies on a 120-Year Project** | 长周期建筑项目如何使用实时可视化支持设计决策和沟通。 | 低 |

---

# 2025

## Unreal Fest Orlando 2025：渲染、世界与性能

官方播放列表：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gbSPueZMAf0gacwmuVBU3hO>

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **First Look at Unreal Engine 5.6** | 总览 UE5.6 的开放世界、渲染、动画、MetaHuman 和移动端改进。 | **高** |
| 2 | **The Road to 60 FPS in The Witcher 4 UE5 Tech Demo** | 解析大型开放世界技术演示如何围绕 60 FPS 预算优化 CPU、GPU、流送和植被。 | **高** |
| 3 | **Streaming Improvements for Dense Worlds in The Witcher 4 UE5 Tech Demo** | 介绍 Fast Geometry Streaming、异步物理状态和密集世界内容流送。 | **高** |
| 4 | **Avowed: A GPU Technical Retrospective** | Obsidian 回顾《宣誓》的 UE5 GPU 技术选择、瓶颈和后期优化。 | **高** |
| 5 | **Technical Artist’s Guide to Profiling in Unreal Engine** | 从技术美术角度把 Insights、GPU Profile 和内容指标转化为可执行优化任务。 | **高** |
| 6 | **Optimizing Niagara: a Practical Approach to Performant Worlds** | 系统讲解 Niagara Stats、Debugger、Insights、Effect Type、Scalability、Pooling、Lightweight Emitter 和 Data Channel。 | **高** |
| 7 | **Subculture Rendering and Calculations in Mongil: Star Dive** | Netmarble 介绍二次元角色与场景的定制渲染、Shader 和 GPU 优化。 | 中高 |
| 8 | **Developer Efficiency in Unreal Engine 5.6** | 端到端介绍编译、Cook、DDC、资产和设备迭代效率。 | **高** |
| 9 | **First-Person Rendering in Unreal Engine 5.6** | 讲解第一人称 FOV、深度、阴影、武器与世界渲染的稳定配置。 | 中 |
| 10 | **Mobile Game Development with Unreal Engine 5.6** | 汇总移动渲染路径、设备配置、性能与 UE5.6 新能力。 | 中高 |
| 11 | **Unity to Unreal Engine Transition: Workflows for Mobile Development** | 对照 Unity/UE 工作流、蓝图、设备配置和移动端性能。 | 中 |
| 12 | **Taking the Pain Out of Engine Upgrades** | 讲解长期分支、插件、自动测试和引擎升级风险控制。 | **高** |
| 13 | **How Epic Games Uses Horde to Make Builds Better** | 深入 Epic 使用 Horde、UGS、构建农场和测试的实践。 | 中高 |
| 14 | **Low-Level Development Using UE and the Latest Gaming Platforms** | 讨论主机平台、底层系统、RHI 和项目级低层开发协作。 | **高** |
| 15 | **Creating the ‘Otherworld’ of SILENT HILL 2** | 环境设计、灯光、材质和关卡引导如何共同建立异世界体验。 | 中高 |
| 16 | **25 Ways to Stylize a Project in Unreal Engine** | 从材质、光照、后处理、几何和动画列举风格化手段。 | 中 |
| 17 | **Powering Up Your Projects with Scene Graph and Verse** | 介绍 Scene Graph、组件与 Verse 的项目架构。 | 低 |
| 18 | **UEFN HLODs, Data Layers, Draw Distance, and Static Level Optimizations** | 系统讲解 UEFN 的 HLOD、流送、空间加载与静态场景优化。 | 中高 |

## Unreal Fest Orlando 2025：动画、AI 与制作工具

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **State of Animation Authoring Tools in UE 5.6** | 汇总 Skeletal Editor、Control Rig、Animation Layers、Deformer 等引擎内动画工具。 | 低 |
| 2 | **Rigging for Animators in Unreal Engine** | 面向动画师讲解 Control Rig、Skeletal Editor 和 Deformer 的实用 Rig 工作流。 | 低 |
| 3 | **The Future of Animation Retargeting in Unreal Engine** | 介绍跨比例、跨骨架重定向和 UE5.6 的改进。 | 低 |
| 4 | **Unreal Animation Framework in The Witcher 4 UE5 Tech Demo** | 拆解《巫师4》技术演示的动画框架、Motion Matching 与高密度人群/角色表现。 | 低 |
| 5 | **Control Rig Physics: Fast, Fun, and Expressive Character Animation** | 将物理、约束和 Control Rig 结合，生成可控的次级运动和角色表现。 | 中 |
| 6 | **Build Your Entire Animation Workflow in Unreal Engine** | 从静态资产、Rig、动画到 Sequencer 最终镜头的一体化流程。 | 低 |
| 7 | **Using Gameplay for Animating and Prototyping** | 利用游戏输入、录制和运行时行为快速生成动画素材与原型。 | 低 |
| 8 | **State of Performance Capture in Unreal Engine** | 介绍面部/身体表演捕捉和 MetaHuman Animator 更新。 | 低 |
| 9 | **xADA: Expressive Audio Driven Animation for MetaHumans** | 使用机器学习从语音生成面部、舌头和头部动画。 | 低 |
| 10 | **Build AI-Powered Digital Humans in Unreal Engine 5** | 结合 NVIDIA ACE 和 MetaHuman 构建可对话数字人。 | 低 |
| 11 | **Closing the Sim-to-Real Gap with Unreal Engine** | 讨论机器人/AI 仿真、AirSim 类环境和云端训练。 | 中 |
| 12 | **Building Extensible RPG Systems with the Gameplay Ability System** | 讲解 GAS 的模块化 RPG 能力、状态和数据驱动设计。 | 低 |

## Unreal Fest Bali 2025：渲染、材质、光照与性能

官方播放列表：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gZy2nANAiZTd72TBvLyurkl>

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Rolling Shore Waves in 2XKO’s Scuttler’s Strand** | Riot 拆解《2XKO》卷岸波浪：基于顶点着色器的三维程序化位移，通过简单函数组合出翻卷、推进和非重复波形。 | **高** |
| 2 | **Exploring Substrate Materials: Basic to Advanced Techniques** | 从 Slab、混合、分层讲到汽车漆、水坑、河流、积雪和 Nanite Tessellation。 | **高** |
| 3 | **UE5 Graphics Deep Insights From Japan** | 汇总 Nanite、虚拟纹理、Lumen 软件光追和 VSM 的项目经验与常见错误。 | **高** |
| 4 | **Beyond Scalability: Multi-Platform Insights From Japan** | 讨论设备配置、平台开关、材质/资产回退和多平台自动验证。 | **高** |
| 5 | **Lighting in UE5: Scaling for Quality & Performance** | 以《BADMAD ROBOTS》为例，从高端 Lumen 缩放到低端设备，并展示性能优化过程。 | **高** |
| 6 | **The Artistic and Technical Approach to Lighting in Fortnite: Battle Royale** | 讨论昼夜、天气、可读性、跨平台一致性和灯光预算。 | **高** |
| 7 | **Pushing Visual Boundaries Without Breaking the Bank** | 在有限硬件与制作预算下组合高级图形能力，并建立质量分级和回退。 | **高** |
| 8 | **Megascans Vegetation: What’s New and What’s Coming Soon** | 介绍 Fab 植物库、Nanite 植被、风动、材质和后续方向。 | 中高 |
| 9 | **Mastering Performance Analysis with Unreal Insights** | 系统定位 Game/Render/GPU、内存、加载和偶发尖峰。 | **高** |
| 10 | **A Tech Artist’s Guide to Automated Performance Testing** | 从脚本到 Automated Performance Testing 插件，建立性能回归和版本对比。 | **高** |
| 11 | **Tips and Tricks for Cloth Dynamics** | 对比布料动力学方案、制作流程、性能分级和回退。 | 中 |

## Unreal Fest Bali 2025：工程架构、调试与生产基础设施

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 12 | **Breaking (and Fixing) Unreal: An Engineer’s Guide to Problem-Solving** | 通过最小复现、日志、断言、调用栈和源码验证系统定位问题。 | **高** |
| 13 | **Beyond Print String: Debugging Unreal Engine Lightning Round** | 快速展示日志、控制台、蓝图/C++ 调试和运行时状态观察。 | **高** |
| 14 | **Enhanced Validation: Lessons From a Custom AAA Implementation** | 扩展 Data Validation 到 Actor、Level Instance 和提交工作流。 | **高** |
| 15 | **Technical Pre-Production Fundamentals for Unreal Engine Projects** | 在量产前验证平台、帧率、引擎版本、插件、资产规模和技术风险。 | **高** |
| 16 | **Optimizing Pre-Production to Prevent Costly Pipelines** | 使用 Control Rig、PCG 和 Scriptable Tools 减少 DCC 往返并提前固化工具。 | **高** |
| 17 | **Introduction to Horde: A Technical Primer** | 介绍分布式构建、任务调度、CI、远程执行和团队资源管理。 | 中高 |
| 18 | **Lessons From a Plugin Developer: How to Extend UE When You’re Not Epic** | Voxel Plugin 团队总结模块、委托、扩展点、反射和避免长期引擎 Fork 的方法。 | **高** |
| 19 | **Levelling Up: Advanced Perforce Techniques for UE Projects and Teams** | Streams、Typemap、文件锁、工作区和大型 UE 团队分支策略。 | 中高 |
| 20 | **Unity to Unreal Engine Transition: Workflows for Mobile Development** | 对照 Unity/UE 对象、资源、脚本、构建和移动端性能。 | 中 |
| 21 | **Supporting Mods and UGC in Your Unreal Engine Game** | 从项目架构预留 Mod/UGC 内容边界、插件化、加载、兼容和发布流程。 | 中 |

## Unreal Fest Bali 2025：开放世界、PCG 与数字化场景

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 22 | **Inside Project Titan: Making an Open World Game with 4,000 People** | 回顾 64 km² 开放世界和大型协作 Art Jam 的底层世界、内容模板和协作规则。 | **高** |
| 23 | **Leveraging PCG for Building and City Creation** | 用 PCG 生成建筑与城市，讨论组件、属性、层级和美术可编辑性。 | **高** |
| 24 | **Procedural Roads and Buildings in PCG** | 使用 UE5.5/5.6 PCG 构建道路、建筑、样条和城市结构。 | **高** |
| 25 | **Upin & Ipin Go Global: Crafting an Open World UE5 Game from Southeast Asia** | 结合 Lyra、GAS、World Partition、LOD/HLOD 和资产虚拟化进行跨平台开放世界开发。 | **高** |
| 26 | **Carving Reality: From Chainsaws to Digital Landscapes** | 摄影测量、RealityCapture、Rhino/CAD 与 Twinmotion 的现实场地数字化。 | 中 |

## Unreal Fest Bali 2025：Gameplay、网络与 AI

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 27 | **2025 Tech Designers Toolkit** | 串联相机、蓝图工具、StateTree、GAS Channel、Gameplay Effect 和 Enhanced Input。 | 中 |
| 28 | **Gameplay Ability System: Game Designer Examples** | 从设计师角度配置 Ability、Attribute、Effect、Tag、触发和冷却。 | 低 |
| 29 | **Best Practices for Networked Movement Abilities** | 处理冲刺、翻越、攀爬、抓钩的预测、服务器权威、回滚和视觉反馈。 | 低 |
| 30 | **Network Prediction: Replication’s Crystal Ball** | 介绍确定性模拟的客户端预测、状态校正与回滚重放。 | 低 |
| 31 | **Smart Ant: Building AI Behavior with State Tree and Smart Objects** | 组合 StateTree、Smart Object 和 Gameplay Interaction 构建群体交互。 | 中 |
| 32 | **To Hell and Back: Going Rogue in Unreal Engine** | 《Malys》的 GAS、Random Stream、定制日志和紧张周期下的系统设计。 | 低 |
| 33 | **Dealing with Localized Keywords in Card Games** | 卡牌关键词、术语表、Google Sheets、PO 文件和 UMG 本地化工具。 | 低 |

## Unreal Fest Bali 2025：动画、角色与数字人

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 34 | **Animation Authoring in Unreal Engine** | 在 UE 内从零制作动画，组织 Control Rig、Sequencer、关键帧和动画资产。 | 低 |
| 35 | **Animation Editing in Unreal Engine** | 修改已有动画、曲线、姿态和镜头所需局部变化。 | 低 |
| 36 | **Embracing Motion Matching: Using a Little to Get a Lot** | 用有限动画数据构建 Pose Search 数据库、查询特征和轨迹。 | 低 |
| 37 | **Customize Anything: Embracing Mutable** | 使用 Mutable 在运行时生成/合并 Skeletal Mesh、材质和纹理。 | 中 |
| 38 | **Creating Performant MetaHuman Characters in Unreal Engine** | 聚焦 MetaHuman LOD、材质、骨骼、动画和中低端平台优化。 | 中 |
| 39 | **How to Create Grooms for MetaHumans** | 完整演示 Groom 造型、曲线属性、导入 UE 和发布优化。 | 低 |
| 40 | **Learning to Walk, Run, and Deliver: Our Journey from 5.0 to 5.5 and Beyond** | Brown Bag Films 的 Rig、Deformer、毛发、工具升级与跨团队实时动画管线。 | 中 |
| 41 | **Wingstar: A Bold Leap into Animating Within Unreal Engine** | 使用 MetaHuman、AI 辅助工具和 UE 内动画完成长篇项目。 | 中 |

## Unreal Fest Bali 2025：影视、Motion Design、UI 与 UEFN

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 42 | **Building Real-Time Cinematics at M2 Animation** | 从预渲染转向 UE 实时资产、镜头、灯光和交付管线。 | 中 |
| 43 | **Bringing Unreal Engine into a Classic CG Pipeline with Python** | 用 Python、Maya、ShotGrid 自动导出资产、创建 Level/Sequence 和 MRQ 预设。 | 中高 |
| 44 | **The Future of Previz: Collaborative Filmmaking in Unreal Engine** | 利用 Sequencer 和远程协作快速完成预演与镜头迭代。 | 低 |
| 45 | **The Fast and the Curious: Advanced Materials for Motion Design** | Material Designer、Cloner Attribute 和动态图形高级材质。 | 中 |
| 46 | **Unlocking Creative Storytelling Through Cutting-Edge Technology** | UE、硬件和 AI 辅助工具结合的实时非线性动画管线。 | 低 |
| 47 | **5-Minute Operations to Improve Your UI** | 快速串讲 UMG 布局、复用、视觉调整和高频工作习惯。 | 低 |
| 48 | **Tools, Frameworks, and Insights into Rapid UI Iteration** | 构建无需频繁 PIE 的 UI 预览和快速反馈循环。 | 低 |
| 49 | **A Childlike Perspective of the Verse Programming Language** | 用非程序员友好的方式解释 Verse 变量、函数、控制流和设备交互。 | 低 |
| 50 | **The Art of Real-Time Concerts: Building a Fortnite UGC Event With UEFN** | 组合 Verse、Cinematic Sequence、角色、VFX 和服装模拟完成在线演唱会。 | 中 |
| 51 | **Building Massively Multiplayer Browser Experiences with Xsolla Metasites** | 通过云端 UE、Pixel Streaming、会话和扩展构建浏览器多人体验。 | 中 |

## Unreal Fest Stockholm 2025：渲染、性能与环境技术

官方播放列表：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gar0LXDZDcg8vivvEwW86ZJ>

| # | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | **Unreal Engine 5.7 Sneak Peek** | 预览 UE5.7 的渲染、Nanite Foliage、动画、工具与开发体验。 | **高** |
| 2 | **New GPU Profiler and RHI Submission Pipeline** | 深入 UE5.6 新 GPU Profiler 与现代 RHI 提交线程模型，帮助分析 Render/RHI/GPU 瓶颈。 | **高** |
| 3 | **Everything You Wanted to Know About Substrate—But Were Too Afraid to Ask** | 系统解释 Substrate 的 BSDF、Slab、混合、分层、性能和迁移。 | **高** |
| 4 | **Large-Scale Animated Foliage in The Witcher 4 UE5 Tech Demo** | 拆解大规模动态植被的数据、动画和渲染方案。 | **高** |
| 5 | **The Future of Nanite Foliage** | 介绍面向高密度植被的 Nanite 新路径、内存和动画挑战。 | **高** |
| 6 | **Interactive Vines Using Niagara and Position-Based Dynamics** | 使用 Niagara Simulation Stage、Grid2D、PBD、距离场碰撞和纹理关节动画实现交互藤蔓。 | **高** |
| 7 | **Profiling with Purpose: Performance Lessons from a Real Unreal Project** | 以真实项目演示从捕获、假设、验证到优化的完整性能方法。 | **高** |
| 8 | **Introduction to Horde: A Technical Primer** | 深入 Horde、UGS、遥测、构建和移动端迭代基础设施。 | 中高 |
| 9 | **Creating Debug Tools with SlateIM** | 使用 SlateIM 快速开发运行时/编辑器调试界面和工具。 | **高** |
| 10 | **I Wish I Learned This Sooner! – Part 2** | 汇总一组容易被忽视但能显著提高 UE 开发效率的功能和技巧。 | 中高 |
| 11 | **Materials, Shaders, and Substrate – Unreal Engine Development** | 从 Shader 编译、材质系统到 Substrate 的底层与生产工作流。 | **高** |
| 12 | **From Texture to Display: The Color Pipeline of a Pixel in Unreal Engine** | 解释纹理色彩空间、线性计算、HDR、Tonemapping 和显示输出。 | **高** |
| 13 | **Unreal Materials: New Features and Productivity Enhancements** | 汇总材质编辑器、函数、参数和生产效率改进。 | 中高 |
| 14 | **The State of Model Importing Processes in Unreal Engine** | 对比 Interchange、Datasmith、FBX 等导入链路和未来方向。 | 中 |
| 15 | **The State of Animation Authoring Tools in UE 5.6** | 回顾动画工具现状与后续方向。 | 低 |
| 16 | **How to Make Control Rigs Smart** | 通过元数据、模块和逻辑提高 Control Rig 的复用与自适应能力。 | 低 |
| 17 | **Crafting Scalable AI for a AAA Souls-Like Game** | 《堕落之主》感知、目标、仇恨和决策系统的模块化架构。 | 低 |
| 18 | **Florian and Sam Make a Real-Time Strategy Game in UEFN** | 使用 Verse、设备和 UEFN 快速构建 RTS 原型。 | 低 |
| 19 | **How 2D Creatives Can Embrace Unreal Engine with Odyssey** | 介绍 2D/故事板创作者进入 UE 实时制作的工作流。 | 低 |
| 20 | **Disrupting the Traditional: The Unreal Evolution of Real-Time Animation** | Dimension Studio 的实时动画与非线性制作模式。 | 低 |
| 21 | **Engineering Digital Twins for Milano Cortina 2026 Winter Olympics** | 将 BIM、GIS、地图和 UE5 结合用于冬奥基础设施数字孪生。 | 中 |
| 22 | **Portal to Reality: Fusing Real-World Assets with Unreal Workflows** | RealityScan/摄影测量资产进入 UE 的采集、清理和实时使用流程。 | 中 |
| 23 | **Making Digital Twins Playable: From UEFN to Unreal Engine** | 把数字孪生从可视化扩展为可交互、可部署体验。 | 中 |
| 24 | **XR Streaming and Digital Twins: Enabling an Open Infrastructure Metaverse** | 讨论云渲染、XR Streaming 和大规模数字孪生交付。 | 低 |

---

# 三年变化总结

| 年份 | 课程重心 | 对当前课题最重要的变化 |
|---:|---|---|
| **2023** | UE5 核心功能认知、Lumen/Nanite/Substrate 早期生产化、PCG 与 World Partition | 建立“UE5 新系统能做什么”的基础认知；环境与渲染仍以功能介绍为主。 |
| **2024** | 工具化、自动化、跨平台、开放世界生产、Niagara/PCG 深入 | 技术开始从功能展示转向生产经验；出现更多 Simulation Stage、GPU PCG、编辑器扩展和持续集成。 |
| **2025** | 60 FPS 大世界、Niagara 工程化、RHI/GPU Profiler、Substrate 正式化、Nanite Foliage | 最接近当前沙暴/雪崩项目的阶段：强调成本测量、GPU 数据流、跨平台回退和可维护的插件/工具链。 |

# 面向沙暴 / 雪崩项目的优先观看顺序

| 优先级 | 课程 | 直接用途 |
|---:|---|---|
| S | **Advanced Niagara VFX: Fluids, Simulation Stages, and More!（Gold Coast 2024）** | 建立 Niagara GPU 模拟、Grid 和 Simulation Stage 基础。 |
| S | **Interactive Vines Using Niagara and PBD（Stockholm 2025）** | 学习生产级 Niagara Compute、PBD、距离场碰撞、渲染数据输出。 |
| S | **Optimizing Niagara: a Practical Approach to Performant Worlds（Orlando 2025）** | 构建 Niagara 性能分析、Effect Type、Scalability 和 Data Channel 方法。 |
| S | **New GPU Profiler and RHI Submission Pipeline（Stockholm 2025）** | 深入理解渲染线程、RHI 线程和 GPU 提交流程。 |
| S | **Lessons From a Plugin Developer（Bali 2025）** | 决定外部插件扩展、引擎 Fork 与源码修改的边界。 |
| S | **Mastering Performance Analysis with Unreal Insights（Bali 2025）** | 对体渲染、Niagara 和自定义 Pass 建立可复查性能证据。 |
| A | **Rolling Shore Waves in 2XKO（Bali 2025）** | 程序化环境运动可迁移到沙面、风吹雪和雪崩边界。 |
| A | **Exploring Substrate Materials（Bali 2025）** | 构建积雪、湿雪、沙尘覆盖和地表状态变化。 |
| A | **Obscure Techniques…（Seattle 2024）** | Local Volumetric Fog、Landscape 材质和环境细节技巧。 |
| A | **The Road to 60 FPS in The Witcher 4（Orlando 2025）** | 学习高质量大世界功能如何服从整帧预算。 |
| A | **A Tech Artist’s Guide to Automated Performance Testing（Bali 2025）** | 建立固定天气状态和固定镜头的自动性能回归。 |
| A | **PCG Advanced Topics（Seattle 2024）** | 生成风场采样点、地表类型、碰撞代理和天气触发区域。 |

# 主要来源

- Unreal Fest 2023 官方活动页：<https://www.unrealengine.com/events/unreal-fest-2023>
- Unreal Engine 官方播放列表页：<https://www.youtube.com/@UnrealEngine/playlists>
- Unreal Fest Gold Coast 2024：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gZK_Dt-WymqP4UrAr6pdHZ4>
- Unreal Fest Prague 2024：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gZZJOmMfAsli_S2vx4mVSs7>
- Unreal Fest Seattle 2024：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gb0rxbHfn2t--7jO2gADVNT>
- Unreal Fest Orlando 2025：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gbSPueZMAf0gacwmuVBU3hO>
- Unreal Fest Bali 2025：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gZy2nANAiZTd72TBvLyurkl>
- Unreal Fest Stockholm 2025：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gar0LXDZDcg8vivvEwW86ZJ>
