# Main Python file
from modules.interfaces.main_interface import Interfaz

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


def crear_interfaz():
    '''Creates the interface instantiating it, and then using the method show.
    The selection is handled by IMPORTS tuple'''
    _interface = Interfaz()
    _interface.show()
    user_input = convertir(input(">>> "))
    exec(_interface.IMPORTS[user_input])

if __name__ == "__main__":
    crear_interfaz()
