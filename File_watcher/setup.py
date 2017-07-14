from cx_Freeze import setup, Executable
from os.path import dirname
from re import sub
from sys import executable, platform
#from os import environ

base = None
if platform == 'win32':
    base = 'Win32GUI'

executable_path = executable
executable_path = sub(pattern = "python\\.exe", repl="", string = executable_path)
#csv_file_path = r"C:\\Users\\naveen.nathan\\Desktop\\RFR\\Position_Salaries.csv"

#environ['TCL_LIBRARY'] = executable_path + "tcl\\tcl8.5"
#environ['TK_LIBRARY'] = executable_path + "tcl\\tk8.5"

includes = ['watchdog', 'logging']
#include_files = [executable_path + "DLLs\\tcl85.dll", executable_path + "DLLs\\tk85.dll"]

options = {
    'build_exe': {
        'includes': includes#, "include_files": include_files
    }
}

executables = [
    Executable('file_watch.py', base=base)
]

setup(name='File_Watcher',
      version='0.1',
      description='File Watcher',
      options=options,
      executables=executables
      )
