#
# alimaster/gui/help_window.py
#
"""
Code for displaying the main help window, loaded from the alimaster main-window
"""

from tkinter import *      # noqa
from tkinter.ttk import *  # noqa

from .fontawesome import FontAwesome
from .window import Window


class HelpWindow(Window):

    toolbar_icon_size = 16

    imgs = {
        "larrow": FontAwesome.generate_icon('chevron-left', tb_icon_size),
        "rarrow": FontAwesome.generate_icon('chevron-right', tb_icon_size),
        "home": FontAwesome.generate_icon('home', tb_icon_size),
        "folder": FontAwesome.generate_icon('folder', 12)
    }

    default_window = {'width': 640, 'height': 480}
    default_height = 480
    default_width = 640

    min_size = (220, 300)

    title = "Alimaster | Help"

    def __init__(self, app, toplevel=None):
        """Construct the Help Window"""
        super().__init__(app, toplevel)

        self._setup_menu()

        self.frame = Frame(self.window, **self.default_window)
        self.frame.pack_propagate(0)

        self._setup_toolbar()

        self.content = Frame(self.frame,
                             relief=FLAT,
                             style='MainFileBrowser.TFrame'
                             )
        self.content.pack(fill=BOTH, expand=1)
        self.label = Label(self.content, text="Help")
        self.label.pack(side='left', anchor='nw')

        self.frame.pack(fill=BOTH, expand=True)

    def _setup_toolbar(self):
        self.toolbar = Frame(self.frame, relief=RAISED)

    def _setup_menu(self):
        pass

    def on_left_button(self):
        print("[on_left_button]")

        def _cb(arg):
            print("[_cb]", arg)

        self.app.alien.call(_cb, 'ls')
