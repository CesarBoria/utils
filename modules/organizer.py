import os
import sys
from main import crear_interfaz
from modules.interfaces.general_interface import BASE, selector
from modules.interfaces.organizer_interface import MOD_INTERFACE

first_print = MOD_INTERFACE['HEAD']
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
    try:
        _input = parse_tool()
    except TypeError:
        choice = input("The command doesn't exist or is not recognized. Exit?\n >>> ")
        if choice.lower() in ('y', 'yes', 'si', 'back', 'return', 'go back'):
            crear_interfaz()
        else:
            mod_main()
    except Exception as e:
        print('There was an error, please, copy and paste this following text and send it to my github, thanks :)')
        print(repr(e))
        out = input(BASE)
        selector(out)
    else: # TODO: Refactorizar a match/case en Python 3.11
        if str(_input[0]).lower() == 'path': # TODO: Crear docs para PATH
            if len(_input) == 1:
                print(f'Current path: {os.getcwd()}')
            elif len(_input) == 2:
                get_path(_input[1])
            else:
                what_is_this = _input[3:]
                print(f'{what_is_this} not recognized, only {_input[1]} will be used')
        elif str(_input[0]).lower() == 'do':
            pass
        elif str(_input[0]).lower() == 'order':
            pass
        elif str(_input[0]).lower() == 'show':
            pass
        elif str(_input[0]).lower() == 'hidden':
            pass
        elif str(_input[0]).lower() == 'link':
            pass
        else:
            print('Command not recognized, please try again') # TODO: Es necesario?
        mod_main()


def get_path(_input: str) -> str:
    if _input[0] in ('..', os.sep):
        os.chdir(_input)
        print(f'New path set to {os.getcwd()}')
    elif _input[0] == '~':
        os.chdir(os.environ['HOME'])
        print(f'New path set to HOME ({os.getcwd()})')
    else:
        new_path = os.path.join(os.getcwd(), _input)
        os.chdir(new_path)
        print(f'New path set to {new_path}')
    return os.getcwd()


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
    _input = input(" >>> ").split()
    if _input[0] in [str(option) for option in tuple(dict_with_commands.keys())]:
        _input[0] = dict_with_commands[int(_input[0])]
    return _input


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_organizer.txt", verbose=True)
