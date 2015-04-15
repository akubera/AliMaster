#
# alimaster/gui/window.py
#
"""
Provides base window class for alimaster
"""

from .simple_window import SimpleWindow

class Window(SimpleWindow):
    """
    A base class for handling the construction of alimaster gui-windows.
    """

    title = "Unnamed Window"
    min_size = (200, 200)

    def __init__(self, app, toplevel=None):
        """
        Constructs the window
        @param app: The application the window belongs to
        @param toplevel: A top-level
        """
        self.app = app

        if toplevel is None:
            toplevel = self.app.get_new_window(self.title, self.min_size)

        super().__init__(toplevel,
                         self.title,
                         self.min_size,
                         auto_close_window=False)
        self.window = toplevel

    def close(self):
        self.toplevel.close()

    def hide(self):
        self.toplevel.hide()

    def on_focus(self, ev):
        """Dummy function to give all windows an 'on_focus' event"""
        # print ("FOCUS", self, ev.widget)
        pass
