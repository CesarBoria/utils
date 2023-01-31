import os
from modules.interfaces.general_interface import BASE, selector
from modules.interfaces.organizer_interface import MOD_INTERFACE

first_print = print(MOD_INTERFACE['HEAD'])
dict_with_commands = {
    0: 'PATH',
    1: 'DO',
    2: 'ORDER',
    3: 'SHOW',
    4: 'HIDDEN',
    5: 'LINK'
}
def mod_main():
    global first_print
    print(first_print)
    first_print = ''
    _input = parse_tool()
    out = input(BASE)
    selector(out)


def get_path(_input: str = '') -> str:
    if _input == '' or _input is None:
        return os.getcwd()
    else:
        return os.path.join(os.getcwd(), _input)


def do_command(_input: str = '') -> str:
    pass


def order_files(_input: str = '') -> str:
    pass


def show_info(_input: str = '') -> str:
    pass


def show_hidden(_input: str = '') -> str:
    pass


def make_links(_input: str = '') -> str:
    pass


def parse_tool() -> list[str]:
    _input = input().split()
    # TODO: Terminar funcion de parseado
    return _input


if __name__ == '__main__':
    import doctest
    #doctest.testfile("../tests/test_organizer.txt", verbose=True)
    print(parse_tool())
