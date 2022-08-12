

class Xserver:
    def __init__(self): ...

    class WindowManager:
        def __init__(self): ...

        def config(self, config: str):
            ...

        def x11(self) -> None:
            return self

        def wayland(self) -> None:
            return self

    class DisplayManager:
        def __init__(self): ...
