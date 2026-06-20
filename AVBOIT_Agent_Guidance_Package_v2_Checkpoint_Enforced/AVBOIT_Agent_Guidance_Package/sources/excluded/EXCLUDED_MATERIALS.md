# Excluded Materials

## SingleVolume.zip

状态：明确排除，不打包。

原因：

- 用户明确要求排除 SingleVolume 源码；
- 其算法目标是体积 Ray March，而非 AVBOIT；
- 防止 Agent 复制无关实现或形成错误耦合；
- 对应演讲 PDF 可以保留，用于宏观插件工程学习。

Agent 不得通过外部下载重新补充该源码。


Checkpoint 归档中也禁止引用、复制或生成 SingleVolume 源码级分析。
