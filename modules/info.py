# Tool for showing basic information about the system
import os
import sys, subprocess, psutil
from modules.interfaces.general_interface import BASE, selector


def OS_ver():
    os_version = str(sys.platform).capitalize()
    os.system('uname -r > temp.txt')
    with open('temp.txt') as temp_file:
        kernel = temp_file.read()
        kernel = kernel.strip('\n')
        temp_path = os.path.join(os.getcwd(), temp_file.name)
    os.remove(temp_path)
    return os_version if os_version != 'Linux' else f"{os_version} with kernel {kernel}"


def cpu_info():
    bin_info = subprocess.check_output("lscpu").decode()
    cpu_info_raw = bin_info.replace(" ","")
    cpu_info_raw = cpu_info_raw.replace("\n", "||")
    cpu_info_raw = cpu_info_raw.split("||")
    cpu_info = []
    for key, value in zip(range(7), (0, 4, 7, 10, 20, 22, 23)):
        value_short = cpu_info_raw[value]
        value_short = value_short[value_short.find(":")+1:]
        cpu_info.append((key, value_short))
    return {item[0]: item[1] for item in cpu_info}


cpu_info = cpu_info()


def mod_main():
    print(f"""
    Informacion del sistema
    -----------------------
    
    Python version: {sys.version[:sys.version.find(" ")]}
    Operative system: {OS_ver()}
    Endianness: {str(sys.byteorder).capitalize()} Endian
    Nº of built-in Python modules: {len(sys.builtin_module_names)} found, 59 to be expected
    PYTHONPATH: {str("  ".join(sys.path)).replace(r"/home/starseeker/Escritorio/Proyectos/Noethercode", ".")}
    CPU model: CPU {cpu_info[2]} ({cpu_info[0]} architecture), {cpu_info[1]} cores ({cpu_info[3]} threads each)
    CPU cache: L1 {str(cpu_info[4])[:5]}  L2 {str(cpu_info[5])[:6]}  L3 {str(cpu_info[6])[:4]}
    Memory: {round(int(psutil.virtual_memory().total)/1073741824, 2)} GB RAM memory, available {round(int(psutil.virtual_memory().available)/1073741824, 2)} GB (used {round(int(psutil.virtual_memory().used)/1073741824, 2)} GB)
    Disk: Total disk space {round(int(psutil.disk_usage('/').total)/1073741824, 2)} GB, used {round(int(psutil.disk_usage('/').used)/1073741824, 2)} GB ({round(int(psutil.disk_usage('/').free)/1073741824, 2)} GB free)
    Nº of partitions found: {len(tuple(item.device for item in psutil.disk_partitions(all=False)))} partitions
    """)
    out = input(BASE)
    selector(out)


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_info.txt", verbose=True)
