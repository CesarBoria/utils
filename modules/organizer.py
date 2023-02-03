import os
import shutil
from typing import List

from main import crear_interfaz
from modules.interfaces.general_interface import BASE, selector
from modules.interfaces.organizer_interface import MOD_INTERFACE
from pathlib import Path

first_print = MOD_INTERFACE['HEAD']
dict_with_commands = {
    0: 'PATH',
    1: 'DO',
    2: 'ORDER',
    3: 'SHOW',
    4: 'HIDDEN',
    5: 'LINK'
}
home_path = os.path.expanduser('~')


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
    else: # TODO: Refactorizar a match/case en Python 3.11
        if str(_input[0]).lower() == 'path': # TODO: Comprobar que funciona
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
            if len(_input) > 2:
                print(f'Files will be ordered inside {_input[1]}')
            try:
                order_files(_input[1])
            except IndexError:
                order_files()
        elif str(_input[0]).lower() == 'show':
            if len(_input) > 3:
                print("Incorrect syntax, restarting the tool")
                mod_main()
            if 'all' in str(_input[1]).lower() or 'all' in str(_input[2]).lower():
                try:
                    show_info([item for item in _input[1:] if item.lower() != 'all'][0], all_info=True)
                except IndexError:
                    show_info()
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


def get_path(_input: str):
    try:
        if _input[0] in ('.', os.sep):
            os.chdir(_input)
        elif _input[0] == '~':
            new_path = os.path.join(home_path, _input[2:])
            os.chdir(new_path)
        else:
            child_path = os.path.join(os.getcwd(), _input)
            os.chdir(child_path)
        print(f'New path set to {os.getcwd()}')
    except FileNotFoundError:
        print('There is no directory with that name')


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


def order_files(_input: str = os.path.join(home_path, 'Desktop')): # TODO: Universalizar
    if _input == os.path.join(home_path, 'Desktop'):
        if not os.path.exists(os.path.join(home_path, 'Desktop')):
            _input = os.path.join(home_path, 'Escritorio')
    if _input.lower() == 'here':
        _input = os.getcwd()
    files = [file for file in os.listdir(_input) if os.path.isfile(os.path.join(_input, file))]
    extensions = {file[file.rfind('.') + 1:] for file in files}
    for ext in extensions:
        try:
            os.mkdir(os.path.join(_input, ext))
        except FileExistsError:
            pass
        print(f"Moved *.{ext} files")
        for file in files:
            if file.endswith(f".{ext}"):
                shutil.move(os.path.join(_input, file), os.path.join(_input, ext))


def show_info(_input: str = os.getcwd(), all_info=False):
    up = Path(_input).parent
    info_up = [folder for folder in os.listdir(up) if os.path.isdir(os.path.join(up, folder))]
    folders = [folder for folder in os.listdir(_input) if os.path.isdir(os.path.join(_input, folder))]
    files = [file for file in os.listdir(_input) if os.path.isfile(os.path.join(_input, file))]
    info_down = ""
    for folder in folders:
        down = [deep_folder for deep_folder in os.listdir(os.path.join(_input, folder)) if os.path.isdir(os.path.join(_input, folder, deep_folder))]
        info_down += f'{folder}: '
        if len(down) == 0:
            info_down += '[no directories found]'
        for directory in down:
            info_down += f'{directory} '
        info_down += f'\n'
    print(
f"""Path: {_input}

Directories upwards:
{" | ".join(info_up)}

Contents of {_input}:
-> Directories: {" ".join(folders)}
-> Files: {" ".join(files)}

Directories downwards:
{info_down}
""")


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
    if len(_input) > 1 and _input[1].lower() == 'info':
        print(MOD_INTERFACE[_input[0].upper()])
        mod_main()
    return _input


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_organizer.txt", verbose=True)
