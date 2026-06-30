# AVBOIT Decision Record & Ground Truth Math

## 目标
建立 15_Transparency 中新增加的 AVBOIT 透明算法接口，并为其建立 100% 可推导的 RGB 三面片数学真值 (Ground Truth)，用于在实现不同透明管线时有一个不受环境、光照和分辨率干扰的硬性验证基准。

## 契约：RGB 三面片基准 (RGB Quads Ground Truth)
为了精确判断透明度算法是否具有“Order Independent (与顺序无关)”的能力，以及其透射率累加是否在数学上收敛于真实物理定律，我们引入三个互相平行的纯色面片：
*   **近景 (Front)**: 红色  = (1.0, 0.0, 0.0)$，透明度 $\alpha_R = 0.5$，放置于  = -5.0$
*   **中景 (Middle)**: 绿色  = (0.0, 1.0, 0.0)$，透明度 $\alpha_G = 0.5$，放置于  = -10.0$
*   **远景 (Back)**: 蓝色  = (0.0, 0.0, 1.0)$，透明度 $\alpha_B = 0.5$，放置于  = -15.0$
*   **背景 (Skybox/Clear Color)**: 假设为 {bg}$

### 理想光学方程推导 (Back-to-Front Alpha Blending)
采用前向遮挡与透射率 (Transmittance  = 1 - \alpha$) 模型：
1.  **蓝色面片 (远景)** 与背景混合：
     C_{outB} = C_B \cdot \alpha_B + C_{bg} \cdot (1 - \alpha_B) = (0, 0, 1) \cdot 0.5 + C_{bg} \cdot 0.5
2.  **绿色面片 (中景)** 与其混合：
     C_{outG} = C_G \cdot \alpha_G + C_{outB} \cdot (1 - \alpha_G) = (0, 1, 0) \cdot 0.5 + ((0, 0, 0.5) + C_{bg} \cdot 0.5) \cdot 0.5
     C_{outG} = (0, 0.5, 0.25) + C_{bg} \cdot 0.25
3.  **红色面片 (近景)** 与其混合：
     C_{outR} = C_R \cdot \alpha_R + C_{outG} \cdot (1 - \alpha_R) = (1, 0, 0) \cdot 0.5 + ((0, 0.5, 0.25) + C_{bg} \cdot 0.25) \cdot 0.5
     C_{outR} = (0.5, 0.25, 0.125) + C_{bg} \cdot 0.125

### 预期结果像素值 (Ground Truth 色彩)
若背景近似全黑 ({bg} \approx 0$)，最终屏幕中心像素颜色应趋近于：
*   **Red (R)**: .500$ (即 127 或 128 (8-bit))
*   **Green (G)**: .250$ (即 63 或 64 (8-bit))
*   **Blue (B)**: .125$ (即 31 或 32 (8-bit))
*   **结论**：
gb(128, 64, 32) 是无论面片以何种顺序提交（6 种 draw order permutations），AVBOIT 等具备 OIT 能力的算法必须输出的绝对不变色相和亮度基准。

## 契约：AVBOIT 管线插入
*   **枚举位置**：将 AVBOIT 作为 TRANSPARENCY_TYPE_ADAPTIVE_VOXEL_BASED_OIT 加入到 TransparencyType，序号 5。
*   **函数占位**：创建 AdaptiveVoxelBasedOITPass 函数。它应当：
    1.  如果开启，执行 AVBOIT Clear Pass
    2.  利用现有的 gTransparentDrawCalls 执行 AVBOIT Build Pass，将片元注入自适应体素/节点结构。
    3.  执行 AVBOIT Resolve Pass，依据上面算出的透射率公式，将结果组合到全屏四边形。
*   **数据共享**：直接读取 gTransparentObjectInfoUniformData 和已有的材质颜色缓冲。不影响已有的 WeightedBlendedOrderIndependentTransparencyPass 等等。

## 结论与承诺
本决策确保了后续 AVBOIT 的增量开发拥有：
1. 可见的正确性真值。
2. 不会侵入或破坏 The Forge 其他后端的隔离框架。
