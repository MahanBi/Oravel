from bootloader import GRUB
from network import Network
from pkg import Install

main = {

    "bootloader": GRUB(
        settings={

        },
    ),

    "network": Network(

    ),

    "pkg": Install(

    ),

}
