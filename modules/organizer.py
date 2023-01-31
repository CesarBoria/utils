import os
import sys
import shutil
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
    except Exception as e:
        print('There was an error, please, copy and paste this following text and send it to my github, thanks :)')
        print(repr(e))
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
            try:
                if _input[1].lower() in ('cp', 'copy', '-c'):
                    do_command('copy', _input[2:])
                elif _input[1].lower() in ('mv', 'move', '-m'):
                    do_command('move', _input[2:])
                elif _input[1].lower() in ('cp', 'remove', 'delete', 'del', '-d'):
                    do_command('remove', _input[2:])
                else:
                    raise ValueError
            except Exception as e:
                print(repr(e))
                print("Incorrect syntax, restarting the tool")
                mod_main()
        elif str(_input[0]).lower() == 'order':
            pass
        elif str(_input[0]).lower() == 'show':
            pass
        elif str(_input[0]).lower() == 'hidden':
            pass
        elif str(_input[0]).lower() == 'link':
            pass
        else:
            print('Command not recognized. Introduce START to restart the tool') # TODO: Es necesario?
            out = input(BASE)
            if out.lower() in ('start', 'restart', 're', 'again'):
                mod_main()
            selector(out)
            first_print = MOD_INTERFACE['HEAD']
        mod_main()


def get_path(_input: str) -> str:
    try:
        if _input[0] in ('.', os.sep):
            os.chdir(_input)
            print(f'New path set to {os.getcwd()}')
        elif _input[0] == '~':
            new_path = _input.replace('~', os.environ['HOME'])
            os.chdir(new_path)
            print(f'New path set to {os.getcwd()}')
        else:
            new_path = os.path.join(os.getcwd(), _input)
            os.chdir(new_path)
            print(f'New path set to {new_path}')
        return os.getcwd()
    except FileNotFoundError:
        print('There is no directory with that name')
        mod_main()


def do_command(command: str, _input: list[str]):
    start = _input[0]
    if command == 'remove':
        if input(f'WARNING: You are about to remove {start}, are you sure?') in ('yes', 'y', 'si'):
            if os.path.isfile(start):
                os.remove(start)
            else:
                shutil.rmtree(start)
            print(f'{start} has been removed')
        return None
    try:
        end = _input[1]
    except IndexError:
        end = os.getcwd()
    if command == 'copy':
        if os.path.isfile(start):
            new_path = shutil.copy2(start, end)
            print(f'{start} file copied to {new_path}')
        else:
            new_path = shutil.copytree(start, end)
            print(f'{start} directory copied to {new_path}')
    if command == 'move':
        new_path = shutil.move(start, end)
        print(f'{start} moved to {new_path}')


def order_files(_input: str = '') -> str:
    pass


def show_info(_input: str = '') -> str:
    pass


def show_hidden(_input: str = '') -> str:
    pass


def make_links(_input: str = '') -> str:
    pass


def parse_tool() -> list[str]:
    global first_print
    _input = input(" >>> ").split()
    if _input[0].lower() in ('exit', 'back', 'return', 'go back', 'menu', 'start', 'restart'):
        first_print = MOD_INTERFACE['HEAD']
        crear_interfaz()
    if _input[0] in [str(option) for option in tuple(dict_with_commands.keys())]:
        _input[0] = dict_with_commands[int(_input[0])]
    if _input[1].lower():
        print(MOD_INTERFACE[_input[0].upper()])
        mod_main()
    return _input


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_organizer.txt", verbose=True)
