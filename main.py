# Main Python file
from interface import Interfaz

def convertir(input) -> int:
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

if __name__ == "__main__":
    _interface = Interfaz()
    _interface.show()
    user_input = convertir(input(">>> "))
