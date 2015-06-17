#
# alimaster/analysis_builder/gui.py
#
"""
File creating the GUI for alimaster.analysis_builder
"""

from alimaster.gui.fontawesome import FontAwesome
from alimaster.gui import SimpleWindow

from tkinter import *       # noqa
from tkinter.ttk import *   # noqa

from .new_project_wizard import NewProjectWizard


class MainWindow(SimpleWindow):
    """
    Main window for the analysis_builder interface
    """

    img_size = 14
    small_img_size = 10

    imgs = {
        'new': FontAwesome.generate_icon('file-o', img_size),
        'open': FontAwesome.generate_icon('folder-o', img_size),
        'save': FontAwesome.generate_icon('floppy-o', img_size),
        'new_project': FontAwesome.generate_icon('cube', img_size),
        'project': FontAwesome.generate_icon('cube', small_img_size),
        'config': FontAwesome.generate_icon('gears', small_img_size),
        'file': FontAwesome.generate_icon('file', small_img_size),
    }

    def __init__(self, builder, root):
        """
        Construct the analysis builder window.

        @param root: TK object to be the root of this window
        """
        super().__init__(root, "AliMaster | Analysis Builder")
        self.window = self.frame
        self._setup_toolbar()
        self.frame = Frame(self.window)
        self._setup_statusbar()
        self._setup_content()
        self.frame.pack(expand=True, fill=BOTH)

    def _setup_toolbar(self):
        """Constructs the toolbar at the top of the window"""
        self.toolbar = Frame(self.window, relief=RAISED)

        def add_button(img_name, command=None):
            if command is None:
                command = lambda: print(img_name)
            Button(self.toolbar,
                   style='Toolbar.TButton',
                   image=self.imgs[img_name],
                   command=command).pack(side=LEFT, padx=0, pady=2)

        def add_separator():
            Separator(self.toolbar,
                      orient=VERTICAL).pack(side=LEFT, padx=1, pady=4, fill=Y)

        add_button('new_project', self.create_new_project_wizard)
        add_separator()
        add_button('new')
        add_button('open')
        add_button('save')

        self.toolbar.pack(side=TOP, fill=X, expand=0)

    def _setup_statusbar(self):
        """Constructs the statusbar at bottom of the window"""
        self.status = StringVar()
        self.statusbar = Label(self.window,
                               textvar=self.status,
                               font=("DejaVu Sans", -10),
                               relief='sunken')
        self.set_status = self.status.set
        self.set_status("")
        self.statusbar.pack(side=BOTTOM, fill=X, expand=0, pady=1)

    def _setup_content(self):
        """Constructs the tree on the left side of the window"""
        self.tree_view = Treeview(self.frame)
        self.tree_view.pack(fill=Y, side=LEFT, padx=6, pady=6)

        self.tabbed_view = Notebook(self.frame)
        self.tabbed_view.pack(fill=BOTH, side=RIGHT, expand=2, padx=6, pady=6)
        self.tab_frames = dict()

        a = self.tree_view.insert('',
                                  'end',
                                  image=self.imgs['project'],
                                  text='AnAnalysis')
        self.tree_view.insert(a,
                              'end',
                              image=self.imgs['config'],
                              text="config")
        self.tree_view.insert(a,
                              'end',
                              image=self.imgs['file'],
                              text="LambdaCut")


    def create_new_project_wizard(self):
        """Constructs and displays a NewProjectWizard window"""
        def cb():
            print("[create_new_project_wizard] callback")
        NewProjectWizard(Toplevel(self.window), cb)
