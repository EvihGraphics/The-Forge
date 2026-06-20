# Dependency Preparation Report

Generated: 2026-06-20T01:47:25+08:00

## Official Flow
- Command: PRE_BUILD.bat
- Working Directory: D:\HTC\avboit\The-Forge
- Log: Dependency_Logs/PRE_BUILD_Log.txt
- Result: The wrapper timed out while the download was still active, but the background Art.zip download completed.

## Completion Steps
- Command: Tools/7z.exe x Art.zip -y
- Log: Dependency_Logs/PRE_BUILD_Unzip_Log.txt
- Result: PASS, Art.zip extracted and removed as PRE_BUILD.bat normally does.

## Resource Path Adaptations
The extracted Art package did not contain the exact UnitTestResources layout expected by several VS project post-build steps. Documented junctions/hardlinks were created and logged in Dependency_Logs/Resource_Path_Adaptation_Log.txt.

Created mappings include:
- Art/UnitTestResources -> Art
- Art/Hair -> Art/Meshes/Hair
- Art/ZipFilesDds -> Art/ZipFiles/dds
- Art/PBR/dds -> Art/Textures/dds/PBR
- Art/Particles/Textures/dds -> Art/Textures/dds/Particles
- Art/SanMiguel_3/Meshes -> Art/Meshes/SanMiguel_3
- Art/SanMiguel_3/Textures/dds -> Art/Textures/dds/SanMiguel_3
- Art/Animation/stormtrooper/riggedMesh.bin hardlink -> Art/Meshes/stormtrooper/riggedMesh.bin

## Remaining Missing Optional Inputs
- Art/cameraPath.bin was not present in the downloaded package; Art/cameraPath.txt exists.
- Art/UnitTestResources/Scripts was not present.
- Some post-build font/script copy commands still report zero-file or missing-file conditions.

## Patch Status
No resource adaptation changed renderer source, shader source, transparent rendering code, or Unit Test behavior. One toolchain source patch is documented separately in Patches/.
