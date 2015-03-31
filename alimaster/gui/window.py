#
# alimaster/gui/window.py
#
"""
Provides base window class for alimaster
"""

class Window():
    """
    A base class for handling the construction of alimaster gui-windows.
    """

    title = "Unnamed Window"
    min_size = (200, 200)

    def __init__(self, app, toplevel):
        """
        Constructs the window
        @param app: The application the window belongs to
        @param toplevel: A top-level
        """
        self.app = app

        if toplevel is None:
                self.window = self.app.get_new_window(self.title, self.min_size)
        else:
                self.window = toplevel
                self.window.minsize(*self.min_size)
                self.window.title(self.title)
        self.menu = None
        self.window.bind("<FocusIn>", self._on_focus)
        # self.window.protocol('WM_TAKE_FOCUS', self.on_focus)

    def close(self):
        self.toplevel.close()

    def hide(self):
        self.toplevel.hide()

    def _on_focus(self, ev):
        """
        A 'filter' function which propagates a focus event only if the main
        widget was the toplevel of the function
        """
        if ev.widget is not self.window:
            return
        self.on_focus(ev)

    def on_focus(self, ev):
        """Dummy function to give all windows an 'on_focus' event"""
        # print ("FOCUS", self, ev.widget)
        pass
