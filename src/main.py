import os
import platform
import subprocess
from exceptions import (
    OSNotSupported,
    PackageManagerNotSupported,
    ServiceManagerNotSupported,
    BootloaderNotSupported,
)
from importlib import import_module

BOOTLOADERS = ["grub", "lilo"]

OS_OPTION = {
    "arch": {
        "pkg": ["pacman", "yay", "pamac"],
        "service": "systemd",
        "bootloader": BOOTLOADERS,
    },
    "manjaro": {
        "pkg": ["pacman", "yay", "pamac"],
        "service": "systemd",
        "bootloader": BOOTLOADERS,
    },
    "debian": {
        "pkg": ["apt"],
        "service": "systemd",
        "bootloader": BOOTLOADERS,
    },
}


class Initializer:
    """
    get data and check operating system and send config data to OS builder
    """

    def __init__(self, cmd=None, config_file=None, mode="build"):
        self.cmd = cmd
        self.config_file = config_file
        self.mode = mode
        self.os = os.popen("uname -n").read().strip()
        self.check_module()

    def signal(self, signal_path):
        ...

    def check_module(self):

        if detail := OS_OPTION.get(self.os, None):

            for k, v in detail.items():  # TODO: add config reader

                match k:

                    case "pkg":

                        try:

                            for option in v:
                                import_module(f"pkg.{option}")

                        except ModuleNotFoundError:
                            raise PackageManagerNotSupported(
                                f"{option} not supported.\n please open issue https://github.com/MahanBi/Oravel/issues"
                            )

                    case "service":

                        try:
                            import_module(f"service.{v}")

                        except ModuleNotFoundError:
                            raise ServiceManagerNotSupported(
                                f"{v} not supported.\n please open issue https://github.com/MahanBi/Oravel/issues"
                            )

                    case "bootloader":

                        try:
                            import_module(f"bootloader.{v}")

                        except ModuleNotFoundError:
                            raise BootloaderNotSupported(
                                f"{v} not supported.\n please open issue https://github.com/MahanBi/Oravel/issues"
                            )

        else:
            raise OSNotSupported(
                f"{self.os} not supported. \n please open issue https://github.com/MahanBi/Oravel/issues"
            )
