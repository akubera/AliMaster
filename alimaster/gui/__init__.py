
from .. import __version__

from os import path

def RES(filename):
    return path.join(path.dirname(__file__), 'res', filename)
