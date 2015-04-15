#
# alimaster/gui/settings_window.py
#
"""
A GUI window for managing user settings.
"""

from tkinter import *
from tkinter.ttk import *

from .window import Window

class SettingsWindow(Window):

    title = "Settings | AliMaster"
    min_size = (500, 200)

    def __init__(self, app, mainwindow=None):
        """
        Construct the settings window
        """
        super().__init__(app, mainwindow)

        self.content_frame = Frame(self.frame)

        self.tree_view = Treeview(self.content_frame)
        self.tree_view.pack(fill=Y, side=LEFT, padx=6, pady=6)

        self.tabbed_view = Notebook(self.content_frame)
        self.tabbed_view.pack(fill=BOTH, side=RIGHT, expand=2, padx=6, pady=6)

        self.content_frame.pack(fill=BOTH, expand=1)
        self.tab_frames = dict()

        # self.add_tab("General")
        self.authentication_tab(self.add_tab("Authentication"))

        self.button_frame = Frame(self.frame)
        Button(self.button_frame,
               text="SAVE",
               command=self.save_settings,
               ).pack(side=RIGHT, padx=6, pady=(0, 4))
        Button(self.button_frame,
               text="CANCEL",
               command=self.close
               ).pack(side=RIGHT, pady=(0, 4))
        self.button_frame.pack(side=BOTTOM, fill=X)

    def save_settings(self):
        print("Saving settings...")

    def add_tab(self, name, frame=None):
        if name not in self.tab_frames:
            if frame is None:
                frame = Frame(self.tabbed_view)
            frame.pack(fill=BOTH, expand=1)
            self.tabbed_view.add(frame, text=name)
            self.tab_frames[name] = frame
        return self.tab_frames[name]

    def general_tab(self):
        pass

    def authentication_tab(self, frame):
        frame.cert_location = StringVar()
        from os import path
        frame.cert_location.set(path.expanduser("$HOME/.globus"))
        msg = ("Settings for your authentication to the ALICE grid. This is "
               "usually in the form of a CERN assigned X.509 RSA certificate."
               "")
        Label(frame, text=msg).pack(padx=4, pady=4, anchor=NW, fill=X)

        cert_frame = frame.cert_frame = Frame(frame)
        Label(cert_frame, text="Certificate Location: ").grid(row=0, column=0)
        Entry(cert_frame, textvar=frame.cert_location).grid(row=0, column=1, sticky='ew')
        Button(cert_frame, text="Find").grid(row=0, column=2, sticky='e')
        cert_frame.info_frame = Frame(cert_frame)
        cert_frame.info_frame.grid(row=1,columnspan=3,sticky='ew')

        self.update_certificate_info()
        cert_frame.pack(fill=X)

    def update_certificate_info(self):
        f = self.tab_frames['Authentication']
        Label(f.cert_frame.info_frame, text="IT WORKS").pack()
