#
# alimaster/gui/style.py
#

from tkinter import *      # noqa
from tkinter.ttk import *  # noqa

from .fontawesome import _font_16 as fontawesome

style = None


def get_style():
    global style, style_theme
    if style is not None:
        return style
    style = ttk.Style()
    style.theme_create("alimaster", parent='alt', settings=style_theme)
    return style

style_theme = {
    ".": {
        "configure": {
            # "font": ('Helvetica', 50)
        }
    },

    "TNotebook": {
        "configure": {
            "tabmargins": [2, 5, 2, 0]
        }
    },

    "TNotebook.Tab": {
        "configure": {
            "padding": [5, 1]
        }
    },
    "alienwindow.TFrame": {
        "configure": {
            "padding": [5, 1]
        }
    },

    "StatusGood.TLabel": {
        "configure": {
            "foreground": "green"
        }
    },

    'StatusBad.TLabel': {
        'configure': {
            'foreground': 'red'
        }
    },

    "Sidebar_FileBrowser.TFrame": {
        "configure": {
            'background': 'blue'
        }
    },

    # This doesn't work (yet)
    'Awesome.Toolbar.TButton': {
        'configure': {
            'font': fontawesome
        }
    },

    'TButton': {
        'configure': {
            'relief': 'raised',
            'cursor': 'help',
            'anchor': 'center',
            'padding': 3
        },
        'map': {
            'foreground': [
                ('disabled', '#999'),
                ('pressed', '#444'),
                ('active', '#444')
            ]
        }
    },


    "Toolbar.TButton": {
        'configure': {
            'relief': 'flat',
            'font': ('DejaVu Mono', -13)
        }
    }

}
