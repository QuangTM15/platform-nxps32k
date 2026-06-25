"""
EduFramework integration for NXP S32K144 / MaaZEDU.

EduFramework extends the bare-metal base layer by adding:

- public EduFramework headers
- prebuilt EduFramework static library

The package is expected to have this layout:

framework-eduframework-s32k144/
├── package.json
└── eduframework/
    ├── include/
    └── lib/
        └── libeduframework.a
"""

from os.path import isdir, isfile, join

from SCons.Script import Import

Import("env")

FRAMEWORK_PACKAGE_NAME = "framework-eduframework-s32k144"
FRAMEWORK_DIR_NAME = "eduframework"
FRAMEWORK_LIB_NAME = "eduframework"

platform = env.PioPlatform()

framework_package_dir = platform.get_package_dir(FRAMEWORK_PACKAGE_NAME)

if not framework_package_dir:
    raise RuntimeError("%s package was not found" % FRAMEWORK_PACKAGE_NAME)

framework_root_dir = join(framework_package_dir, FRAMEWORK_DIR_NAME)
framework_include_dir = join(framework_root_dir, "include")
framework_lib_dir = join(framework_root_dir, "lib")
framework_lib_file = join(framework_lib_dir, "lib%s.a" % FRAMEWORK_LIB_NAME)

if not isdir(framework_include_dir):
    raise RuntimeError("EduFramework include directory was not found: %s" % framework_include_dir)

if not isfile(framework_lib_file):
    raise RuntimeError("EduFramework static library was not found: %s" % framework_lib_file)

env.Append(
    CPPPATH=[
        framework_include_dir
    ],
    LIBPATH=[
        framework_lib_dir
    ],
    LIBS=[
        FRAMEWORK_LIB_NAME
    ]
)