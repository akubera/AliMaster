#
# alimaster/analysis_builder/gui.py
#
"""
File creating the GUI for alimaster.analysis_builder
"""

import alimaster
from alimaster.gui.fontawesome import FontAwesome
from alimaster.gui import SimpleWindow

from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

class MainWindow(SimpleWindow):
    """
    Main window for the analysis_builder interface
    """

    img_size = 14

    imgs = {
        'save': FontAwesome.generate_icon('search', img_size)
    }

    def __init__(self, root):
        """
        Construct the analysis builder window.

        @param root: TK object to be the root of this window
        """
        super().__init__(root, "AliMaster | Analysis Builder")
