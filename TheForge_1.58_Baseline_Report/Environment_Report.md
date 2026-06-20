# Environment Report

Generated: 2026-06-20T01:45:35+08:00

## System
- OS: Microsoft Windows 11 Pro 10.0.26200, build 26200
- CPU: Intel(R) Core(TM) i9-14900KF, 24 cores, 32 logical processors
- System Memory: 63.82 GB
- Disk Free Space: C: 130.5 GB, D: 103.7 GB, E: 56.7 GB at audit time
- Primary GPU: NVIDIA GeForce RTX 4060 Ti
- GPU Driver Version: WMI 32.0.15.9186 / NVIDIA package 591.86
- Display: NVIDIA output reports 2560 x 1440 desktop; Forge DX12 swapchains captured at 1920 x 1080
- Windows DPI: Forge logs report monitor DPI scale 1.25, 1.25
- Remote/Virtual Display: OrayIddDriver device present; screenshots captured with PrintWindow to avoid remote lock-screen capture
- Independent GPU Used: YES, NVIDIA RTX 4060 Ti selected by DX12 logs

## Toolchain
- Git: git version 2.48.1.windows.1
- Git LFS: git-lfs/3.6.1
- CMake: 3.30.5
- Python: 3.13.2
- Visual Studio 2019: Community 16.11.47 installed; C++ targets incomplete for this run
- Visual Studio 2022: Community 17.13.0 installed and used for final build
- Visual Studio 2026: installed but not used
- MSVC Toolsets: VS2019 v142 directory present; final compiler was VS2022 v143/MSVC 14.38 (_MSC_VER 1938)
- Windows SDK Required By Projects: 10.0.17763.0, not installed
- Windows SDK Used For Adapted Build: 10.0.22621.0
- DirectX Shader Compiler: no system dxc in PATH; repo/bundled shader tooling used by project build

## Graphics API Status
- DX12 Support: YES, Direct3D12 initialized and selected NVIDIA GeForce RTX 4060 Ti
- Vulkan SDK Installed: NO system VULKAN_SDK environment variable; repo has bundled Vulkan-related files
- Vulkan Runtime Available: YES, C:\Windows\System32\vulkaninfo.exe, instance 1.4.321
- Vulkan-Capable Driver: YES, NVIDIA GeForce RTX 4060 Ti reports Vulkan API 1.4.325
- Vulkan Validation Layers: NO, VK_LAYER_KHRONOS_validation was not reported
- Vulkan Tested: NO
- Vulkan Result: NOT_TESTED
- Reason: primary baseline backend is DX12; Vulkan validation layer was missing and Vulkan was not selected for first-pass visual capture
- Primary Graphics Backend: DX12
- Fallback Backend: DX12
- Fallback Reason: Vulkan validation environment incomplete; DX12 was supported and stable for the baseline objective
- Cross-Backend Validation: NOT_PERFORMED

## Raw Evidence
- Environment_Raw_Log.txt
- dxdiag.txt
