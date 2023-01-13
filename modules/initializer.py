from modules.interfaces.general_interface import BASE, selector
from modules.interfaces.initializer_interface import MOD_INTERFACE
import os


def mod_main():

    print(MOD_INTERFACE['HEAD'])
    name = input(MOD_INTERFACE['OPTION_1'])
    choice = input(MOD_INTERFACE['OPTION_2'])
    if choice.lower() in ('y', 'yes', 'si'):
        # Estructura Flask TODO: En modules, _flask_structure con copy/paste de https://github.com/realpython/flask-boilerplate
        out = input(BASE)
        selector(out)
    os.chdir('..')
    base_path = os.path.join(os.getcwd(), f'{name}')
    try:
        os.makedirs(os.path.join(base_path, 'source', f'{name.lower()}'))
        with open(os.path.join(base_path, 'source', '__init__.py'), 'w') as file:
            pass
        with open(os.path.join(base_path, 'source', f'{name.lower()}', '__init__.py'), 'w') as file:
            pass
    except OSError:
        print('The project is already in this directory. The tool will stop now')
        out = input(BASE)
        selector(out)
    with open(os.path.join(base_path, '.gitignore'), 'w') as file:
        pass # TODO: Template de .gitignore en modules, _gitignore_template de github
    with open(os.path.join(base_path, 'LICENSE.txt'), 'w') as file:
        pass # TODO
    with open(os.path.join(base_path, 'README.md'), 'w') as file:
        pass # TODO
    with open(os.path.join(base_path, 'requirements.txt'), 'w') as file:
        pass # TODO
    choice = input(MOD_INTERFACE['OPTION_3'])
    if choice.lower() in ('y', 'yes', 'si'):
        os.mkdir(os.path.join(base_path, 'tests'))
        with open(os.path.join(base_path, 'tests', '__init__.py'), 'w') as file:
            pass
        os.mkdir(os.path.join(base_path, 'docs'))
        with open(os.path.join(base_path, 'docs', '__init__.py'), 'w') as file:
            pass
    choice = input(MOD_INTERFACE['OPTION_4'])
    if choice.lower() in ('y', 'yes', 'si'):
        with open(os.path.join(base_path, 'setup.py'), 'w') as file:
            pass # TODO
        with open(os.path.join(base_path, 'setup.cfg'), 'w') as file:
            pass # TODO
        with open(os.path.join(base_path, 'MANIFEST.ini'), 'w') as file:
            pass # TODO
    choice = input(MOD_INTERFACE['OPTION_5'])
    if choice.lower() in ('y', 'yes', 'si'):
        choice = input(MOD_INTERFACE['OPTION_6'])
        if choice.lower() in ('data', 'analysis', 'analisis', 'datos', 'data analysis', 'analisis de datos'):
            with open(os.path.join(base_path, 'input.csv'), 'w') as file:
                pass # TODO
            with open(os.path.join(base_path, 'output.xlsx'), 'w') as file:
                pass # TODO
        elif choice.lower() in ('programming', 'web', 'wed development', 'development', 'dev', 'desarrollo', 'db', 'database', 'sql', 'nosql'):
            with open(os.path.join(base_path, 'database.db'), 'w') as file:
                pass # TODO
            with open(os.path.join(base_path, 'database.sql'), 'w') as file:
                pass # TODO
        else:
            print('None selected, no placeholderfiles will be created in ./data')
    choice = input(MOD_INTERFACE['OPTION_7'])
    if choice.lower() in ('y', 'yes', 'si'):
        os.mkdir(os.path.join(base_path, 'binaries'))
        # TODO Se crea Makefile y makefile.bat
    choice = input(MOD_INTERFACE['OPTION_8'])
    if choice.lower() in ('y', 'yes', 'si'):
        # TODO Se inizializa con git init
        pass
    print(f'\nSThe project has been created at {base_path}\n')
    out = input(BASE)
    selector(out)
