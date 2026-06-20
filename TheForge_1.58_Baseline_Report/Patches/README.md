# Patches

A source patch was required because the current machine does not have a complete VS2019/v142 C++ build toolchain, while The Forge 1.58 explicitly whitelists _MSC_VER == 1929.

## toolchain_vs2022_1938_whitelist.patch
- Type: toolchain adaptation
- File: Common_3/Application/Config.h
- Purpose: allow the installed VS2022 MSVC 14.38 compiler (_MSC_VER == 1938) to compile the baseline after original VS2019/v142 and VS2022/v143 unpatched attempts were preserved as failures.
- Scope: one compiler-version guard line only.
- Rendering/Shader/OIT changes: none.
