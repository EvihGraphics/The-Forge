# AVBOIT Phase 1: Visual and Performance Archive
**Machine**: HIVE_4090x2
**Timestamp**: 2026-06-20
**Configuration**: Release / x64 / DX12

## 概要 (Summary)
本次测试展示了 The Forge 1.58 中现有的5种透明算法以及新加入的 AVBOIT（Mode 5，当前为占位符）。测试场中已注入绝对物理顺序的 RGB Ground Truth 三面片（分别位于 Z=-5, -10, -15）。所有性能开销数据和视觉结果均通过 Microprofiler 在对应的截图中留底，确保在同一硬件环境和分辨率下的公平对比。

## 视觉与性能对比矩阵 (Visual & Performance Comparison Matrix)

| Mode | Backend | Visual Status | Performance (GPU Time) | Screenshot Path |
|------|---------|---------------|------------------------|-----------------|
| 0 | Sorted Alpha (Ground Truth) | 绝对正确。正确的红绿蓝色彩衰减，逼近理论真值 gb(128, 64, 32)。 | 见图内 Microprofiler | ./VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_0.png |
| 1 | WBOIT | 深度层次不准确，存在颜色泛化。 | 见图内 Microprofiler | ./VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_1.png |
| 2 | WBOIT Volition | 针对不透明度做了调整，但深层排序依然有失真。 | 见图内 Microprofiler | ./VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_2.png |
| 3 | Phenomenological PT | 折射与颜色物理正确性增强，但在面片严格排序下不如 Ground Truth 锐利。 | 见图内 Microprofiler | ./VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_3.png |
| 4 | Adaptive OIT (AOIT) | 视觉接近 Ground Truth，自适应节点进行了有效的透射率合并。 | 见图内 Microprofiler | ./VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_4.png |
| 5 | AVBOIT (Placeholder) | 仅显示不透明物体。由于 Build 与 Resolve 仍是空管线，不渲染面片，证明不侵入现有管线。 | 仅开销基础管线，极低。 | ./VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_5.png |

## 结语 (Conclusion)
所有视觉截屏与附带的实时 MicroProfiler 性能测量帧已静态绑定至 LocalVisualResults\HIVE_4090x2 目录中，为后续实现体素/节点结构（Virtual Block Based / Virtual Slice Based AVBOIT）确立了 100% 可重复验证的真值上限与性能耗时起点。
