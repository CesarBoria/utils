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
        with open(os.path.join(base_path, 'source', 'main.py'), 'w') as file:
            pass # TODO: Make a sample main.py
    except OSError:
        print('The project is already in this directory. The tool will stop now')
        out = input(BASE)
        selector(out)
    with open(os.path.join(base_path, '.gitignore'), 'w') as file:
        pass # TODO: Template de .gitignore en modules, _gitignore_template de github
    with open(os.path.join(base_path, 'LICENSE.txt'), 'w') as file:
        pass # TODO: Use the github licenses
    with open(os.path.join(base_path, 'README.md'), 'w') as file:
        pass # TODO: Make a sample readme
    with open(os.path.join(base_path, 'requirements.txt'), 'w') as file:
        pass # TODO: ?? Just make a requirements (maybe automate)
    choice = input(MOD_INTERFACE['OPTION_3'])
    if choice.lower() in ('y', 'yes', 'si'):
        os.mkdir(os.path.join(base_path, 'tests'))
        with open(os.path.join(base_path, 'tests', '__init__.py'), 'w') as file:
            pass
        with open(os.path.join(base_path, 'tests', 'tests_basic.py'), 'w') as file:
            pass # TODO: import pytest y toda la historia
        with open(os.path.join(base_path, 'tests', 'tests_advanced.py'), 'w') as file:
            pass # TODO: import pytest y toda la historia
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
    os.mkdir(os.path.join(base_path, 'data'))
    choice = input(MOD_INTERFACE['OPTION_5'])
    if choice.lower() in ('data', 'analysis', 'analisis', 'datos', 'data analysis', 'analisis de datos'):
        with open(os.path.join(base_path, 'data', 'input.csv'), 'w') as file:
            pass # TODO
        with open(os.path.join(base_path, 'data', 'output.xlsx'), 'w') as file:
            pass # TODO
    elif choice.lower() in ('programming', 'web', 'wed development', 'development', 'dev', 'desarrollo', 'db', 'database', 'sql', 'nosql'):
        with open(os.path.join(base_path, 'data', 'database.db'), 'w') as file:
            pass # TODO
        with open(os.path.join(base_path, 'data', 'database.sql'), 'w') as file:
            pass # TODO
        os.mkdir(os.path.join(base_path, 'templates'))
        with open(os.path.join(base_path, 'templates', 'index.html'), 'w') as file:
            pass # TODO: Template basico
        os.makedirs(os.path.join(base_path, 'static', 'css'))
        with open(os.path.join(base_path, 'static', 'css', 'style.css'), 'w') as file:
            pass # TODO: Template basico
        os.mkdir(os.path.join(base_path, 'static', 'fonts'))
        os.mkdir(os.path.join(base_path, 'static', 'icons'))
        os.mkdir(os.path.join(base_path, 'static', 'pictures'))
        os.mkdir(os.path.join(base_path, 'static', 'media'))
        os.mkdir(os.path.join(base_path, 'static', 'js'))
        with open(os.path.join(base_path, 'static', 'js', 'index.js'), 'w') as file:
            pass # TODO: Boilerplate basico
    else:
        print('None selected, no placeholderfiles will be created in ./data and no web scaffoding will be created')
    choice = input(MOD_INTERFACE['OPTION_6'])
    if choice.lower() in ('y', 'yes', 'si'):
        os.mkdir(os.path.join(base_path, 'binaries'))
        # TODO Se crea Makefile y makefile.bat
    choice = input(MOD_INTERFACE['OPTION_7'])
    if choice.lower() in ('y', 'yes', 'si'):
        # TODO Se inizializa con git init
        pass
    print(f'\nThe project has been created at {base_path}\n')
    os.chdir(os.path.join(os.getcwd(), 'utils'))
    out = input(BASE)
    selector(out)

if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_initializer.txt", verbose=True)
