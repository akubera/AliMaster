#
# alimaster/gui/__init__.py
#

from os import path

from .. import __version__

def RES(filename):
    return path.join(path.dirname(__file__), 'res', filename)
