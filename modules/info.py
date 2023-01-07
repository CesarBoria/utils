# Tool for showing basic information about the system

import sys
from os import system
from modules.interfaces.general_interface import BASE, selector


def OS_ver():
    os_version = str(sys.platform).capitalize()
    return os_version if os_version != 'Linux' else f"{os_version} with kernel {system('uname -r')}" # TODO manejar stdout!

def mod_main():
    print(f"""
    Informacion del sistema
    -----------------------
    
    Python version: {sys.version[:sys.version.find(" ")]}
    Operative system: {OS_ver()}
    Endianness: {str(sys.byteorder).capitalize()} Endian
    Nº of built-in Python modules: {len(sys.builtin_module_names)} found, 59 to be expected
    PYTHONPATH: {str(" | ".join(sys.path)).replace(r"/home/starseeker/Escritorio/Proyectos/Noethercode", ".")}
    Disk: {system('df -h /')}
    Memory: {system('free')}
    CPU: {system('lscpu')}
    """)
    # TODO mostrar el pythonpath de manera muchisimo mas elegante
    # TODO manejar stdout!
    out = input(BASE)
    selector(out)


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_info.txt", verbose=True)
