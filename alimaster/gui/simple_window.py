

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk
from alimaster.gui.fontawesome import FontAwesome


class SimpleWindow():
    """
    A Simple window which should be subclassed. This class is not tied to
    alimaster.app like the alimaster.gui.Window class is.
    """

    imgs = dict()

    def __init__(self, root, title, minsize=(400, 200), ):
        self._generate_icons()
        self.root = root
        self.root.title(title)
        self.root.protocol("WM_DELETE_WINDOW", self.stop_tk_root)
        self.root.minsize(*minsize)

        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)

    def stop_tk_root(self):
        self.root.after(0, self.root.quit)

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
