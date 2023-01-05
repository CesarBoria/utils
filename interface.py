# This module contains the interface of the CLI
import sys


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
    2 - Low level explorer
    3 - Organizer
    4 - Analyzer
    5 - CRON job creator
    6 - Dotfile handler
    7 - Import checker
    8 - Encrypter
    9 - Key generator
    10 - Mouse and keyboard handler
    11 - Diff tool
    12 - API checker
    13 - Web redirector
    14 - Systemd tool
    
    """
    INFORMACION = {
        0: "Shows general information about the Python interpreter, the system, ...",
        1: "Initializes a Python project, creating a file and directory structure (scaffolding)",
        2: "Shows byte/hex code of a file, in an ordered fashion",
        3: "Cleans up a directory, allocating files according to their extension (in folders specifying such extension)",
        4: "Analyzes a directory, showing info like total size used, largest file, absolute path, ...",
        5: "Creates a CRON job interactively",
        6: "Easy to use tool for importing or exporting dotfiles",
        7: "Tool for checking imports in a Python project. It will show a graph with interdependencies between modules",
        8: "Encrypts or decrypts using known and tested algorithms",
        9: "Password or SSH/GPG key generator",
        10: "Allows to automate mouse movement and keyboard input",
        11: "Shows deltas (diffs) between two files, git style",
        12: "Checks the status of an API endpoint",
        13: "Redirects a given URL to a different web site",
        14: "Shows information about active systemd processes (systemctl)"
    }

    def info(self, n: int):
        """Shows info about the selected option"""
        if n >= 0 and n <= len(self.INFORMACION) - 1:
            print(self.INFORMACION[n])
        else:
            print("Invalid input, if you want to exit, enter EXIT")

    @staticmethod
    def exit():
        """Exits the program"""
        sys.exit()

    def show(self):
        print(self.INTERFAZ)


if __name__ == '__main__':
    # Test basico con doctest
    import doctest
    doctest.testfile('./tests/test_interface.txt', verbose=True)
