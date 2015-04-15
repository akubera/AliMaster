#
# alimaster/gui/simple_window.py
#
"""
Defines a 'simple_window' which should be subclassed to a specific window.
"""

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk
from alimaster.gui.fontawesome import FontAwesome


class SimpleWindow():
    """
    A Simple window which should be subclassed. This class is not tied to
    alimaster.app like the alimaster.gui.Window class is.

    The class automatically generates any ImageTk's upon creation. To use this,
    simply create a class-level dict 'imgs' which maps strings to images
    (recommended created via FontAwesome.generate_icon function).

    If this window is specific to to AliMaster's main window, your class should
    subclass alimaster.gui.Window, which is a SimpleWindow that is
    automatically bound to the masterwindow.
    """

    imgs = dict()

    def __init__(self,
                 root,
                 title,
                 minsize=(400, 200),
                 auto_close_window=True):
        self._generate_icons()
        self.root = root
        self.root.title(title)
        if auto_close_window:
            self.root.protocol("WM_DELETE_WINDOW", self.stop_tk_root)
        self.root.minsize(*minsize)

        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)

        self.on_focus = lambda: True

        self.root.bind("<FocusIn>", self._on_focus)

    def stop_tk_root(self):
        self.root.after(0, self.root.quit)

    def _on_focus(self, event):
        """
        A 'filter' function which propagates a focus event only if the main
        widget was the toplevel of the function
        """
        if event.widget is not self.window:
            return
        self.on_focus(event)


    @classmethod
    def _generate_icons(cls):
        """
        Generates the icons found in the class's imgs dict. Should only run
        once the first time one of these windows is created.
        """
        if len(cls.imgs) == 0 or any(map(
                lambda obj: isinstance(obj, ImageTk.PhotoImage),
                cls.imgs.values())):
            return

        for key, val in cls.imgs.items():
            cls.imgs[key] = ImageTk.PhotoImage(val)
