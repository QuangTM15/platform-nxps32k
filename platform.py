"""
NXP S32K PlatformIO platform definition.
"""

import sys
from os.path import isfile, join

from platformio.managers.platform import PlatformBase


class Nxps32kPlatform(PlatformBase):
    def configure_default_packages(self, variables, targets):
        super().configure_default_packages(variables, targets)

    def _get_gdb_executable(self):
        toolchain_dir = self.get_package_dir("toolchain-gccarmnoneeabi")
        gdb_name = "arm-none-eabi-gdb.exe" if sys.platform.startswith("win") else "arm-none-eabi-gdb"

        if toolchain_dir:
            gdb_path = join(toolchain_dir, "bin", gdb_name)

            if isfile(gdb_path):
                return gdb_path

        return gdb_name

    def configure_debug_session(self, debug_config):
        gdb_path = self._get_gdb_executable()

        debug_config.build_data["gdb_path"] = gdb_path

        return debug_config