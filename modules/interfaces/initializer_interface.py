MOD_INTERFACE = {
'HEAD': """
INITIALIZER
-----------

This tool automates the creation of a Python project.
It will create a basic structure for any app.

Example:
    
    MY_PROJECT
    |
    |
    |----source
    |        |--__init__.py
    |        |--main.py
    |        |--project
    |                |--__init__.py
    |                |-- ...
    |----tests
    |        |--__init__.py
    |        |--tests.py
    |
    |--.gitignore
    |--README.md
    |--requirements.txt
    |--setup.py

"""
,
'OPTION_1': """
Specify the app name (case sensitive)

"""
,
'OPTION_2': """
Quick setup: There's a Flask app structure ready to be used, would you like to use it?
If you enter NO, then you will create a custom app structure

"""
,
'OPTION_3': """
Do you want to include a /tests and /docs directories?

"""
,
'OPTION_4': """
Do you want to include some setup files for setuptools (making the app a Python package)?

"""
,
'OPTION_5': """
Will you use this app for data analysis or backend web development?

"""
,
'OPTION_6': """
Do you want to include a /binaries directory for binary files, and a basic makefile (quick app installation and initialization)?

"""
,
'OPTION_7': """
Do you want to initialize a local git repository for the app?

"""
}
