#
# alimaster/gui/filebrowser.py
#

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

from . import RES

from .fontawesome import FontAwesome


class FileBrowserWindow():

  toolbar_icon_size = 22

  left_arrow_img = FontAwesome.generate_icon('chevron-left', toolbar_icon_size)
  right_arrow_img = FontAwesome.generate_icon('chevron-right', toolbar_icon_size)

  def __init__(self, control, master):
    self.root = master
    self.window = Toplevel(self.root)
    self.window.minsize(220,300)
    self.window.title("Alimaster File Browser")
    self._setup_menu()

    self.frame = Frame(self.window, width=640,height=480)
    self.frame.pack_propagate(0)

    self.toolbar = Frame(self.frame, relief=RAISED)
    toolbar_icon_size = 17
    self.larrow = ImageTk.PhotoImage(FontAwesome.generate_icon('chevron-left', toolbar_icon_size))
    self.rarrow = ImageTk.PhotoImage(FontAwesome.generate_icon('chevron-right', toolbar_icon_size))
    self.homeimg = ImageTk.PhotoImage(FontAwesome.generate_icon('home', toolbar_icon_size))
    print ('eimg', self.left_arrow_img)
    self.back_b = Button(self.toolbar, style='Toolbar.TButton', image=self.larrow, command=lambda:print("left button")).pack(side=LEFT, padx=0, pady=2)
    self.forward_b = Button(self.toolbar, style='Toolbar.TButton', image=self.rarrow, command=lambda:print("right button")).pack(side=LEFT, padx=0, pady=2)
    self.home_b = Button(self.toolbar, style='Toolbar.TButton', image=self.homeimg, text='Home', command=lambda:print("GOHOME")).pack(side=LEFT, padx=(12,0), pady=2)
    self.search_b = Button(self.toolbar, style='Toolbar.TButton', text='Search', command=lambda:print("Search button")).pack(side=RIGHT, padx=2, pady=2)

    self.toolbar.pack(side=TOP, fill=X, expand=0)

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

    self.label = Label(self.content, text="Files").pack()



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
