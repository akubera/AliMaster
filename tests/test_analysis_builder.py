#
# tests/test_analysis_builder.py
#

import alimaster.analysis_builder as analysis_builder

from tkinter import *

def test_creation():
    ab = analysis_builder.AliAnalysisBuilder(Tk())
