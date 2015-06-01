#
# setup.py
#
"""
A (non-web) graphic user interface for interacting with AliMonitor
"""

import os
from glob import glob
from setuptools import (setup, find_packages)
from importlib.machinery import SourceFileLoader

metadata_path = os.path.join(".", "alimaster", "metadata.py")
metadata = SourceFileLoader("metadata", metadata_path).load_module()

REQUIRES = [
    'pillow',
    'OpenSSL'
]

EXTRAS = {
    ':python_version=="3.3"': ['asyncio>=0.2.1']
}

PACKAGES = find_packages(exclude=['tests'])

SCRIPTS = glob('scripts/*')

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "License :: OSI Approved :: GNU Lesser General Public License v3 or"
    " later (LGPLv3+)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Scientific/Engineering :: Physics",
    "Natural Language :: English"
]

setup(
    name=metadata.package,
    version=metadata.version,
    author=metadata.author,
    author_email=metadata.author_email,
    url=metadata.url,
    license=metadata.license,
    description=__doc__.strip(),
    packages=PACKAGES,
    scripts=SCRIPTS,
    install_requires=REQUIRES,
    extras_require=EXTRAS,
    classifiers=CLASSIFIERS
)
