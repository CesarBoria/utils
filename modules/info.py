# Tool for showing basic information about the system

import sys
from modules.interfaces.general_interface import BASE, selector


def mod_main():
    print(f"""
    Informacion del sistema
    -----------------------
    
    Version de Python: {sys.version[:sys.version.find(" ")]}
    Sistema operativo: {str(sys.platform).capitalize()}
    Endianness: {str(sys.byteorder).capitalize()} Endian
    Nº de built-in modules: {len(sys.builtin_module_names)} encontrados, 59 esperados
    PYTHONPATH: {str(" | ".join(sys.path)).replace(r"/home/starseeker/Escritorio/Proyectos/Noethercode", ".")}
    Nº modulos
    OS
    Kernel
    CPU
    GPU
    Memory
    Total disk
    Disk used
    """)
    # TODO mostrar el pythonpath de manera muchisimo mas elegante
    out = input(BASE)
    selector(out)


if __name__ == '__main__':
    import doctest
    doctest.testfile("", verbose=True)
