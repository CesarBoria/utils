# Main Python file
from modules.interfaces.main_interface import Interfaz
from time import sleep


def convertir(input) -> int:
    '''Makes sure the input is an int''' # TODO ver si esto hace que falle info(n=2) en main_interface.py
    try:
        output = int(input)
    except ValueError:
        try:
            input = float(input)
        except ValueError:
            print('No es un numero')
            return None # TODO cambiarlo para que sea mas elegante
        else:
            output = str(input).split('.')
            output = int(output[0])

    return output
# TODO: falla en 'a', arreglar


def crear_interfaz():
    '''Creates the interface instantiating it, and then using the method show.
    The selection is handled by IMPORTS tuple'''
    _interface = Interfaz()
    _interface.show()
    user_input = input(">>> ")
    _ = user_input.lower()
    if _.find('info') > -1:
        info_index = convertir(_.replace("info ", ""))
        _interface.info(info_index)
        sleep(3)
        crear_interfaz()
    elif _.find('exit') > -1:
        import sys
        sys.exit()
    exec(_interface.IMPORTS[convertir(user_input)])


if __name__ == "__main__":
    crear_interfaz()
