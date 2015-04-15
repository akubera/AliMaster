#
# alimaster/gui/mainwindow.py
#

from tkinter import *
from tkinter.ttk import *

from alimaster import __version__
from .filebrowser import FileBrowserWindow
from .help_window import HelpWindow
from .settings_window import SettingsWindow

import alimaster

import threading
from threading import Thread


class MainWindow():
    """
    The main window which holds some status about the ALIEN connection and
    provides buttons which load all the other alimaster windows.

    If there are other child windows open, the MainWindow will not close, but
    minimize to taskbar.
    """"

    def __init__(self, app):
        """
        Create the main 'control' window of the AliMaster program
        """
        self.app = app
        self.root = app.root

        self.window = app.get_new_window("Alimaster Control", (220, 500))
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        # self.window = Toplevel(master)
        # self.window.minsize(220,500)
        # self.window.title("Alimaster Control")
        # self.window.protocol("WM_DELETE_WINDOW", self.hide)

        # self.style = Style()
        # GenerateStyle(self.style)
        # status_style.configure("StatusGood.TLabel", foreground="green")
        # status_style.configure("StatusBad.TLabel", foreground="red")

        self.frame = Frame(self.window)

        self.status_bar = Frame(self.frame)

        self.status_bar.label = Label(self.status_bar,
                                      text="Status"
                                      ).pack(side=LEFT)

        self.status_bar.status = Label(self.status_bar,
                                       text="●"
                                       ).pack()

        self.label = Label(self.frame,
                           text="AliMaster v%s" % (__version__),
                           font=('DejaVu Mono', 16)
                           ).pack(pady=9, padx=4)

        self.status_bar.pack(fill=X, pady=(9, 3), padx=4)

        self.file_browser_button = Button(self.frame,
                                          text="File Browser",
                                          command=self.create_filebrowser
                                          ).pack(fill=X, pady=(9, 3), padx=4)

        self.settings_button = Button(self.frame,
                                      text="Settings",
                                      command=self.create_settings_window
                                      ).pack(fill=X, pady=(9, 3), padx=4)

        self.help_button = Button(self.frame,
                                  text="Help",
                                  command=self.create_helpwindow
                                  ).pack(fill=X, pady=(9, 3), padx=4)

        self.load_button = Button(self.frame,
                                  text="Load ROOT",
                                  command=self.load_root
                                  ).pack(fill=X, pady=(3, 3), padx=4)
        self.quit_button = Button(self.frame,
                                  text="Quit",
                                  command=self.app.quit
                                  ).pack(fill=X, pady=(3, 9), padx=4)

        self.set_status_good()
        self.frame.pack(fill=BOTH, expand=1)

    def quit(self):
        print("[MainWindow::quit]")
        self.root.after(0, self.root.quit)

    def hide(self):
        self.window.withdraw()

    def show(self):
        self.window.update()

    def close(self):
        print('window_count', self.app._win_count)
        if self.app._win_count < 2:
            self.app.quit()
        else:
            self.window.iconify()

    def create_filebrowser(self):
        FileBrowserWindow(self.app)

    def create_helpwindow(self):
        HelpWindow(self.app)

    def create_settings_window(self):
        SettingsWindow(self.app)

    def set_status_bad(self):
        self.status_bar.status.configure(style='StatusBad.TLabel')

    def set_status_good(self):
        from .style import style
        self.status_bar.status.configure(style='StatusGood.TLabel')

    def run_in_thread():
        pass

    def load_root(self):
        alimaster.import_root_module()
