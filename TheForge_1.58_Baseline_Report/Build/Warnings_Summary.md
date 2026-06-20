# Warnings Summary

Generated: 2026-06-20T01:48:41+08:00

- Final accepted compile/link pass used VS2022/v143, SDK 10.0.22621.0, toolchain patch, and CL=/wd4189.
- 0 MSVC compiler warnings were counted in the final accepted compile/link log after /wd4189.
- ISPC performance warning text appears in earlier adaptation logs and is preserved in Build/.
- Runtime logs commonly contain non-fatal warnings such as UI fallback font IDs, ReloadServer port reuse, and graphics config fields unknown to this fixed release.
- Post-build warnings/errors remain around optional script/font/cameraPath resource copies for 36_AlgorithmsAndContainers and 39_ParticleSystem. These did not prevent 39_ParticleSystem runtime capture.
