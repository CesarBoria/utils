MOD_INTERFACE = {
'HEAD': """
ORGANIZER
---------

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
# Luego se añadiran opciones de info
}
