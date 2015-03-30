#
# alimaster/root_selector/__init__.py
#
"""
A package which helps the user select the version of root to load.
"""

import alimaster
# import gui as gui
from .gui import create_window

from tkinter import *
from tkinter.ttk import *

def main(args):
    """
    Main function called when using the root-selector as a standalone program.
    Creates a root_selector.gui.MainWindow and runs Tk
    """

    # cfg = alimaster.load_config('root_selector')
    # print (args)

    root = Tk()
    window = gui.create_window(root)
    alimaster.keep_tk_awake(root)
    root.mainloop()

    return 0
