

class Xserver:
    def __init__(self): ...

    class WindowManager:
        def __init__(self, *wm_names: str):
            self.window_managers: tuple = wm_names
            self._x11 = False
            self._wayland = False

        def config(self, config: str):
            ...

        @property
        def x11(self):
            self._x11 = True
            return self

        @property
        def wayland(self):
            self._wayland = True
            return self

    class DisplayManager:
        def __init__(self, dm_default: str, *dm_names: str):
            self.DM: str = dm_default
            self.other_DM: tuple = dm_names

