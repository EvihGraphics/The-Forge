# Inside Unreal 2024—2026 课程内容总结

> 官方播放列表：<https://www.youtube.com/playlist?list=PLZlv_N0_O1gbggHiwNP2JBXGeD2h12tbB>
>
> 整理口径：
>
> - 仅收录 **2024—2026 年首发的 Inside Unreal 正式节目**。
> - **排除全部 Unreal Fest 课程**，同时不混入 State of Unreal、UEFN Build Along、独立预告片和纯宣传短片。
> - YouTube 播放列表及 Epic 论坛会因置顶、补档或话题更新而重新显示旧节目；本文按视频的实际首发年份归类，避免把早期节目误算到 2026。
> - 2026 年统计截至 **2026-06-17**，属于半年度快照。
> - 表格沿用 Unreal Fest Bali 版格式：**序号｜课程｜主要内容｜课题关联度**。
>
> “课题关联度”针对当前研究方向：**UE 渲染管线、Niagara、环境 VFX、体积天气、沙暴／雪崩、性能优化与插件扩展**。  
> **高**＝可直接进入当前学习或开发路线；**中高**＝能迁移关键方法；**中**＝提供工程背景；**低**＝关联较间接。

---

# 2024

2024 年的 Inside Unreal 以 **UE 5.4／5.5 功能落地、Motion Matching、编辑器效率、大世界协作和独立游戏生产案例**为主。相比 Unreal Fest 的正式演讲，Inside Unreal 更偏现场演示、项目拆解和问答。

## 一、引擎版本、动画与编辑器工作流

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**The Strategy of Technical Documentation Writing – Q&A**](https://www.youtube.com/watch?v=mpcJTi1wOo8)<br><sub>2024-03-01</sub> | 从受众、信息层级、示例、版本维护和检索方式出发，讨论怎样编写真正可执行的技术文档。重点不是单纯“写说明”，而是把复杂系统拆成稳定接口、前置条件、流程和故障排查入口。 | **中高**：适合给自定义体积渲染器、Niagara 模块和渲染插件建立可维护文档。 |
| 2 | [**Powering 2D Animation in Unreal Engine with Odyssey**](https://www.youtube.com/watch?v=yqqjboBnm28)<br><sub>2024-04-05</sub> | Praxinos 展示 Odyssey 的二维绘制、时间轴、动画资产及其与 UE 三维场景的协作方式，可将二维图形直接用于场景、材质和混合型动画生产。 | 中：对 VFX Flipbook、手绘遮罩和二维／三维混合效果有辅助价值。 |
| 3 | [**Unreal Engine 5.4 Feature Overview**](https://www.youtube.com/watch?v=RuYHfVKfrMM)<br><sub>2024-05-03</sub> | 汇总 UE 5.4 的核心更新，包括 Motion Matching、动画工具、Nanite Tessellation、渲染性能、PCG 和编辑器工作流，并通过现场项目展示新功能之间的连接方式。 | **高**：Nanite Tessellation、PCG 与性能更新均可进入沙地／雪地和环境系统路线。 |
| 4 | [**Game Animation Sample Walkthrough**](https://www.youtube.com/watch?v=mhVp_cC9MLc)<br><sub>2024-06-14</sub> | 拆解 Game Animation Sample 中 500 余段动画、Pose Search Schema、数据库、轨迹查询和 Motion Matching 运行逻辑，并演示替换角色和导入自有动画。 | 低：动画方向价值很高，但与当前环境渲染课题关系较弱。 |
| 5 | [**Quick Ways for Speeding Up Workflow**](https://www.youtube.com/watch?v=Ks1NZMu_lC0)<br><sub>2024-06-28</sub> | 通过编辑器快捷操作、批处理、Editor Utility、资产管理和自动化减少重复劳动，强调缩短“修改—验证—回退”循环。 | **高**：适合搭建天气效果参数批处理、测试关卡和性能回归工具。 |
| 6 | [**Optimal Collision & Avoiding Common Collision Mistakes**](https://www.youtube.com/watch?v=XRHzrFZNb1A)<br><sub>2024-07-26</sub> | 系统梳理 Collision Channel、Preset、Object／Trace Response、Simple／Complex Collision 及常见误配置，并解释碰撞查询对 CPU、物理和 Gameplay 的影响。 | **中高**：可用于 Niagara 粒子、流体代理和雪崩交互对象的碰撞分层设计。 |
| 7 | [**Demoing 5.4 Animation & Rigging Updates**](https://www.youtube.com/watch?v=t1YxqE6rtZc)<br><sub>2024-08-23</sub> | 演示 Control Rig、Modular Rigging、约束、变形器和 Sequencer 中的动画编辑更新，说明如何减少 DCC 往返。 | 低：对环境方向间接，但可用于受风角色附件和交互动画。 |
| 8 | [**Unreal Engine 5.5 Feature Overview & Demo**](https://www.youtube.com/watch?v=JIDiw1f-9bk)<br><sub>2024-11-15</sub> | 汇总 UE 5.5 的动画创作、渲染、PCG、移动端和开发迭代能力；包括实验性 MegaLights 等新系统的定位与演示。 | **高**：适合跟踪多灯、PCG、移动端回退和引擎版本迁移。 |

## 二、世界构建、技术设计与 Gameplay 系统

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**The Psychology of Environment Art Pt. 2**](https://www.youtube.com/watch?v=ib1zPzIp-oM)<br><sub>2024-02-02</sub> | 从构图、对比、尺度、视觉层级和环境叙事分析玩家如何读取场景，并说明如何用空间与光照引导注意力和行动路线。 | **中高**：有助于控制沙暴／雪暴中的可读性、危险区轮廓和视觉引导。 |
| 2 | [**Project Titan Kickoff & Q&A**](https://www.youtube.com/watch?v=zvL30u1Q8wM)<br><sub>2024-03-29</sub> | 启动多人协作开放世界 Art Jam，介绍底层地图、World Partition、PCG、资产约束、协作规则和提交方式，展示小型核心团队怎样为大规模参与者建立内容框架。 | **高**：可参考大世界天气测试场、区域化效果和多人内容规范。 |
| 3 | [**World Building with Project Titan**](https://www.youtube.com/watch?v=0tNg7RIQ9cM)<br><sub>2024-Q2</sub> | 在 Project Titan 中现场展示地形、世界分区、PCG、环境资产组织及可编辑程序化流程，强调生成结果与人工覆盖之间的平衡。 | **高**：可用于构建沙丘、雪场、植被响应区和天气影响分区。 |
| 4 | [**Tackling Flight Movement & Mechanics with EV2**](https://www.youtube.com/watch?v=G7RRO26G3Bc)<br><sub>2024-04-12</sub> | 拆解飞行移动、输入、相机、加速度和 Gameplay 反馈，展示如何使用蓝图快速迭代非标准移动模型。 | 中：可用于穿越风暴、空中采样和体积效果验证角色。 |
| 5 | [**Gameplay-Conscious Level Design**](https://www.youtube.com/watch?v=UK9SRMPRgoE)<br><sub>2024-09-06</sub> | 强调关卡几何必须与移动、战斗、视线和玩家决策共同设计，通过编辑器实例展示空间结构如何制造 Gameplay 机会。 | 中：对天气遮挡、能见度变化和交互区域布局有参考价值。 |
| 6 | [**Exploring Project Titan**](https://www.youtube.com/watch?v=dw6Ha48HGdc)<br><sub>2024-12</sub> | 回顾完成后的 Project Titan 开放世界，浏览参与者内容，并复盘 World Partition、PCG、协作规范和公开样例工程的结构。 | **高**：适合作为大型环境测试工程和数据组织参考。 |

## 三、独立游戏、项目案例与社区

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Creating Dirge – An Indie Perspective**](https://www.youtube.com/watch?v=Bo6fdKTNJuU)<br><sub>2024-01-19</sub> | NonNobis Games 介绍小团队开发非对称多人恐怖游戏《Dirge》的过程，覆盖原型、网络玩法、资产取舍、团队分工及有限资源下的 UE 工作流。 | 中：主要价值是小团队如何控制项目范围和技术风险。 |
| 2 | [**Building a World Solo with UE5’s Tool Suite – The Axis Unseen**](https://www.youtube.com/watch?v=Y9XYdsz4AD8)<br><sub>2024-02-16</sub> | 单人开发者拆解如何借助 Nanite、Lumen、World Partition 和现成工具构建大型开放世界恐怖游戏，并说明哪些系统值得自动化、哪些内容需要手工把控。 | **中高**：对个人或小团队搭建环境技术 Demo 很有现实参考。 |
| 3 | [**Learning from Games: Dirge**](https://www.youtube.com/watch?v=VTJHnoQBmDY)<br><sub>2024-03-15</sub> | 通过实际游玩和项目讨论分析《Dirge》的系统组合、玩家反馈、多人节奏及实现取舍，属于“从可运行游戏反推技术与设计”的案例。 | 低。 |
| 4 | [**SMITE 2**](https://www.youtube.com/playlist?list=PLZlv_N0_O1gbggHiwNP2JBXGeD2h12tbB)<br><sub>2024-08-29</sub> | Titan Forge 讨论从长期维护的 UE3 项目迁移到 UE5 时，如何重建 MOBA 的 Gameplay、内容工具、表现和跨平台管线，而不是机械搬运旧工程。 | **中高**：适合研究长期项目的引擎迁移、数据重构和兼容策略。 |
| 5 | [**Introducing Epic for Indies**](https://www.youtube.com/watch?v=aBny4i6IKkU)<br><sub>2024-10-17</sub> | 介绍 Epic 为独立团队提供的 Unreal Engine、Fab、Epic Games Store、教育资源和社区支持入口。 | 低。 |
| 6 | [**An Inside Look at FPS Green Hawk Platoon**](https://www.youtube.com/watch?v=3NvCx9I3gCg)<br><sub>2024-10-25</sub> | 拆解微缩士兵题材 FPS 的制作，涉及 Lumen、Control Rig、Niagara、比例感、战斗表现和小团队内容生产。 | **中高**：Niagara、环境比例与特效整合值得参考。 |
| 7 | [**A Spooky Special: Playing the UE5 Title ‘The Axis Unseen’**](https://www.youtube.com/watch?v=-WneEusHWW8)<br><sub>2024-11-01</sub> | 通过正式版本游玩回顾单人开放世界项目从工具选型到落地的效果，并讨论开发阶段的取舍与问题。 | 中。 |
| 8 | [**Year in Review 2024**](https://www.youtube.com/watch?v=XknflWJivgg)<br><sub>2024-12-12</sub> | 回顾全年 Unreal Engine、UEFN、Fab、样例工程和社区项目，适合快速建立 2024 年生态变化时间线。 | 中。 |

---

# 2025

2025 年的节目重点转向 **PSO／Shader Stutter、移动端性能、PCG 扩展、生产级样例工程、动画系统更新和真实项目世界构建**。这一年的技术课程对项目落地比单纯功能展示更有价值。

## 一、性能、引擎版本与运行时系统

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Game Animation Sample Project 5.5 Updates**](https://www.youtube.com/watch?v=3RlnclPo-3U)<br><sub>2025-01-17</sub> | 展示 Game Animation Sample 在 UE 5.5 中的 Motion Matching、数据库、轨迹和 Locomotion 更新，并解释旧项目迁移时需要调整的资产和逻辑。 | 低。 |
| 2 | [**Game Engines & Shader Stuttering: Unreal Engine’s Solution**](https://www.youtube.com/watch?v=0PbexYu01co)<br><sub>2025-02-07</sub> | 从首次遇到材质或 Pipeline State 时的卡顿原因讲起，解释 Shader Compilation、PSO、PSO Precaching、打包数据和验证流程，重点是如何把偶发运行时卡顿转成可预测的构建阶段工作。 | **高**：自定义体积材质、Niagara Shader 和渲染插件都必须处理 Shader／PSO 预热。 |
| 3 | [**New Template Sneak Peek**](https://www.youtube.com/playlist?list=PLZlv_N0_O1gbggHiwNP2JBXGeD2h12tbB)<br><sub>2025-04-04</sub> | 预览面向 UE 5.6 更新的 First Person、Third Person、Top Down 等模板，展示更清晰的项目结构、可选变体和学习入口。 | 中：适合构建干净的沙暴／雪崩实验工程基线。 |
| 4 | [**Maximize and Steady Performance in UE Mobile Development**](https://www.youtube.com/watch?v=Ax4cXRAtZTw)<br><sub>2025-05-23</sub> | 讨论移动端 CPU／GPU Profiling、温控降频、帧率稳定、Device Profile、内存、材质和渲染分级。重点不是短时间峰值 FPS，而是长时间运行时的稳定表现。 | **高**：与移动端 Niagara、屏幕覆盖型沙尘和体积回退方案直接相关。 |
| 5 | [**Unreal Engine 5.7 Feature Overview**](https://www.youtube.com/playlist?list=PLZlv_N0_O1gbggHiwNP2JBXGeD2h12tbB)<br><sub>2025-11-14</sub> | 汇总 UE 5.7 的渲染、动画、PCG、MetaHuman 和编辑器效率更新，并通过 Demo 说明功能成熟度与使用边界。 | **高**：用于判断项目升级、渲染功能变化和插件维护成本。 |
| 6 | [**GASP – It’s Mover! Game Animation Sample Updates + Q&A**](https://www.youtube.com/watch?v=i27eY7LbRzc)<br><sub>2025-12-04</sub> | 将 Game Animation Sample 与 Mover 框架连接，讨论移动模拟、角色表现和动画查询之间的数据流及后续路线。 | 低。 |

## 二、环境、PCG、关卡与样例工程

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**The Psychology of Environment Art Pt. 3**](https://www.youtube.com/watch?v=6z2v24mkWBs)<br><sub>2025-01-31</sub> | 延续环境心理学系列，进一步讨论空间预期、情绪、构图、颜色和可读性如何影响玩家对场景的理解。 | **中高**：适合设计极端天气下的视线层级和危险感。 |
| 2 | [**Exploring the Dark Ruins Megascans Sample**](https://www.youtube.com/watch?v=l3VFQk0aog8)<br><sub>2025-02-28</sub> | 拆解 Dark Ruins 样例中的 Megascans 资产、模块化搭建、材质、灯光、性能和场景组织，展示高质量环境如何保持可编辑性。 | **高**：可作为沙暴／雪暴环境测试关卡的资产与材质组织参考。 |
| 3 | [**Gameplay Focused Level Design**](https://www.youtube.com/watch?v=hfTrMOLVXoI)<br><sub>2025-03-14</sub> | 通过实例说明怎样围绕玩家能力、遭遇、视线和节奏设计关卡，而不是先做景观再强行植入玩法。 | 中。 |
| 4 | [**Taking PCG to the Extreme with the PCGEx Plugin**](https://forums.unrealengine.com/t/inside-unreal-taking-pcg-to-the-extreme-with-the-pcgex-plugin/2479952)<br><sub>2025-05-02</sub> | 介绍开源 PCGEx 对 UE PCG 的扩展，包括图结构、邻接关系、路径处理、空间分析和大量生产便利节点。它把 PCG 从“散布资产”推进到复杂结构生成和关系计算。 | **高**：适合生成沙丘带、雪崩路径、天气区域图和环境交互网络。 |
| 5 | [**Exploring the Parrot Game Sample**](https://www.youtube.com/watch?v=G8GrRA-8BHA)<br><sub>2025-06-27</sub> | 拆解面向 Unity 开发者的 2.5D 平台游戏样例，覆盖输入、Gameplay Framework、UI、项目设置和常见概念映射。 | 低。 |
| 6 | [**Making the World of ‘Echoes of the End’**](https://www.youtube.com/watch?v=CFSjV7fBS9g)<br><sub>2025-06-28</sub> | Myrkur Games 介绍如何采集冰岛环境、重制 Megascans 表面、组织自然场景并结合 Chaos 破坏，展示真实地貌参考到可运行世界的完整转换。 | **高**：与雪地、岩石、风化、破坏和环境真实性高度相关。 |
| 7 | [**Exploring the Sports Broadcast: Motion Design Sample**](https://www.youtube.com/watch?v=YiMh6bEebIs)<br><sub>2025-09</sub> | 浏览包含 40 余个案例的 Motion Design 样例，涉及 Cloner、Transition Logic、Remote Control、Rundown 和实时播出图形。 | 中：其参数驱动、状态切换与远程控制思路可迁移到天气控制台。 |
| 8 | [**Exploring the A-COM Sample Projects**](https://www.youtube.com/watch?v=nVuDBmDjmlI)<br><sub>2025-11-21</sub> | 讲解 Animation 与 Animatic 样例中的 Sequencer、Control Rig、镜头、布局和引擎内影视工作流。 | 低。 |

## 三、游戏案例、制作方法与社区活动

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Creating Classic MMO Mechanics in UE: Ruins of Tearyn**](https://www.youtube.com/watch?v=9YOA3cONmGI)<br><sub>2025-03-28</sub> | 展示经典 MMO 式角色、物品、技能、任务、UI 和数据驱动 Gameplay 的实现方式，讨论小团队如何组织大量相互关联的系统。 | 低。 |
| 2 | [**Developing Adventure Horror in Unreal: Senscape’s ‘ASYLUM’**](https://www.youtube.com/watch?v=slWqXcV84pY)<br><sub>2025-04-11</sub> | 复盘长期开发的第一人称冒险恐怖游戏，覆盖环境、交互、叙事工具、内容迭代和技术债。 | 中：主要价值是长期项目管理和环境叙事。 |
| 3 | [**Mega Stack ‘O’ Jam: Game Jam Kickoff**](https://www.youtube.com/playlist?list=PLZlv_N0_O1gbggHiwNP2JBXGeD2h12tbB)<br><sub>2025-08-15</sub> | 介绍以 Stack-O-Bot 为基础的关卡设计 Jam、规则、资源和快速原型方法。 | 低。 |
| 4 | [**From Clay to Code: Exploring ‘The Midnight Walk’**](https://www.youtube.com/watch?v=BFoPdQlTYaY)<br><sub>2025-10-03</sub> | MoonHood 展示实体黏土模型、摄影测量、动画和 UE 场景之间的混合管线，说明如何保留手工材质感而实现实时交互。 | 中：对扫描资产、非标准材质与独特环境风格有启发。 |
| 5 | [**Mega Stack ‘O’ Jam Winners Announcement**](https://www.youtube.com/playlist?list=PLZlv_N0_O1gbggHiwNP2JBXGeD2h12tbB)<br><sub>2025-10-10</sub> | 展示获奖项目并分析短周期关卡原型的创意和完成度。 | 低。 |
| 6 | [**2025 Epic MegaJam Theme Reveal & Kickoff**](https://www.unrealengine.com/news/epic-megajam-2025)<br><sub>2025-10-17</sub> | 公布年度 MegaJam 主题、规则、资源和评审维度。 | 低。 |
| 7 | [**Building & Sustaining Communities**](https://www.youtube.com/watch?v=rBHDzraSoyA)<br><sub>2025</sub> | 讨论开发者社区的建立、维护、沟通、反馈与长期运营。 | 低。 |
| 8 | [**Year in Review 2025**](https://www.youtube.com/watch?v=LUlxPB5-sno)<br><sub>2025-12-12</sub> | 回顾全年 Unreal Engine、样例工程、独立游戏、Fab 和社区的重要节点。 | 中。 |

---

# 2026

> 2026 年内容截至 **2026-06-17**。这一阶段 Inside Unreal 明显加强了 **本地性能自动化、可选内容与 Mod 管线、Niagara 生产样例、移动端 MegaLights 和团队工具化**。

## 一、性能工程、工具与可扩展内容管线

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Automated Performance Profiling for Local Workflows**](https://www.youtube.com/watch?v=bfkbwXVMtn8)<br><sub>2026</sub> | 将固定场景、运行命令、性能采样、结果保存和版本对比组织成本地自动化流程，使开发者在提交前就能发现帧时间、内存或线程成本回退。 | **高**：非常适合给沙暴／雪崩不同质量档建立可重复性能基线。 |
| 2 | [**Programming for Team Productivity: 15 Practical Tips**](https://www.youtube.com/watch?v=b8BwKI_MKHM)<br><sub>2026</sub> | 汇总资产验证器、设计时节点、可视化辅助对象、编辑器窗口、通知、错误预防和主动反馈等工程技巧，核心目标是把隐性规则转成工具和即时提示。 | **高**：可用于体积资产验证、Niagara 预算检查和渲染参数防错。 |
| 3 | [**Evolving Localization Workflows in UE5 with Custom Tooling**](https://www.youtube.com/watch?v=LsccqWA7yQg)<br><sub>2026</sub> | 展示如何围绕 UE 本地化系统增加自定义编辑器工具、上下文管理、批处理和验证，从而降低大量文本和多语言版本维护成本。 | 中：主题不同，但其数据验证和工具扩展方法可迁移。 |
| 4 | [**Creating Optional Content for Unreal Games**](https://www.youtube.com/watch?v=xqlS6iNGhL8)<br><sub>2026-05-01</sub> | 讲解如何使用 Primary Asset Label、插件化内容、Data Asset 和构建脚本把基础游戏与可选包／DLC 分离，并处理 Cook、安装和运行时发现。 | **中高**：适合把高端体积资产、平台专属材质和可选天气包拆分部署。 |
| 5 | [**Supporting Runtime Mods in UE5: A Complete Pipeline for Developers and Modders**](https://www.youtube.com/watch?v=rHF3VdA_0Js)<br><sub>2026-05-15</sub> | 建立从 Mod Authoring、独立构建、打包、加载、版本兼容到发布的完整运行时 Mod 管线，并说明开发者工程与 Modder 工具包的边界。 | 中：对插件化环境系统和外部内容加载有参考价值。 |
| 6 | [**Exploring Four Methods for Handling Projectiles in UE5**](https://www.youtube.com/watch?v=aq8SfHcclbU)<br><sub>2026-06</sub> | 对比基于 Actor Movement、物理模拟、Trace 和其他运行时方案的弹体实现，分析碰撞精度、网络、数量规模和性能差异。 | 中：可借鉴高速粒子／碎屑的碰撞与表示分层。 |

## 二、Niagara、渲染、动画与音频

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Exploring TechAudioTools Content**](https://www.youtube.com/watch?v=Xlwnu0FtCvY)<br><sub>2026</sub> | 介绍 MetaSound Input Migrator、Metadata Editor、SoundGenerator、Viewmodel 和可复用 UMG 工具，展示如何把复杂音频工作流封装为编辑器产品。 | 中：工具架构值得参考，技术主题与渲染间接。 |
| 2 | [**Exploring the New Cascadeur Update with Unreal Live Link**](https://www.youtube.com/watch?v=jhXtL3CB4Bo)<br><sub>2026</sub> | 展示 Cascadeur 2026.1 与 Unreal Live Link 的实时动画传输、物理辅助姿态和快速迭代流程。 | 低。 |
| 3 | [**Runtime Synthesis & Sequencing with Metron**](https://www.youtube.com/watch?v=VSbyaYp1ICg)<br><sub>2026</sub> | 介绍运行时音乐合成、节奏序列、程序化编排及其与 MetaSounds／Gameplay 数据的连接。 | 低。 |
| 4 | [**Black Eye 2.0: Reimagining Camera Workflows for Gameplay & Cinematics in Unreal**](https://www.youtube.com/watch?v=MZjl2YlvMnw)<br><sub>2026-05</sub> | 讲解统一 Gameplay 与 Cinematic Camera 的管理方式，包括优先级、Blend Matrix、轨道／自由视角、碰撞、阻尼、Trigger Volume、CineCameraActor 和 Play 状态保存。 | 中：适合建立天气效果测试镜头、自动拍摄和可重复对比。 |
| 5 | [**Exploring the Niagara Examples Pack**](https://www.youtube.com/watch?v=NxKz7Pnww54)<br><sub>2026-06-03</sub> | 深入官方 Niagara Examples Pack：50 余个系统、Blueprint 集成、Niagara Data Channel、Effect Type、Scalability、Lightweight Emitter、碰撞材质、爆炸／冲击／投射物、雾与 Sparse Volume Texture，并展示大世界坐标和曝光测试。 | **高**：是 2024—2026 Inside Unreal 中与你当前 Niagara／环境 VFX 路线最直接的一课。 |
| 6 | [**MegaLights on Mobile: Pipe Dream or Reality? How Arm & Sumo Digital Made It Possible**](https://www.youtube.com/watch?v=XG5W2Ei_J0Q)<br><sub>2026-06-12</sub> | Arm 与 Sumo Digital 以 Neural Dawn Demo 展示 UE 5.6.1 中的首批移动端 MegaLights 实践：大量动态灯替代烘焙 Lightmap，并结合移动光追、神经超分与帧生成，在功耗和帧预算内维持画质。 | **高**：对移动端天气照明、动态体积光源和高低配分层具有直接价值。 |

## 三、学习、独立项目与社区

| 序号 | 课程 | 主要内容 | 课题关联度 |
|---:|---|---|---|
| 1 | [**Avoid Tutorial Hell – Utilizing Resources to Learn Unreal Engine in 2026**](https://www.youtube.com/watch?v=IeQpGHTBOkQ)<br><sub>2026</sub> | 讨论如何从被动观看教程转向项目驱动学习，合理组合官方文档、样例工程、源码、论坛和小型验证任务，并通过明确目标和复盘形成自己的知识结构。 | **中高**：非常适合当前“课程索引 → 源码验证 → 模块化实验”的学习方式。 |
| 2 | [**Epic MegaJam 2025 Winners Announcement**](https://www.youtube.com/playlist?list=PLZlv_N0_O1gbggHiwNP2JBXGeD2h12tbB)<br><sub>2026-03</sub> | 公布 2025 Epic MegaJam 获奖作品并展示短周期项目中的设计和技术亮点。 | 低。 |
| 3 | [**Timberline Studio on the Making of ‘Beastro’**](https://www.youtube.com/watch?v=1YN3GRv1o1g)<br><sub>2026-04-16</sub> | Indie Games Week 节目，介绍小团队开发风格化动作 RPG／经营混合项目时的美术、玩法、内容管线和项目范围控制。 | 低。 |

---

# 三年趋势对比

| 维度 | 2024 | 2025 | 2026（截至 6 月） |
|---|---|---|---|
| 引擎功能 | UE 5.4／5.5 新功能现场演示 | UE 5.7、模板和样例工程生产化 | 围绕已有功能补齐工具、测试和部署链路 |
| Niagara／VFX | 以项目案例和新版本能力为主 | 与移动性能、PCG 和环境生产间接结合 | 官方 Niagara Examples Pack 开始提供完整生产参考 |
| 性能 | 编辑器效率、碰撞和版本能力 | PSO Stutter、移动端稳帧 | 自动性能回归、移动 MegaLights、规模化验证 |
| 世界构建 | Project Titan、World Partition、PCG | Dark Ruins、PCGEx、Echoes of the End | 更偏内容模块化、可选包和 Runtime Mod |
| 工程成熟度 | 学会使用功能 | 把功能放进真实项目 | 把规则固化成验证、自动化和可部署产品 |

---

# 针对当前方向的优先观看列表

| 优先级 | 课程 | 主要价值 | 课题关联度 |
|---:|---|---|---|
| S | **Exploring the Niagara Examples Pack** | 官方生产级 Niagara 系统、Data Channel、Scalability、Lightweight Emitter、SVT 和大世界测试。 | **高** |
| S | **Automated Performance Profiling for Local Workflows** | 为不同天气状态建立固定场景和自动性能回归。 | **高** |
| S | **Game Engines & Shader Stuttering: Unreal Engine’s Solution** | 自定义 Shader、Niagara 和渲染插件上线前必须解决的 PSO／预热问题。 | **高** |
| S | **MegaLights on Mobile** | 研究动态多灯、移动光追和跨平台天气照明的最新工程案例。 | **高** |
| A | **Maximize and Steady Performance in UE Mobile Development** | 移动端长时间稳帧、温控、内存和画质分级。 | **高** |
| A | **Taking PCG to the Extreme with PCGEx** | 生成天气区域、雪崩路径和环境关系图。 | **高** |
| A | **Project Titan Kickoff / World Building / Exploring** | 大世界协作、World Partition、PCG 和内容规范的完整链路。 | **高** |
| A | **Exploring the Dark Ruins Megascans Sample** | 高质量环境样例的材质、灯光、资产和性能组织。 | **高** |
| A | **Making the World of Echoes of the End** | 真实地貌、扫描资产、自然环境和 Chaos 破坏。 | **高** |
| A | **Programming for Team Productivity** | 把体积资产约束和性能预算变成自动验证工具。 | **高** |
| B | **UE 5.4／5.5／5.7 Feature Overview** | 建立版本能力与迁移成本时间线。 | **高** |
| B | **Quick Ways for Speeding Up Workflow** | 降低实验和内容批处理成本。 | **高** |

---

# 总结

Inside Unreal 与 Unreal Fest 的价值不同：

- **Unreal Fest** 更适合系统学习一项技术或 Shipping 项目的完整复盘；
- **Inside Unreal** 更适合观察 Epic 如何现场使用功能、拆解样例工程、回答工程细节，以及新功能在后续版本中怎样逐步成熟。

对沙暴／雪崩与 UE 渲染开发而言，2024—2026 最重要的 Inside Unreal 主线不是单独的体积算法，而是：

> **Niagara 生产样例 → PCG／大世界环境组织 → Shader／PSO 稳定性 → 自动性能回归 → 移动端稳帧与 MegaLights → 插件化和可选内容部署。**

它们正好补足 GDC 与 SIGGRAPH 课程中较少展开的 **UE 实际工程接入层**。
