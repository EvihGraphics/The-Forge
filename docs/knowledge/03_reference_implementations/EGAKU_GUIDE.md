# EgakuRenderPipeline Guide

代码快照：`sources/reference_code/EgakuRenderPipeline.zip`

仓库链接：

- https://github.com/chiikusa/EgakuRenderPipeline
- https://github.com/chiikusa/CloudAndOcean2

## 角色

Egaku 是可运行的 Unity 行为参考，用于理解 AVBOIT 原型的 Pass、资源和 Shader 数据流；它不是最终算法规范。

## 使用原则

- 先记录仓库 commit、分支和工作区状态；
- 关注输入输出契约和中间缓冲，不做逐行翻译；
- 比较 Egaku 与正式 AVBOIT PDF 的差异；
- The Forge 实现以正式 PDF、Ground Truth 和实际测试为最终裁决。

## 已知风险

上传快照中的 AVBOIT 代码可能包含未提交工作区内容。Agent 不得用远程 clone 结果无条件覆盖上传快照。
