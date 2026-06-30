# Reference Baseline Audit

Reference Machine Environment:
- OS: Windows 11 Pro 10.0.26200
- Visual Studio Edition: VS2022 Community 17.13
- MSVC Toolset: v143 (_MSC_VER 1938)
- Windows SDK: 10.0.22621.0
- Primary Graphics API: DX12
- Resolution: 1920x1080
- GPU: NVIDIA GeForce RTX 4060 Ti
- Driver: WMI 32.0.15.9186 / NVIDIA 591.86

Unit Test Status from Reference:
- Total Discovered: 19
- Built: 19
- PASS/Accepted Screenshots: 18 (PNG format)
- Known Failures/Warnings: Post-build xcopy failures, UI script automation limits for 15_Transparency.

15_Transparency Status:
- Modes Present: Alpha blended, Weighted Blended OIT, Volition Weighted Blended OIT, Phenomenological Transparency, Intel Adaptive OIT.
- Reference Status: PASS_WITH_WARNINGS, incomplete per-mode visual capture due to automation limits.
- AOIT Capability: Enabled.
