#
# alimaster/root_selector/__main__.py
#
"""
This file allows the root_selector subpackage to be runnable
"""

import sys

from alimaster.root_selector import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
