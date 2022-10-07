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

BOOTLOADERS = ["grub"]

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


class Conf:
    def __init__(self, config):
        self.bootloader = None
        self.network = None
        self.pkg = None
        self.service = None
        self.sound = None
        self.user = None
        self.wm = None
        self.parser(config)

    @property
    def wm(self):
        return self._wm

    @wm.setter
    def wm(self, data):
        self._wm = data

    @property
    def bootloader(self):
        return self._bootloader

    @bootloader.setter
    def bootloader(self, data):
        self._bootloader = data
        ...

    def parser(self):
        ...


class Initializer:
    """
    get data and check operating system and send config data to OS builder
    """

    def __init__(self, config_file=None, mode="build"):
        self.config_file = Conf(config_file)
        self.mode = mode
        self.os = os.popen("uname -n").read().strip()
        if mode == 'test':
            self.check_module()
        if mode == 'build':
            ...  # TODO: write build func

    def signal(self, signal_path):
        ...

    def send_signal_module(self):
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
                            if isinstance(v, list):
                                for bootloader in v:
                                    import_module(f"bootloader.{bootloader}")
                            else:
                                import_module(f"bootloader.{v}")
                        except ModuleNotFoundError:
                            raise BootloaderNotSupported(
                                f"{v} not supported.\n please open issue https://github.com/MahanBi/Oravel/issues"
                            )
        else:
            raise OSNotSupported(
                f"{self.os} not supported. \n please open issue https://github.com/MahanBi/Oravel/issues"
            )
