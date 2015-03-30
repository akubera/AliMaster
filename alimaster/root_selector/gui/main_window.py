#
# alimaster/root_selector/gui/main_window.py
#
"""
The main window for the root_selector alimaster subpackage.
"""

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk


class MainWindow():

    def __init__(self, root):
        """
        Construct the main window of the root_selector program
        """
        print ("[MainWindow::__init__]")
        self.root = root
        self.root.title("AliMaster | ROOT Selector")
        self.root.protocol("WM_DELETE_WINDOW", self.stop_tk_root)
        self.root.minsize(400,200)

        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)

        self.lbl = Label(self.frame , text = "ROOT Selector")
        self.lbl.pack(anchor='nw')

        self.frame.pack()

        # master = self.frame
        # self.btn = Button(master , text = "Button" , command = self.command )
        # self.btn.pack()
        print ("[MainWindow::__init__] Done.")

    def stop_tk_root(self):
        self.root.after(0, self.root.quit)

    def command(self):
        print ('Button is pressed!')

        self.newWindow = tk.Toplevel(self.master)
        self.app = windowclass1(self.newWindow)
