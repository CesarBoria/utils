MOD_INTERFACE = {
'HEAD': """
ORGANIZER
---------

Docs are available with <COMMAND> INFO

0 PATH - Change, set or show the working path (where the tool can make changes)
1 DO <COMMAND> - Copy (CP), move (MV) or remove (RM) files and directories
2 ORDER - Orders the files inside a directory according to extension
3 SHOW - Shows all the information about the current (working) directory
4 LINK - Creates symlinks

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
ORDER <VALID_DIR> - Creates folders inside a valid directory according to file extension and moves
                    all files inside the corresponding folder according to extension
ORDER HERE - Moves files from the current working directory to folders matching the extension
ORDER - Creates folders in desktop according to file extension and moves all files inside the
        corresponding folder ~/Desktop/new_folder_by_extension according to extension

SHOW allows a quick view of what's inside the current directory (or any path)

"""
,
'SHOW':
"""
SHOW - Shows everything inside the current directory, parent and child directories
SHOW ALL - Shows all info of every file and directory inside current directory
SHOW <VALID_DIR> - Shows everything inside that directory, and parent and child directories of that one
SHOW ALL <VALID_DIR> - Shows all info of every file and directory inside that directory
SHOW SYSTEM - Shows all info about root directory
SHOW HOME - Shows detailed info about home directories (desktop, pictures, ...)

Analyzes a directory, showing info like total size used, largest file, absolute path, ...

"""
,
'LINK':
"""
LINK <DESTINY_PATH> - 
LINK <VALID_DIRECTORY> <DESTINY_PATH> - 

Creates a symlink between a directory and another. If only one is specified,
the symlink will be created in the current working directory
"""
}
