# AVBOIT vs Alpha Blend 颜色差异根因分析（最终版）

## 结论

差异的根因是 **AVBOIT 深度分辨率不足导致的跨层 Transmittance 泄漏**。

## 排除项

| 假设 | 排除理由 |
|------|----------|
| 颜色空间 (gamma) | 天空、山脉、无覆盖地板 diff=0，全局变换不存在 |
| 光照强度 | 两模式共用 `Shade()` + `LightUniformBlock`，不透明物体光照完美匹配 |
| 材质/纹理解析 | 独立透明面板像素 diff=0（red_panel、green_panel 等） |
| 算法理论极限 | 单层情况数学证明 AVBOIT=Alpha Blend，不是理论极限 |
| Composite 缺色 | Composite+Forward 组合对单层场景结果正确 |

## 确认的根因：跨层 Transmittance 泄漏

### 证据

`floor_panel_outside` (900, 470) — **孤立的单层地板面板**：

| | Mode 0 | Mode 5 | 差异 |
|---|--------|--------|------|
| BGR | [210, 17, 17] | [105, 17, 17] | **[105, 0, 0]** |

数学推导：
- alpha ≈ 0.914，extinction = 2.45
- Mode 0 正确：`B = 197*(1-0.914) + 211*0.914 = 210` ✅
- Mode 5：`B = 197*T_total + 211*T_front*0.914 = 105`
- 推出 `T_front ≈ 0.456`
- **对单层来说 T_front 应该是 1.0！**

### 机制

通过垂直扫描 x=900 列发现：
- y=350~420：有**竖直透明面板**覆盖（diff=[0,0,4~11]）
- y=430~450：纯地板（diff=0）
- y=460+：**地板面板**开始（diff=[105,0,0]）

这说明竖直面板（近处）和地板面板（远处）在 **相邻的 zIndex** 中。

```
Integration 扫描方向: z=0 (远) → z=63 (近)

zIndex:  0   1   2   3   4   5   ...  30  ...  63
         │   │   │   │   │   │        │        │
         └───┴───┴───┼───┴───┘        │        │
          地板面板区域  │                竖直面板    │
                      ▲
                  T_front 读取点
                  已包含左侧所有 extinction！
```

当地板面板在 `zIndex=5` 时，Forward Pass 读取 `T_front = T[4]`。
如果**另一个透明物体**（更远但在同一区域的深度 slice）的 extinction 在 `z=0~4` 中，就会被计入 `T_front`，导致地板面板的颜色被错误衰减。

### 为什么单层竖直面板不受影响

竖直面板在 `zIndex=30~50`（近处），前方没有其他透明物体。`T_front = T[29] = 1.0`（z=0~29 没有 extinction 积累），所以颜色计算完全正确。

### 为什么地板面板受影响

地板面板在远处（`zIndex ≈ 0~5`），但在 3D 场景中，它们的上方可能有竖直面板，且透视投影将竖直面板**也投射到**地板面板的屏幕像素上。这些竖直面板的近端可能映射到与地板面板相近的 zIndex。

## 修复方向

1. **增加 volumeDepth**（64 → 128/256）：减少深度量化误差
2. **优化深度映射函数**：使用分段线性映射而非对数映射，集中分辨率在透明物体密集的深度范围
3. **改用颜色积累方法**：在 Splat 阶段同时积累 `color × alpha`，在 Composite 阶段一次性输出 `accumulatedColor + background × T_total`，避免逐片段的 T_front 查找

## 当前指标

| 指标 | 数值 |
|------|------|
| Full Image SSIM | 0.9546 |
| Full Image MAE | 0.0284 |
| Full Image PSNR | 20.79 dB |
| 差异方向 | 87.7% Mode 5 更暗 |

![差异热力图](C:/Users/l3d/.gemini/antigravity/brain/2d7a8410-35e6-47b7-a5c1-e3ce6a91a404/Diff_Mode0_Mode5.png)
