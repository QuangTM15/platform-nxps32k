"""
Main PlatformIO builder for the NXP S32K platform.

Responsibilities:

- configure ARM GCC toolchain
- configure common compiler/linker flags
- build user application
- generate Intel HEX image
- provide J-Link upload target

Framework scripts are loaded automatically by PlatformIO according to
the selected framework in platform.json.
"""

import os
import sys
from os.path import join

from SCons.Script import Default, DefaultEnvironment


env = DefaultEnvironment()
board = env.BoardConfig()
platform = env.PioPlatform()

platform_dir = platform.get_dir()

PROGNAME = "firmware"
LINKER_SCRIPT = join(platform_dir, "linker", "S32K144_64_flash.ld")


def get_jlink_executable():
    jlink_dir = platform.get_package_dir("tool-jlink")
    executable = "JLink.exe" if sys.platform.startswith("win") else "JLinkExe"

    if jlink_dir and os.path.isdir(jlink_dir):
        executable = join(jlink_dir, executable)

    return executable


def configure_program_name():
    env.Replace(PROGNAME=PROGNAME)


def configure_toolchain():
    cpu = board.get("build.cpu")

    env.Replace(
        AR="arm-none-eabi-ar",
        AS="arm-none-eabi-as",
        CC="arm-none-eabi-gcc",
        CXX="arm-none-eabi-g++",
        OBJCOPY="arm-none-eabi-objcopy",
        SIZETOOL="arm-none-eabi-size",

        CCFLAGS=[
            "-mcpu=%s" % cpu,
            "-mthumb",
            "-mfloat-abi=hard",
            "-mfpu=fpv4-sp-d16",
            "-fshort-enums",
            "-fno-jump-tables",
            "-funsigned-char",
            "-funsigned-bitfields",
            "-ffunction-sections",
            "-fdata-sections",
            "-fno-common",
            "-O1",
            "-g"
        ],

        CPPDEFINES=[
            "CPU_S32K144HFT0VLLT",
            "CPU_S32K144",
            "START_FROM_FLASH"
        ],

        LINKFLAGS=[
            "-mcpu=%s" % cpu,
            "-mthumb",
            "-mfloat-abi=hard",
            "-mfpu=fpv4-sp-d16",
            "-Wl,--gc-sections",
            "-specs=nano.specs",
            "-specs=nosys.specs",
            "-T%s" % LINKER_SCRIPT
        ]
    )


def build_program_images():
    target_elf = env.BuildProgram()

    target_hex = env.Command(
        join("$BUILD_DIR", "${PROGNAME}.hex"),
        target_elf,
        "$OBJCOPY -O ihex $SOURCE $TARGET"
    )

    return target_elf, target_hex


def create_jlink_script(target, source, env):
    hex_path = source[0].get_abspath().replace("\\", "/")
    upload_script = env.subst(join("$BUILD_DIR", "upload.jlink"))

    with open(upload_script, "w") as script:
        script.write("r\n")
        script.write("loadfile %s\n" % hex_path)
        script.write("r\n")
        script.write("g\n")
        script.write("q\n")


def configure_upload_target(target_hex):
    upload_script = join("$BUILD_DIR", "upload.jlink")

    env.Replace(
        UPLOADER=get_jlink_executable(),
        UPLOADERFLAGS=[
            "-device",
            board.get("debug.jlink_device"),
            "-if",
            "SWD",
            "-speed",
            "4000",
            "-CommanderScript",
            upload_script
        ],
        UPLOADCMD="$UPLOADER $UPLOADERFLAGS"
    )

    upload_actions = [
        env.VerboseAction(create_jlink_script, "Generating J-Link script..."),
        env.VerboseAction("$UPLOADCMD", "Uploading firmware...")
    ]

    env.AddPlatformTarget(
        "upload",
        target_hex,
        upload_actions,
        "Upload firmware using J-Link"
    )


configure_program_name()
configure_toolchain()

target_elf, target_hex = build_program_images()
configure_upload_target(target_hex)

Default([target_elf, target_hex])