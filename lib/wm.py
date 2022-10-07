# WMs
i3 = "i3"
qtile = "qtile"
xfce = "xfce"
icewm = "icewm"
twm = "twm"
xmonad = "xmonad"
mate = "mate"
gnome = "gnome"
plasma = "plasma"

# DMs
sddm = "sddm"
gdm = "gdm"


class Xserver:

    def __init__(self):
        ...


class WindowManager:

    def __init__(self, wm_default: str, *wm_names: str):
        """
        :param wm_default:
        :param wm_names:
        """
        self.default = wm_default
        self.others: tuple = wm_names
        self._x11 = False
        self._wayland = False

    def config(self, config: str):
        ...

    @property
    def x11(self):
        """
        :return:
        """
        self._x11 = True
        return self

    @property
    def wayland(self):
        self._wayland = True
        return self


class DisplayManager:
    def __init__(self, dm_default: str, *dm_names: str):
        self.default: str = dm_default
        self.others: tuple = dm_names


class Drivers:

    def __init__(self, *drivers: str):
        self.drivers = drivers


class Layout:
    ...
