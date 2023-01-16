from modules.interfaces.general_interface import BASE, selector
from modules.interfaces.organizer_interface import MOD_INTERFACE, Explorer


def mod_main():
    print(MOD_INTERFACE['HEAD'])

    out = input(BASE)
    selector(out)
