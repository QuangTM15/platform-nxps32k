"""
Bare-metal framework integration for NXP S32K144.

This script adds the platform-owned low-level support files required by
all S32K144 applications:

- startup file
- system file
- S32K144 device header include path

The linker script is configured by the main builder to avoid duplicate
-T linker script options.
"""

from os.path import join

from SCons.Script import Import

Import("env")

platform = env.PioPlatform()
platform_dir = platform.get_dir()

SYSTEM_DIR = join(platform_dir, "system")

env.Append(
    CPPPATH=[
        SYSTEM_DIR
    ]
)

env.BuildSources(
    join("$BUILD_DIR", "system"),
    SYSTEM_DIR
)