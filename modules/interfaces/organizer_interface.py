MOD_INTERFACE = {
'HEAD': """
ORGANIZER
---------

Docs are available with <COMMAND> INFO

0 PATH - Change, set or show the working path (where the tool can make changes)
1 DO <COMMAND> - Copy (CP), move (MV) or remove (RM) files and directories
2 ORDER - Orders the files inside the directory according to extension
3 SHOW - Shows all the information about the current (working) directory
4 HIDDEN - Shows and creates hidden files and directories
5 LINK - Creates symlinks

Example: Moving the file info.txt from /home to /home/dir

    PATH
        >>> Current path: /
    PATH home
        >>> New path set to /home
    DO MV info.txt dir
        >>> File info.txt moved to /home/dir

"""
,
'PATH':
"""
PATH - Shows the current directory
PATH <VALID_DIR> - Changes the current directory to the specified one

<VALID_DIR> follows the usual path rules. Relative paths can be done with
~ (home), .. (parent) and / (Linux root)

Info about the current path can be listed with the SHOW command

The current directory is the standart path for the other commands of the tool

"""
,
'DO':
"""
CP <FILE_OR_DIR> - Copies the file or directory to the current working directory
CP <FILE_OR_DIR> <DESTINY_DR> - Copies the file or directory to a specified directory
MV <FILE_OR_DIR> - Moves the file or directory to the current working directory
MV <FILE_OR_DIR> <DESTINY_DIR> - Moves the file or directory to a specified directory
RM <FILE_OR_DIR> - Deletes the file or directory

<FILE_OR_DIR> and <DESTINY_DIR> will take PATH current directory
as the relative path, unless an absolute path is specified

"""
,
'ORDER':
"""

"""
,
'SHOW':
"""

"""
,
'HIDDEN':
"""

"""
,
'LINK':
"""

"""
}
