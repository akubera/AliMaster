#
# alimaster/gui/style.py
#

from tkinter import *
from tkinter.ttk import *


style = ttk.Style()

style.theme_create("alimaster", parent='alt', settings={
  "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
  "TNotebook.Tab": {
    "configure": {"padding": [5, 1]}
  },
  "alienwindow.TFrame" : {
    "configure": {"padding": [5, 1]}
  }
})
