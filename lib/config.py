from . import Pkg, Xserver

Main = (
    Pkg.Packages(
        "vim",
        "neovim",
        "neofetch",
    ),
    Xserver.WindowManager(
        "i3",
        "qtile"
    ).x11,  # or wayland .wayland
    Xserver.DisplayManager(
        "sddm",
        "emptty"
    )
)

Config = (

)