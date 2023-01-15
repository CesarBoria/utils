# This module contains the interface of the CLI

class Interfaz:
    INTERFAZ = """
    ------------------------------------------
    
    UTILS - A group of useful tools for scripting
    
    ------------------------------------------
    
    
    Select a tool to run. You can return to this list entering GO BACK.
    You can get more info about a tool entering INFO <Nº OF TOOL>.
    You can exit the program by entering EXIT at any time.
    
    0 - General information
    1 - Project initializer
    2 - Organizer
    3 - Analyzer
    4 - CRON job creator
    5 - Dotfile handler
    6 - Import checker
    7 - Encrypter
    8 - Key generator
    9 - Mouse and keyboard handler
    10 - Diff tool
    11 - API checker
    12 - Web redirector
    13 - Systemd tool
    
    """
    INFORMACION = {
        0: "Shows general information about the Python interpreter, the system, ...",
        1: "Initializes a Python project, creating a file and directory structure (scaffolding)",
        2: "Cleans up a directory, allocating files according to their extension (in folders specifying such extension)",
        3: "Analyzes a directory, showing info like total size used, largest file, absolute path, ...",
        4: "Creates a CRON job interactively",
        5: "Easy to use tool for importing or exporting dotfiles",
        6: "Tool for checking imports in a Python project. It will show a graph with interdependencies between modules",
        7: "Encrypts or decrypts using known and tested algorithms",
        8: "Password or SSH/GPG key generator",
        9: "Allows to automate mouse movement and keyboard input",
        10: "Shows deltas (diffs) between two files, git style",
        11: "Checks the status of an API endpoint",
        12: "Redirects a given URL to a different web site",
        13: "Shows information about active systemd processes (systemctl)"
    }
    IMPORTS = (
        "from modules.info import mod_main\nmod_main()",
        "from modules.initializer import mod_main\nmod_main()",
        "from modules.organizer import mod_main\nmod_main()",
        "from modules.analyzer import mod_main\nmod_main()",
        "from modules.cron import mod_main\nmod_main()",
        "from modules.dotfile import mod_main\nmod_main()",
        "from modules.import_checker import mod_main\nmod_main()",
        "from modules.crypto import mod_main\nmod_main()",
        "from modules.key_gen import mod_main\nmod_main()",
        "from modules.mouse_keyb import mod_main\nmod_main()",
        "from modules.diff_tool import mod_main\nmod_main()",
        "from modules.api_check import mod_main\nmod_main()",
        "from modules.web_redirect import mod_main\nmod_main()",
        "from modules.systemd import mod_main\nmod_main()"
    )

    def info(self, n: int):
        """Shows info about the selected option"""
        try:
            print(self.INFORMACION[n])
        except (TypeError, KeyError):
            print("Invalid input, if you want to exit, enter EXIT")
            # TODO hacer que la llamada sea recursiva

    def show(self):
        '''Shows the interface (creates it)'''
        print(self.INTERFAZ)


if __name__ == '__main__':
    import doctest
    doctest.testfile('../../tests/test_interface.txt', verbose=True)
