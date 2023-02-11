from tkinter import Tk, Label, Button, Entry, filedialog, Frame
from tkinterdnd2 import *
import os
import ctypes, sys



def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0


if is_admin():
     from main_window import MyFirstGUI
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
