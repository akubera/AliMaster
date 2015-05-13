#
# alimaster/root_selector/__init__.py
#
"""
A package which helps the user select the version of root to load.
"""

import alimaster
# import gui as gui
from .gui import create_window

from .finder import Finder

from alimaster.root_selector.__main__ import main
