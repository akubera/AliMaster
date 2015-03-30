#
# alimaster/root_selector/gui/__init__.py
#

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

from alimaster.gui import RES

from alimaster.gui.fontawesome import FontAwesome
from alimaster.gui.style import style

def create_window():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: root.after(0, root.quit))

    style.theme_use('alimaster')

    window = Toplevel(root)

    return root
