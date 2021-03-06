#
# alimaster/root_selector/gui/main_window.py
#
"""
The main window for the root_selector alimaster subpackage.
"""

import threading
import subprocess
import os

from tkinter import *                                                    # noqa
from tkinter.ttk import *                                                # noqa

from alimaster.root_selector.finder import Finder
from alimaster.gui.fontawesome import FontAwesome
from alimaster.gui import SimpleWindow


class MainWindow(SimpleWindow):

    img_size = 16

    imgs = {
        'search': FontAwesome.generate_icon('search', img_size),
    }

    def __init__(self, root):
        """
        Construct the main window of the root_selector program
        """
        print("[MainWindow::__init__]")
        super().__init__(root, "AliMaster | ROOT Selector", (400, 200))

        search_img = self.imgs['search']
        self.search_img = search_img

        self.aliroot_frame = Frame(self.frame)

        self.aliroot_search_button = Button(self.aliroot_frame,
                                            image=search_img,
                                            text='Search',
                                            command=self.search_for_aliroot)
        self.aliroot_search_button.pack(side=LEFT)

        self.aliroot_lbl = Label(self.aliroot_frame, text="AliRoot")
        self.aliroot_lbl.pack(side=LEFT)
        self.aliroot_frame.pack(side=TOP, fill=X, pady=(6, 0), padx=8)

        self.alirootlist = Treeview(self.frame)
        self.alirootlist['columns'] = ('version')
        # , 'modified', 'owner')
        self.alirootlist.heading('#0', text='Path')
        self.alirootlist.heading('version', text='version')
        # self.rootlist.heading('owner', text='owner')
        self.alirootlist.pack(fill=BOTH, expand=1, padx=4, pady=5)

        sep = Separator(self.frame, orient=HORIZONTAL)
        sep.pack(fill=X, padx=10)

        self.root_frame = Frame(self.frame)

        self.root_search_button = Button(self.root_frame,
                                         image=search_img,
                                         text="Search",
                                         command=self.search_for_root,
                                         )
        self.root_search_button.pack(side=LEFT)

        self.aliroot_lbl = Label(self.root_frame, text="ROOT")
        self.aliroot_lbl.pack(side=LEFT)
        self.root_frame.pack(side=TOP, fill=X, pady=(6, 0), padx=8)

        self.rootlist = Treeview(self.frame)
        self.rootlist.heading('#0', text='ROOTSYS')
        self.rootlist['columns'] = ('version')  # , 'modified', 'owner')
        self.rootlist.heading('version', text='version')
        # self.rootlist.heading('owner', text='owner')
        self.rootlist.pack(fill=BOTH, expand=1, padx=4, pady=5)

        self.use_button = Button(self.frame,
                                 text="Use",
                                 command=self.set_selected_item,
                                 )
        self.use_button.state(["disabled"])
        self.use_button.pack(anchor='se')

        self.frame.pack()

        # master = self.frame
        # self.btn = Button(master , text = "Button" , command = self.command )
        # self.btn.pack()
        print("[MainWindow::__init__] Done.")

    def command(self):
        print('Button is pressed!')

        self.newWindow = tk.Toplevel(self.master)
        self.app = windowclass1(self.newWindow)

    def search_for_aliroot(self):
        finder = Finder()
        aliroot = self.open_searchbox(finder.find_aliroot)
        return aliroot

    def search_for_root(self):
        finder = Finder()
        self.open_searchbox(finder.find_root)

    def open_searchbox(self, fcn=None):
        from tkinter import filedialog

        d = filedialog.askdirectory()
        if not d:
            return None

        # self.rootlist.insert('', 'end', 'ROOT', text=root_path)

        # @asyncio.coroutine
        def threaded_find_roots():
            print("Searching for ROOTs in path", d)

            for root_path in Finder.find_root(d):
                meta = {}
                exe = os.path.join(root_path, 'root-config')
                meta['rootsys'] = subprocess.check_output([exe, "--prefix"])
                meta['version'] = subprocess.check_output([exe, "--version"])
                meta['features'] = subprocess.check_output([exe, "--features"])
                # print('found root path:', root_path)
                self.insert_item(meta['rootsys'], meta)
                print("GOOD")
                # yield from asyncio.sleep(1)
                # self.rootlist.insert('','end',x, text=x )

        thread = threading.Thread(name='FindRoot', target=threaded_find_roots)
        thread.start()

        # asyncio.get_event_loop().run_until_complete(asyncio_find_roots())

        # print("selected",d)
        # finder = Finder()
        # for root_path in finder.Find(d):
        #     self.rootlist.insert('', 'end', 'ROOT', text=root_path)

        # self.searchbox = Toplevel(self.root)
        # searchframe = Frame(self.searchbox)
        # label = Label(searchframe, text="Search Path:")

        # label.pack()
        # searchframe.pack()

    def insert_item(self, item, extras={}):
        from _tkinter import TclError
        key = self.rootlist.insert('', 'end', text=item)
        newitem = self.rootlist.item(key)
        print('key', key.__class__)
        print('new', newitem.__class__)
        for header, value in extras.items():
            value = value.decode()
            print('adding', header, ':', value)
            try:
                self.rootlist.set(key, header, value)
            except AttributeError:
                pass
            except TclError:
                pass
        print('[insert_item] DONE')

    def set_selected_item(self):
        pass
