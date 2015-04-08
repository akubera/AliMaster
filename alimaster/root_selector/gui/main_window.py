#
# alimaster/root_selector/gui/main_window.py
#
"""
The main window for the root_selector alimaster subpackage.
"""

import asyncio
import threading
import subprocess
import os

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

from alimaster.root_selector.finder import Finder

class MainWindow():

    def __init__(self, root):
        """
        Construct the main window of the root_selector program
        """
        print ("[MainWindow::__init__]")
        self.root = root
        self.root.title("AliMaster | ROOT Selector")
        self.root.protocol("WM_DELETE_WINDOW", self.stop_tk_root)
        self.root.minsize(400,200)

        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)

        # self.lbl = Label(self.frame , text="ROOT Selector")
        # self.lbl.pack(anchor='nw')

        self.search_button = Button(self.frame, text="Search", command=self.open_searchbox)
        self.search_button.pack()

        self.rootlist = Treeview(self.frame)
        self.rootlist['columns'] = ('version') # , 'modified', 'owner')
        # self.rootlist.heading('', text='path')
        self.rootlist.heading('version', text='version')
        # self.rootlist.heading('owner', text='owner')
        self.rootlist.pack(fill=BOTH, expand=1, padx=2, pady=3)

        self.use_button = Button(self.frame, text="Use", command=self.open_searchbox,state=DISABLED)
        # self.use_button.state=DISABLED
        self.use_button.state(["disabled"])
        self.use_button.pack(anchor='se')


        self.frame.pack()

        # master = self.frame
        # self.btn = Button(master , text = "Button" , command = self.command )
        # self.btn.pack()
        print ("[MainWindow::__init__] Done.")

    def stop_tk_root(self):
        self.root.after(0, self.root.quit)

    def command(self):
        print ('Button is pressed!')

        self.newWindow = tk.Toplevel(self.master)
        self.app = windowclass1(self.newWindow)

    def open_searchbox(self):
        from tkinter import filedialog
        from queue import Queue

        d = filedialog.askdirectory()
        if not d:
            return

        # self.rootlist.insert('', 'end', 'ROOT', text=root_path)

        q = Queue()

        # @asyncio.coroutine
        def threaded_find_roots():
            print ("Searching for ROOTs in path",d)
            # for x in range(4):
            finder = Finder()
            for root_path in finder.find(d):
                # q.put(root_path)
                meta = {}
                exe = os.path.join(root_path,'root-config')
                meta['version'] = subprocess.check_output([exe, "--version"])
                meta['features'] = subprocess.check_output([exe, "--features"])
                # print ('found root path:', root_path)
                self.insert_item(root_path, meta)
                print ("GOOD")
                # yield from asyncio.sleep(1)
                # self.rootlist.insert('','end',x, text=x )

        thread = threading.Thread(name='FindRoot', target=threaded_find_roots)
        thread.start()

        # asyncio.get_event_loop().run_until_complete(asyncio_find_roots())

        # print ("selected",d)
        # finder = Finder()
        # for root_path in finder.Find(d):
            # self.rootlist.insert('', 'end', 'ROOT', text=root_path)

        # self.searchbox = Toplevel(self.root)
        # searchframe = Frame(self.searchbox)
        # label = Label(searchframe, text="Search Path:")

        # label.pack()
        # searchframe.pack()

    def insert_item(self, item, extras=[]):
        from _tkinter import TclError
        key = self.rootlist.insert('', 'end', text=item)
        newitem = self.rootlist.item(key)
        print ('key', key.__class__)
        print ('new', newitem.__class__)
        for header, value in extras.items():
            value = value.decode()
            print ('adding', header, ':', value)
            try:
                self.rootlist.set(key, header, value)
            except AttributeError:
                pass
            except TclError:
                pass
        print ('[insert_item] DONE')
