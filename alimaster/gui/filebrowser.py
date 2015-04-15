#
# alimaster/gui/filebrowser.py
#

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

from . import RES

from .window import Window

from .fontawesome import FontAwesome


class FileBrowserWindow(Window):

    tb_icon_size = 16

    imgs = {
        "larrow": FontAwesome.generate_icon('chevron-left', tb_icon_size),
        "rarrow": FontAwesome.generate_icon('chevron-right', tb_icon_size),
        "home":   FontAwesome.generate_icon('home', tb_icon_size),
        "folder": FontAwesome.generate_icon('folder', 12)
    }

    default_window = {'width': 640, 'height': 480}
    default_height = 480
    default_width = 640

    min_size = (220, 300)
    title = "Alimaster File Browser"

    def __init__(self, app, toplevel=None):
        """
        Construct a alimaster file browser inside the provided toplevel

        @param app: The alimaster application the window communicates with
        @param toplevel: a window provided to
        """
        super().__init__(app, toplevel)
        self._generate_icons()
        self._setup_menu()

        self.frame = Frame(self.window, **self.default_window)
        self.frame.pack_propagate(0)

        self._setup_toolbar()

        self.location_var = StringVar()
        self.locationbox = Combobox(self.frame,
                                    height=12,
                                    textvariable=self.location_var
                                    )

        self.locationbox.bind('<Return>',
                              lambda ev: print("[RETURN]", ev.widget.get()))

        self.locationbox.bind('<<ComboboxSelected>>',
                              lambda ev: print("EVENT", ev))

        self.locationbox.pack(side=TOP, fill=X, padx=8, pady=3, expand=0)
        self.location_var.set('~')

        self.status = StringVar()
        self.statusbar = Label(self.frame,
                               textvar=self.status,
                               font=("DejaVu Sans", -10),
                               relief='sunken'
                               ).pack(expand=0,
                                      fill=X,
                                      side=BOTTOM,
                                      anchor=S,
                                      padx=1,
                                      pady=2)

        self.set_status("Initializing")

        #     self.tree_view = (parent, **kwargs)

        self.sidebar = Treeview(self.frame,
                                style='SidebarFileBrowser.TFrame'
                                ).pack(fill=Y, side=LEFT, expand=0)

        self.content = Frame(self.frame,
                             relief=FLAT,
                             style='MainFileBrowser.TFrame'
                             ).pack(fill=BOTH, expand=1)

        self.label = Label(self.content,
                           text="Files",
                           image=self.imgs["folder"],
                           compound='left').pack()

        self.frame.pack(fill=BOTH, expand=True)

    def new_file(self):
        pass

    def set_status(self, msg=''):
        self.status.set(' ' + msg)

    def _setup_menu(self):
        self.menubar = Menu(self.window, relief='flat', tearoff='false')

        m_file = Menu(self.menubar, tearoff='false')
        m_file.id = 'm_file'

        m_file.add_command(label='New', command=self.new_file)
        m_file.add_separator()
        m_file.add_command(label="Close", command=self.close)

        m_edit = Menu(self.menubar, tearoff='false')
        m_edit.id = 'm_edit'

        m_edit.add_separator()
        m_edit.add_command(label='Preferences')

        m_help = Menu(self.menubar, tearoff='false')
        m_help.id = 'm_help'

        m_help.add_command(label="About")

        self.menubar.add_cascade(menu=m_file, label="File")
        self.menubar.add_cascade(menu=m_edit, label="Edit")
        self.menubar.add_cascade(menu=m_help, label="Help")

        self.window.config(menu=self.menubar)

    def _setup_toolbar(self):
        self.toolbar = Frame(self.frame, relief=RAISED)
        self.back_b = Button(self.toolbar,
                             style='Toolbar.TButton',
                             image=self.imgs["larrow"],
                             command=self.on_left_button
                             ).pack(side=LEFT, padx=0, pady=2)

        self.forward_b = Button(self.toolbar,
                                style='Toolbar.TButton',
                                image=self.imgs["rarrow"],
                                command=lambda: print("right button")
                                ).pack(side=LEFT, padx=0, pady=2)

        self.home_b = Button(self.toolbar,
                             style='Toolbar.TButton',
                             image=self.imgs["home"],
                             text='Home',
                             command=lambda: print("GOHOME")
                             ).pack(side=LEFT, padx=(12, 0), pady=2)

        self.search_b = Button(self.toolbar,
                               style='Toolbar.TButton',
                               text='Search',
                               command=lambda: print("Search button")
                               ).pack(side=RIGHT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X, expand=0)

    def on_left_button(self):
        print("[on_left_button]")
        self.app.alien.call(lambda arg: print("<[", arg, "]>"), 'ls')
