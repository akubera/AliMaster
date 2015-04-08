#
# alimaster/root_selector/finder.py
#

import asyncio

class Finder:
    """
    Searches for root installations
    """

    @classmethod
    def find_root(cls, path):
        """
        Uses standard library os.walk to walk the path, looking for any
        directories that contain the file 'root-config'. This is a generator.
        """
        from glob import glob
        import os
        for root, dirnames, filenames in os.walk(path):
            if 'root-config' in filenames:
                yield root

    @classmethod
    def find_aliroot(cls, path):
        """
        Uses standard library os.walk to walk the path, looking for any
        directories that contain the executable file 'aliroot'. This is assumed
        to be the 'bin' directory of the aliroot installation, and the parent
        path is returned. This is a generator.
        """
        from glob import glob
        import os
        for root, dirnames, filenames in os.walk(path):
            if 'aliroot' in filenames:
                yield root
