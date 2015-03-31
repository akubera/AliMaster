#
# alimaster/gui/filebrowser.py
#

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

from . import RES

from .fontawesome import FontAwesome

class FileBrowserWindow():

  toolbar_icon_size = 16

  left_arrow_img   = FontAwesome.generate_icon('chevron-left', toolbar_icon_size)
  right_arrow_img  = FontAwesome.generate_icon('chevron-right', toolbar_icon_size)
  home_img         = FontAwesome.generate_icon('home', toolbar_icon_size)

  default_window = {'width':640, 'height':480}
  default_height = 480
  default_width = 640

  def __init__(self, control, toplevel):
    """
        Construct a alimaster file browser inside the provided toplevel
        """
    self._generate_icons()
    self.main_window = control
    self.app = self.main_window.app
    # self.root = master

    self.window = toplevel #Toplevel(self.root)
    self.window.minsize(220,300)
    self.window.title("Alimaster File Browser")
    self._setup_menu()

    self.frame = Frame(self.window, **self.default_window)
    self.frame.pack_propagate(0)

    self._setup_toolbar()

    self.location_var = StringVar()
    self.locationbox = Combobox(self.frame, height=12, textvariable=self.location_var)
    self.locationbox.bind('<Return>', lambda ev: print("RETURN", ev.widget.get())) #  dir(ev), ))
    self.locationbox.bind('<<ComboboxSelected>>', lambda ev: print("EVENT",ev))
    self.locationbox.pack(side=TOP, fill=X, padx=8,pady=3, expand=0)
    self.location_var.set('~')

    self.status = StringVar()
    self.statusbar = Label(self.frame, textvar= self.status, font=("DejaVu Sans", -10), relief='sunken')
    self.statusbar.pack(expand=0, fill=X, side=BOTTOM, anchor= S, padx=1,pady=2)
    self.set_status("Initializing")

    #     self.tree_view = (parent, **kwargs)

    self.sidebar = Treeview(self.frame, style='SidebarFileBrowser.TFrame')
    #     self.label = Label(self.sidebar, text="Sidebar").pack()
    self.sidebar.pack(fill=Y, side=LEFT, expand=0)

    self.content = Frame(self.frame, relief=FLAT, style='MainFileBrowser.TFrame')
    self.content.pack(fill=BOTH, expand=1)
    self.folder_img = ImageTk.PhotoImage(FontAwesome.generate_icon('folder', 12))
    self.label = Label(self.content, text="Files", image=self.folder_img, compound='left').pack()

    self.frame.pack(fill=BOTH, expand=True)

  def new_file(self):
    pass

  def quit(self):
    pass

  def set_status(self, msg= ''):
    self.status.set(' ' + msg)

  def _setup_menu(self):
    self.menubar = Menu(self.window, relief='flat', tearoff='false')

    m_file = Menu(self.menubar, tearoff='false')
    m_file.id = 'm_file'

    m_file.add_command(label='New', command=self.new_file)
    m_file.add_separator()
    m_file.add_command(label="Quit", command= self.quit)

    m_edit = Menu(self.menubar, tearoff='false')
    m_edit.id = 'm_edit'

    m_edit.add_separator()
    m_edit.add_command(label='Preferences')

    m_help = Menu(self.menubar, tearoff='false')
    m_help.id = 'm_help'

    m_help.add_command(label="About")

    self.menubar.add_cascade(menu=m_file, label="File")
    self.menubar.add_cascade(menu=m_edit, label="Edit")
    self.menubar.add_cascade(menu=m_help, label= "Help")

    self.window.config(menu=self.menubar)

  def _setup_toolbar(self):
    self.toolbar = Frame(self.frame, relief=RAISED)
    self.back_b = Button(self.toolbar, style='Toolbar.TButton', image=self.left_arrow_img, command=self.on_left_button).pack(side=LEFT, padx=0, pady=2)
    self.forward_b = Button(self.toolbar, style='Toolbar.TButton', image=self.right_arrow_img, command=lambda:print("right button")).pack(side=LEFT, padx=0, pady=2)
    self.home_b = Button(self.toolbar, style='Toolbar.TButton', image=self.home_img, text='Home', command=lambda:print("GOHOME")).pack(side=LEFT, padx=(12,0), pady=2)
    self.search_b = Button(self.toolbar, style='Toolbar.TButton', text='Search', command=lambda:print("Search button")).pack(side=RIGHT, padx=2, pady=2)

    self.toolbar.pack(side=TOP, fill=X, expand=0)

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
