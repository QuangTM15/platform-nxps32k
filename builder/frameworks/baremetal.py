"""
Bare-metal framework integration for NXP S32K144.

This script adds the platform-owned CMSIS/device support files required
by all S32K144 applications.
"""

from os.path import join

from SCons.Script import Import

Import("env")

platform = env.PioPlatform()
platform_dir = platform.get_dir()

CMSIS_DIR = join(platform_dir, "cmsis")

env.Append(
    CPPPATH=[
        CMSIS_DIR
    ]
)

env.BuildSources(
    join("$BUILD_DIR", "cmsis"),
    CMSIS_DIR
)