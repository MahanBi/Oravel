from . import Pkg, Xserver, User, i3, qtile, xfce

Main = (
    Pkg.Packages(
        "vim",
        "neovim",
        "neofetch",
    ),
    Xserver.WindowManager(
        i3,
        xfce,
        qtile
    ).x11,  # or wayland .wayland
    Xserver.DisplayManager(
        "sddm",
        "emptty"
    ),
    Xserver.Drivers(
        "amdgpu",
        "nvidia"
    ),


)

Config = (

)