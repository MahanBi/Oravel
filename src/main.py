import os
import platform
import subprocess

OS_DETAIL = {
    'arch': {
        'pkg': ['pacman', 'yay', 'pamac'],
        'service': 'systemd',

    },
    'debian': {
        'pkg': ['apt']
    }
}


class Initializer:
    """
    get data and check operating system and send config data to OS builder
    """

    def __init__(self, cmd, config_file, mode='build'):
        self.cmd = cmd
        self.config_file = config_file
        self.mode = mode
        self.os = os.popen('uname -n', mode='r')
        self.setup_runners()

    def signal(self, signal_path):
        ...

    def setup_runners(self):
        if detail := OS_DETAIL.get(self.os, None):
            for k, v in detail:
                self.signal(f'{k}.{v}')
            else:
                ...
        else:
            ...