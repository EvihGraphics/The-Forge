# AVBOIT PDF Reading Guide

原始资料：`sources/pdf/AVBOIT_SIG2025_MDROBOT-final.pdf`

## 阅读目的

不是逐页翻译，而是提取：

- 游戏透明问题定义；
- Ground Truth 与近似算法的关系；
- VBOIT 基本数据流；
- AVBOIT 自适应深度表示；
- Mono、Total Extinction 与 RGB Transmittance；
- 质量、性能、内存与内容约束；
- 官方已知限制和未来方向。

## 当前项目重点

AVBOIT 服务于 glass、VFX meshes、VFX cards 的稳定透明合成。它不是粒子系统，也不是天气模拟器。工业案例研究将它定位为沙暴／雪粉／烟雾近景透明合成层。

## Agent 阅读问题

1. 正确 Alpha 合成的参考定义是什么？
2. 为什么 WBOIT 在远距离烟雾与玻璃组合中可能丢失遮挡？
3. AVBOIT 的预通路、积分、透明绘制和 Resolve 各自解决什么？
4. 自适应深度结构如何利用 Z 稀疏性？
5. 官方性能数字建立在什么分辨率和内容条件下？
6. 哪些结论是项目相关的，哪些不能直接迁移？
