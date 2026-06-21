param(
    [string]$ArtRoot = (Join-Path $PSScriptRoot "Art")
)

$ErrorActionPreference = "Stop"

$base = $ArtRoot
if (-Not (Test-Path "$base\UnitTestResources")) { New-Item -ItemType Junction -Path "$base\UnitTestResources" -Target "$base" -Force }
if (-Not (Test-Path "$base\Hair")) { New-Item -ItemType Junction -Path "$base\Hair" -Target "$base\Meshes\Hair" -Force }
if (-Not (Test-Path "$base\ZipFilesDds")) { New-Item -ItemType Junction -Path "$base\ZipFilesDds" -Target "$base\ZipFiles\dds" -Force }
if (-Not (Test-Path "$base\Textures\dds\PBR")) { New-Item -ItemType Directory -Path "$base\Textures\dds\PBR" -Force }
if (-Not (Test-Path "$base\PBR\dds")) { New-Item -ItemType Junction -Path "$base\PBR\dds" -Target "$base\Textures\dds\PBR" -Force }
if (-Not (Test-Path "$base\Textures\dds\Particles")) { New-Item -ItemType Directory -Path "$base\Textures\dds\Particles" -Force }
if (-Not (Test-Path "$base\Particles\Textures\dds")) { New-Item -ItemType Junction -Path "$base\Particles\Textures\dds" -Target "$base\Textures\dds\Particles" -Force }
if (-Not (Test-Path "$base\SanMiguel_3\Meshes")) { New-Item -ItemType Junction -Path "$base\SanMiguel_3\Meshes" -Target "$base\Meshes\SanMiguel_3" -Force }
if (-Not (Test-Path "$base\SanMiguel_3\Textures\dds")) { New-Item -ItemType Junction -Path "$base\SanMiguel_3\Textures\dds" -Target "$base\Textures\dds\SanMiguel_3" -Force }
if (-Not (Test-Path "$base\Animation\stormtrooper\riggedMesh.bin") -and (Test-Path "$base\Meshes\stormtrooper\riggedMesh.bin")) { New-Item -ItemType HardLink -Path "$base\Animation\stormtrooper\riggedMesh.bin" -Target "$base\Meshes\stormtrooper\riggedMesh.bin" -Force }
