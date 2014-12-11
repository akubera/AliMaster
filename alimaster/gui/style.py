#
# alimaster/gui/style.py
#

from tkinter import *
from tkinter.ttk import *


style = ttk.Style()

style.theme_create("alimaster", parent='alt', settings={
  "." : {
    "configure": {
      # "font": ('Helvetica', 50)
    }
  },

  "TNotebook" : {
    "configure": {"tabmargins": [2, 5, 2, 0]}
  },

  "TNotebook.Tab": {
    "configure": {"padding": [5, 1]}
  },
  "alienwindow.TFrame" : {
    "configure": {"padding": [5, 1]}
  },

  "StatusGood.TLabel" : {
    "configure": {"foreground": "green"}
  },
  "StatusBad.TLabel" : {
    "configure": {"foreground": "red"}
  },

  "Sidebar_FileBrowser.TFrame": {
    "configure": {"background": "blue"}
  },

  "Toolbar.TButton": {
    "configure": {"relief": "flat",
                  "foreground": "red",
                  "background": "black",
                      "height": 64}
  },

  "TButton": {
    "configure": {"relief": "raised",
                "cursor":"help",
                'anchor':'center',
                'padding': 3},
    "map": {"foreground": [("pressed", '#444'), ('active', '#444')]}
  }


})
