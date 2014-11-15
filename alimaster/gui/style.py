#
#
#

from tkinter import *
from tkinter.ttk import *


def GenerateStyle(style):
  style.configure("StatusGood.TLabel", foreground="green")
  style.configure("StatusBad.TLabel", foreground="red")

  style.configure('Sidebar_FileBrowser.TFrame', background='blue')
  style.configure('Toolbar.TButton', foreground='red', background='black', height=64)
