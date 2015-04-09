#
# alimaster/analysis_builder/analysis_builder.py
#
"""
The Analysis Builder package will offer an easy and extendable interface for
creating analysis scripts for use with an AliAnalysis
"""

from alimaster.analysis_builder.gui import MainWindow

class AliAnalysisBuilder:

    def __init__(self, root):
        self.root = root
        self.window = MainWindow(self, root)

    def run(self):
        self.root.mainloop()
