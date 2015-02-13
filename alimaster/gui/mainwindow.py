#
# alimaster/gui/mainwindow.py
#

from tkinter import *
from tkinter.ttk import *

from . import __version__
from .filebrowser import FileBrowserWindow

import threading
from threading import Thread

class MainWindow():

  def __init__(self, app):
    '''Create the main 'control' window of the AliMaster program'''
    self.app = app
    self.root = app.root

    self.window = app.get_new_window("Alimaster Control", (220, 500))

    # self.window = Toplevel(master)
    # self.window.minsize(220,500)
    # self.window.title("Alimaster Control")
    # self.window.protocol("WM_DELETE_WINDOW", self.hide)

    #self.style = Style()
    #GenerateStyle(self.style)
    # status_style.configure("StatusGood.TLabel", foreground="green")
    # status_style.configure("StatusBad.TLabel", foreground="red")

    self.frame = Frame(self.window)
    self.status_bar = Frame(self.frame)
    self.status_bar.label = Label(self.status_bar, text="Status")
    self.status_bar.label.pack(side=LEFT)
    self.status_bar.status = Label(self.status_bar, text="●")
    self.status_bar.status.pack()
    
    self.label = Label(self.frame, text="AliMaster v%s" % (__version__), font=('DejaVu Mono', 16)).pack(pady=9, padx=4)
    self.status_bar.pack(fill=X, pady=(9,3), padx=4)

    self.help = Button(self.frame, text="Help", command=self.set_status_bad)
    self.quit = Button(self.frame, text="Quit", command= self.quit)
    self.file_browser = Button(self.frame, text="File Browser", command=self.create_filebrowser)

    self.file_browser.pack(fill=X, pady=(9,3), padx=4)
    self.help.pack(fill=X, pady=(9,3), padx=4)
    self.quit.pack(fill=X, pady=(3,9), padx=4)
    self.set_status_good()

    self.frame.pack(fill=BOTH, expand=1)

  def quit(self):
    print ("[MainWindow::quit]")
    self.root.after(0, self.root.quit)

  def hide(self):
    self.window.withdraw()

  def show(self):
    self.window.update()

  def create_filebrowser(self):
    FileBrowserWindow(self, self.root)

  def set_status_bad(self):
    self.status_bar.status.configure(style = 'StatusBad.TLabel')
    
  def set_status_good(self):
    from .style import style
    self.status_bar.status.configure(style = 'StatusGood.TLabel')

  def run_in_thread():
    pass
