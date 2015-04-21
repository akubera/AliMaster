#
# alimaster/gui/help_window.py
#
"""
Code for displaying the main help window, loaded from the alimaster main-window
"""

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

from . import RES
from .fontawesome import FontAwesome
from .window import Window


class HelpWindow(Window):

  toolbar_icon_size = 16

  left_arrow_img   = FontAwesome.generate_icon('chevron-left', toolbar_icon_size)
  right_arrow_img  = FontAwesome.generate_icon('chevron-right', toolbar_icon_size)
  home_img         = FontAwesome.generate_icon('home', toolbar_icon_size)

  default_window = {'width':640, 'height':480}
  default_height = 480
  default_width = 640

  title = "Alimaster | Help"

  def __init__(self, app, toplevel = None):
    """Construct the Help Window"""
    super().__init__(app, toplevel)

    self._generate_icons()

    self._setup_menu()

    self.frame = Frame(self.window, **self.default_window)
    self.frame.pack_propagate(0)

    self._setup_toolbar()

    self.content = Frame(self.frame, relief=FLAT, style='MainFileBrowser.TFrame')
    self.content.pack(fill=BOTH, expand=1)
    self.label = Label(self.content, text="Help").pack(side='left',anchor='nw')

    self.frame.pack(fill=BOTH, expand=True)

  def _setup_toolbar(self):
    self.toolbar = Frame(self.frame, relief=RAISED)
    return
    self.back_b = Button(self.toolbar, style='Toolbar.TButton', image=self.left_arrow_img, command=self.on_left_button).pack(side=LEFT, padx=0, pady=2)
    self.forward_b = Button(self.toolbar, style='Toolbar.TButton', image=self.right_arrow_img, command=lambda:print("right button")).pack(side=LEFT, padx=0, pady=2)
    self.home_b = Button(self.toolbar, style='Toolbar.TButton', image=self.home_img, text='Home', command=lambda:print("GOHOME")).pack(side=LEFT, padx=(12,0), pady=2)
    self.search_b = Button(self.toolbar, style='Toolbar.TButton', text='Search', command=lambda:print("Search button")).pack(side=RIGHT, padx=2, pady=2)

    self.toolbar.pack(side=TOP, fill=X, expand=0)

  def _setup_menu(self):
      pass

  def on_left_button(self):
    print ("[on_left_button]")

    def _cb(arg):
      print ("[_cb]", arg)

    self.app.alien.call(_cb, 'ls')

  @classmethod
  def _generate_icons(cls):
    if isinstance(cls.home_img, ImageTk.PhotoImage): return
    cls.home_img = ImageTk.PhotoImage(cls.home_img)
    cls.left_arrow_img = ImageTk.PhotoImage(cls.left_arrow_img.crop((0,0,cls.toolbar_icon_size - 5, cls.toolbar_icon_size)))
    cls.right_arrow_img = ImageTk.PhotoImage(cls.right_arrow_img.crop((0,0,cls.toolbar_icon_size - 5, cls.toolbar_icon_size)))
