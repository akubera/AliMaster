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

__version__ = '0.0.1'
__author__ = 'Andrew Kubera'
__author_email__ = 'andrew.michael.kubera@cern.ch'

__all__ = ['__version__', '__author__', '__author_email__']

from .gui.mainwindow import MainWindow


