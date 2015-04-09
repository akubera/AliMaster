#
# alimaster/analysis_builder/__main__.py
#

import sys

from tkinter import *
from tkinter.ttk import *

from argparse import ArgumentParser

# from alimaster.analysis_builder.analysis_builder
from .alianalysis_builder import AliAnalysisBuilder


def main(args):
    """
    Main function launching analysis_builder
    """
    parser = ArgumentParser(description="GUI helper for creating AliAnalysis scripts")
    parser.add_argument("-c", "--conf", metavar="FILE", help="Load configuration")
    parser.add_argument("-v", "--verbose", dest='verbose', action='store_true', help="Print helpful information")
    args = parser.parse_args(args)

    root = Tk()
    gui = AliAnalysisBuilder(root)
    gui.run()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
