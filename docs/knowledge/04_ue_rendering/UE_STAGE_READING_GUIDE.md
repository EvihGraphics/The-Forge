# UE Rendering Stage Reading Guide（Future）

当前 The Forge 阶段默认不读取。

相关资料：

- `sources/markdown/UE5_渲染管线教程.md`
- `sources/pdf/在UE5外部模块中扩展复杂渲染管线实践.pdf`
- `sources/transcripts/Lessons_From_A_Plugin_Developer.txt`

## 未来阅读目标

- 理解 Game Thread、Render Thread、Scene、View、RDG、RHI 的关系；
- 判断插件公共扩展点的能力边界；
- 把 The Forge 冻结契约重建为 UE 数据流；
- 不把 AVBOIT 写入 GBuffer；
- 第一阶段只做独立 Flipbook Player，不提前接 Niagara。

Single Volume PDF 只提供宏观插件化、线程分离、渲染代理和产品化经验；不得使用或寻找其源码。
