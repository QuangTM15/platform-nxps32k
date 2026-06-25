"""
EduFramework integration for NXP S32K144 / MaaZEDU.

This framework extends the bare-metal base layer by adding:

- EduFramework public headers
- EduFramework static library: libeduframework.a

The low-level startup, system file and linker script are still provided
by the platform-level bare-metal support.
"""

from os.path import join
from SCons.Script import Import

Import("env")

platform = env.PioPlatform()

framework_dir = platform.get_package_dir("framework-eduframework-s32k144")

if not framework_dir:
    raise RuntimeError("framework-eduframework-s32k144 package was not found")

eduframework_dir = join(framework_dir, "eduframework")
include_dir = join(eduframework_dir, "include")
lib_dir = join(eduframework_dir, "lib")

env.Append(
    CPPPATH=[
        include_dir
    ],
    LIBPATH=[
        lib_dir
    ],
    LIBS=[
        "eduframework"
    ]
)