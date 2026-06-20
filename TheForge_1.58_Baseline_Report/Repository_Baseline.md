# Repository Baseline

Generated: 2026-06-20T01:45:35+08:00

Fork Remote: https://github.com/EvihGraphics/The-Forge
Upstream Project: https://github.com/ConfettiFX/The-Forge
Baseline Commit: 2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d
Expected Release: 1.58
Expected Date: 2024-06-17

## Verification
- HEAD verification: PASS
- Actual HEAD: 2f47c1445ca0062998b4b4aa81e5346a4c3cdf2d
- Branch State: detached HEAD
- Submodule verification: PASS, no .gitmodules entries in this fixed checkout
- Working tree clean: NO
- Git LFS complete: YES, no missing LFS object was reported by git lfs status

## Remotes
```text
origin	https://github.com/EvihGraphics/The-Forge.git (fetch)
origin	https://github.com/EvihGraphics/The-Forge.git (push)
upstream	https://github.com/ConfettiFX/The-Forge.git (fetch)
upstream	https://github.com/ConfettiFX/The-Forge.git (push)
```

## Working Tree Status
The non-clean state is documented and expected for this baseline: Art resources, generated build outputs, report artifacts, one toolchain patch, and a failed automation-output directory are present.

```text
 M Common_3/Application/Config.h
?? Art/
?? "Examples_3/Unit_Tests/PC Visual Studio 2019x64/"
```

## Git LFS Status
```text
On branch HEAD

Objects to be committed:


Objects not staged for commit:

	Common_3/Application/Config.h (Git: 9dfb5eb -> File: 758e763)

```

## Generated/Adapted Items
- Art/: output of the official PRE_BUILD asset download/extract flow plus documented resource junctions.
- Common_3/Application/Config.h: one compiler-version whitelist patch, saved in Patches/toolchain_vs2022_1938_whitelist.patch.
- Examples_3/Unit_Tests/PC Visual Studio 2019x64/: stray generated output from a documented failed AUTOMATED_TESTING rebuild attempt; not used as baseline output.
