#
# alimaster/gui/utils.py
#
"""
Miscellaneous functions for gui tasks
"""

from os import path


def RES(filename):
    """
    Return absolute path to resource file with name 'filename'.

    @param filename: Name of the file in the alimaster/gui/res directory
    """
    abspath = path.abspath(path.dirname(__file__))
    return path.join(abspath, 'res', filename)
