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
    min_size = (500, 200)

    def __init__(self, app, mainwindow=None):
        """
        Construct the settings window
        """
        super().__init__(app, mainwindow)
        self.xframe = Frame(self.frame)
        self.tree_view = Treeview(self.xframe)
        self.tree_view.pack(fill=Y, side=LEFT, padx=6, pady=6)
        self.tabbed_view = Notebook(self.xframe)
        self.tabbed_view.pack(fill=BOTH, side=RIGHT, expand=2, padx=6, pady=6)

        self.xframe.pack(fill=BOTH, expand=1)
        # self.add_tab("General")

        self.button_frame = Frame(self.frame)
        Button(self.button_frame,
               text="SAVE",
               command=self.save_settings,
               ).pack(side=RIGHT, padx=6, pady=(0,4))
        Button(self.button_frame,
               text="CANCEL",
               command=self.close
               ).pack(side=RIGHT, pady=(0,4))
        self.button_frame.pack(side=BOTTOM, fill=X)

    def save_settings(self):
        print("Saving settings...")

    def add_tab(self, name):
        self.tabbed_view.add(None, text=name)
