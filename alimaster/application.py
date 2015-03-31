#
# alimaster/application.py
#

from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

import threading
from threading import Thread
from asyncio import (new_event_loop)

from alimaster.alien import Alien

import alimaster
from .gui import MainWindow

class Application:
  """
  Main application class which houses multiple threads for gui and server communication.
  """

  _win_count = 0

  def __init__(self, *, opts={}, gui_thread=True, handle_signals=False, title='AliMaster Application', width=750, height=300, window_builder=Tk):
    """
    Construct the alimaster application
    @param opts: Extra configuration options
    @param gui_thread: If false, runs in current thread, if True, creates new thread, if thread runs in THAT thread
    @param handle_signals: Will automatically create a signal listener to catch and quit on SIGINT
    @param title: Title of the main window
    @param window_builder: function providing the root window
    """
    self.generate_window = window_builder
    self.window_info = {"w":width, "h":height, "title":title}

    # set the correct thread
    if gui_thread is True:
      self.gui_thread = Thread(name='GuiThread', target = self.main_gui_loop)
    elif isinstance(gui_thread, Thread):
      self.gui_thread = gui_thread
    else:
      self.gui_thread = threading.current_thread()

    if handle_signals:
      self.handle_signals()

    self.alien = Alien()
    # self.alien.connect('')
    self.alien_thread = Thread(name="AlienThread", target= self.alien.start)
    self.alien_thread.start()


  def _build_interface(self):
    print ("[_build_interface]")
    self.loop = new_event_loop()

    self.root = self.generate_window()

    from .gui.style import get_style
    get_style().theme_use('alimaster')

    self.logo = ImageTk.PhotoImage(Image.open(alimaster.RES('icon.png')))
    self.root.withdraw()
    self.root.protocol("WM_DELETE_WINDOW", self.quit)

    # self.mwin = self.get_new_window(self.window_info['title'], (400,300))

    #from .gui.style import style

    # self._frame = Frame(self.mwin, width=self.window_info['w'], height=self.window_info['h'])
    # self._frame.pack(fill=BOTH, expand=1)

    self.main_window = MainWindow(self)
    # self.root = self.generate_window()


  def handle_signals(self):
    from signal import (SIGINT, signal)

    def _stop(signum, frame):
      print("[_stop]", self, "Signal Caught", signum, frame)
      self.quit()

    signal(SIGINT, _stop)

  def quit(self):
    print("[QUIT]")
    self.alien.stop()
    self.alien_thread.join()
    print ("[quit] joined with alien thread")
    self.root.after(0, self.root.quit)
    return True

  def main_gui_loop(self):
    print("Running main gui loop in thread", threading.current_thread())
    self._build_interface()
    alimaster.keep_tk_awake(self.root)
    self.root.mainloop()

  def run_in_thread(self):
    if self.gui_thread is None:
      raise Exception
    self.gui_thread.start()

  def run(self):
    if threading.current_thread() == self.gui_thread:
      self.main_gui_loop()
    else:
      self.gui_thread.start()
      self.gui_thread.join()

  def _release_window(self, window):
    def _doit():
      self._win_count -= 1
      if self._win_count == 0:
        self.quit()
      window.destroy()
    return _doit

  def get_new_window(self, title, minsize = (500, 300)):
    res = Toplevel(self.root)
    res.minsize(*minsize)
    res.protocol("WM_DELETE_WINDOW", self._release_window(res))
    res.tk.call('wm', 'iconphoto', res._w, self.logo)
    res.title(title)
    self._win_count += 1
    return res
