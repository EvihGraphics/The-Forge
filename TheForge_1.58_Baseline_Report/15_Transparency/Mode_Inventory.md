# 15_Transparency Mode Inventory

Generated: 2026-06-20T01:49:08+08:00

| Mode | Present | Build | Runtime | API | Screenshot | Notes |
|---|---|---|---|---|---|---|
| Alpha blended | YES | PASS | NOT_VISUALLY_SWITCHED | DX12 | Attempt evidence only | Source enum, UI name, and Test_AlphaBlend.lua present. Regular-build UI automation did not produce accepted per-mode capture. |
| Weighted blended OIT | YES | PASS | NOT_VISUALLY_SWITCHED | DX12 | Attempt evidence only | Source enum, UI name, and Test_WeightedBlendedOIT.lua present. |
| Volition weighted blended OIT | YES | PASS | NOT_VISUALLY_SWITCHED | DX12 | Attempt evidence only | Source enum, UI name, and Test_WeightedBlendedOITVolition.lua present. |
| Phenomenological Transparency | YES | PASS | PASS_WITH_WARNINGS | DX12 | VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Default_01.png | This is the default gTransparencyType in the fixed commit and produced the accepted default screenshot. |
| Intel Adaptive OIT (AOIT) | YES | PASS | CAPABILITY_ENABLED_NOT_VISUALLY_SWITCHED | DX12 | Attempt evidence only | GPUCfg enables AOIT when RasterOrderViewSupport == 1; runtime log set EnableAOIT to 1. No accepted AOIT mode screenshot from regular build. |
