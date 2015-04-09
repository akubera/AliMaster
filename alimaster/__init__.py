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
import os, sys
from importlib.machinery import SourceFileLoader
from os import path

# from analysis_builder import 

# from alimaster import metdata
# ospath =
metadata = SourceFileLoader("metadata", path.join(path.dirname(__file__),"metadata.py")).load_module()

__version__   = metadata.version
__author__    = metadata.author
__date__      = metadata.date
__copyright__ = metadata.copyright
__license__   = metadata.license

__all__ = ['__version__', '__author__']

def LOCAL(f):
  return path.join(path.dirname(__file__), f)

def RES(f):
  return LOCAL(path.join('res', f))

def load_config(file):
    """
    Loads the alimaster configuration file named 'file' from the alimaster
    configuration directory. This directory is currently forced to be:
        $HOME/.config/alimaster
    this might be favoring unix users, but until a windows developer wants to
    show how to fix this, we're going to use this.
    """
    conf_dir = path.expanduser("~/.config")
    if not path.isdir(conf_dir):
        os.mkdir(conf_dir)
    alimaster_conf = conf_dir + "/alimaster"
    if not path.isdir(alimaster_conf):
        os.mkdir(alimaster_conf)
    conf_file = path.join(alimaster_conf, file)
    return open(conf_file, 'r+')

def keep_tk_awake(tk_root):
    tk_root.after(1, lambda *args: keep_tk_awake(tk_root))

_root_load_callbacks = []
def on_root_import(func):
    """
    Once the ROOT module is loaded, run func. This runnable is stored in a list
    and each is run in a first-come first-served way. These are run from the
    main application thread.
    If ROOT is already loaded, the function runs immediately in the caller's
    thread.
    """
    global _root_load_callbacks
    if "ROOT" not in sys.modules:
        _root_load_callbacks.append(func)
    else:
        func()

def import_root_module():
    global _root_load_callbacks
    print ("Importing ROOT module", end='... ')
    import ROOT
    print ("Done.")
    gROOT = ROOT.gROOT
    print ("""===================
      ROOT
~~~~~~~~~~~~~~~~~~~
 Version: {}
    Date: {}
  Module: {}
   Alien: {}
  Minuit: {}
  Thread: {}
  Libraries: {}
===================""".format(gROOT.GetVersion(),
                              gROOT.GetVersionDate(),
                               ROOT.__file__,
                               hasattr(ROOT, 'TMinuit'),
                               hasattr(ROOT, 'TAlien'),
                               hasattr(ROOT, 'TThread'),
                               ROOT.gSystem.GetLibraries()
                             ))

    [func() for func in _root_load_callbacks]

from .gui.mainwindow import MainWindow
from alimaster.application import Application

from .alicommunicator import AliCommunicator

# import aliroot
