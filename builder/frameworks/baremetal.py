"""
Bare-metal framework integration for NXP S32K144.

This script provides the common low-level build inputs required by
a bare-metal S32K144 application:

- startup file
- system file
- device header include path
- linker script

EduFramework will reuse this same base layer and only add its own
public headers and static library.
"""

from os.path import join
from SCons.Script import Import

Import("env")

platform = env.PioPlatform()

platform_dir = platform.get_dir()
system_dir = join(platform_dir, "system")
linker_script = join(platform_dir, "linker", "S32K144_64_flash.ld")

env.Append(
    CPPPATH=[
        system_dir
    ]
)

env.BuildSources(
    join("$BUILD_DIR", "system"),
    system_dir
)