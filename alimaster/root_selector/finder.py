#
# alimaster/root_selector/finder.py
#

import asyncio

class Finder:
    """
    Searches for root installations
    """

    def find(self, path):
        from glob import glob
        import os
        for root, dirnames, filenames in os.walk(path):
            if 'root-config' in filenames:
                yield root
            # print (dirnames)
            # found = glob(path + "/**/root-config")
        # print ("Found", found)

    @asyncio.coroutine
    def find_async(self, path):
        yield from self.Find(path)
