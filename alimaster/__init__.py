#
# alimaster/__init__.py
#
#
"""# AliMaster
AliMaster intends to be a utility for managing files and jobs on
CERN's grid through AliMonitor. It currently uses the commands provided by the AliEn
software package. Perhaps one day there will be python bindings to the services, but until
then, AliEn (and AliROOT, for that matter) should be installed before AliMaster (to do so,
follow the guide at https://dberzano.github.io/alice/install-aliroot.
"""

import alimaster.metadata

__version__   = metadata.version
__author__    = metadata.author
__date__      = metadata.date
__copyright__ = metadata.copyright
__license__   = metadata.license



__all__ = ['__version__', '__author__']

from .gui.mainwindow import MainWindow
from alimaster.application import Application


from os import path

def LOCAL(f):
  return path.join(path.dirname(__file__), f)

def RES(f):
  return LOCAL(path.join('res', f))
