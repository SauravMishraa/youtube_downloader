import cx_Freeze 
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\{NAME}\AppData\Local\Programs\Python\Python36\tcl\tcl8.6" 
# Open Your Python File Location and go to tcl folder then copy path for tcl8.6 and tk8.6
# note You copy tcl8.6 and tk8.6 actual path 
# if you are on windows select the tcl8.6 and then from Home at top you can copy
os.environ['TK_LIBRARY'] = r"C:\Users\{NAME}\AppData\Local\Programs\Python\Python36\tcl\tK8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="icon.ico")]
# change the main.py if your program name is different

cx_Freeze.setup(
    name = "YouTube Downloader",
    options = {"build_exe": {"packages":["tkinter","youtube_dl"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll',]}}, 
    # from Python file location go to dlls and copy tcl86t.dll and tk86t.dll files to the folder where this setup.py is and the main.py is.
    

    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )