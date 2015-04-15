#
# alimaster/gui/settings_window.py
#
"""
A GUI window for managing user settings.
"""

from tkinter import *
from tkinter.ttk import *

from .window import Window

class SettingsWindow(Window):

    title = "Settings | AliMaster"
    default_window = {'width':640, 'height':480}

    def __init__(self, app, mainwindow=None):
        """
        Construct the settings window
        """
        super().__init__(app, mainwindow)
        self.frame = Frame(self.window, **self.default_window)
        self.frame.pack_propagate(0)
        self.frame.pack(fill=BOTH, expand=True)
