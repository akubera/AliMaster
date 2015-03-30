#
# setup.py
#

import os
from importlib.machinery import SourceFileLoader
metadata = SourceFileLoader("metadata", os.path.join(".","alimaster","metadata.py")).load_module()


from setuptools import setup

setup(       name = metadata.package,
          version = metadata.version,
    	     author = metadata.author,
   	 author_email = metadata.author_email,
              url = metadata.url,
          license = metadata.license,
      description = "A (non-web) graphic user interface for interacting with AliMonitor",
 long_description = """AliMaster intends to be a utility for managing files and jobs on
 CERN's grid through AliMonitor. It currently uses the commands provided by the AliEn
 software package. Perhaps one day there will be python bindings to the services, but until
 then, AliEn (and AliROOT, for that matter) should be installed before AliMaster (to do so,
 follow the guide at https://dberzano.github.io/alice/install-aliroot.)""",

         packages = ['alimaster'],
          scripts = ['scripts/alimaster'],

 install_requires = ['tkinter', 'pillow'],
   extras_require = {':python_version=="3.3"': ['asyncio>=0.2.1']},

      classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Scientific/Engineering :: Physics",
        "Natural Language :: English"
      ]
)
