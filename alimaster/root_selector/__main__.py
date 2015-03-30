#
# runnable
#

import sys


import alimaster.root_selector.gui as gui

def main(args):
    window = gui.create_window()
    return window.mainloop()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
