#
# alimaster/root_selector/__init__.py
#
"""
A package which helps the user select the version of root to load.
"""

# import gui as gui
from .gui import create_window

def main(args):
    """
    Main function called when using the root-selector as a standalone
    program
    """
    window = gui.create_window()
    return window.mainloop()
