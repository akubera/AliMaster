#
# alimaster/root_selector/__main__.py
#
"""
This file allows the root_selector subpackage to be runnable
"""

import sys

from tkinter import *
from tkinter.ttk import *

from alimaster.root_selector import gui
from alimaster import keep_tk_awake

def main(args):
    """
    Main function called when using the root-selector as a standalone program.
    Creates a root_selector.gui.MainWindow and runs Tk
    """

    root = Tk()
    window = gui.create_window(root)
    keep_tk_awake(root)

    root.mainloop()


    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
