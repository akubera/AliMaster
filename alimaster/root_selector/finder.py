#
# alimaster/root_selector/finder.py
#


class Finder:
    """
    Searches for root installations
    """

    def Find(self, path):
        from glob import glob
        import os
        for root, dirnames, filenames in os.walk(path):
            if 'root-config' in filenames:
                print (root)
            # print (dirnames)
            # found = glob(path + "/**/root-config")
        # print ("Found", found)
