#
# alimaster/root_selector/gui/__init__.py
#

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

from alimaster.gui import RES

from alimaster.gui.fontawesome import FontAwesome
from alimaster.gui.style import get_style

from .main_window import MainWindow

# import alimaster.root_selector as root_selector

def create_window(root):
    """
    Loads the alimaster style, then creates and returns a
    root_selector.gui.MainWindow with provided tk instance
    """
    style = get_style()
    style.theme_use('alimaster')
    return MainWindow(root)
