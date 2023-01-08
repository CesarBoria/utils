BASE = f"""
Introduce GO BACK para volver atras, o EXIT para salir\n>>> 
"""

from main import crear_interfaz


def selector(choice: str):
    if choice.lower() == 'exit':
        import sys
        sys.exit()
    elif choice.lower() in ('back', 'go back', 'return'):
        crear_interfaz()
