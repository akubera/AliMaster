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


class Application:

  '''
  Main application class which houses multiple threads for gui and server communication.
  '''
  def __init__(self, *, opts={}, gui_thread=True, title='AliMaster Application', width=750, height=300, window_builder=Tk):
    '''
    @param opts: Extra configuration options
    @param gui_thread: If false, runs in current thread, if True, creates new thread, if thread runs in THAT thread
    @param title: Title of the main window
    @param window_builder: function providing the root window
    '''
    self.generate_window = window_builder
    self.window_info = {"w":width, "h":height, "title":title}

    # set the correct thread
    if gui_thread is True:
      self.gui_thread = Thread(name='GuiThread', target = self.main_gui_loop)
    elif isinstance(gui_thread, Thread):
      self.gui_thread = gui_thread
    else:
      self.gui_thread = threading.current_thread()

    self.alien = Alien()
    self.alien_thread = Thread(name="AlienThread", target= self.alien.wait_for_command)

  def _build_interface(self):
    print ("[_build_interface]")
    self.loop = new_event_loop()

    self.root = self.generate_window()

    img = ImageTk.PhotoImage(Image.open(alimaster.RES('icon.png')))



    self.root.tk.call('wm', 'iconphoto', self.root._w, img)
    # self.root.withdraw()
    self.root.minsize(500, 300)
    self.root.protocol("WM_DELETE_WINDOW", self.quit)
    self.root.title(self.window_info['title'])

    #from .gui.style import style
    #style.theme_use('alimaster')

    self._frame = Frame(self.root, width=self.window_info['w'], height=self.window_info['h'])
    self._frame.pack(fill=BOTH, expand=1)



  def handle_signals(self):
    from signal import (SIGINT, signal)

    def _stop(signum, frame):
      print("[_stop]", self, "Signal Caught", signum, frame)
      self.quit()

    signal(SIGINT, _stop)

  def quit(self):
    print("[QUIT]")
    self.root.after(0, self.root.quit)

  def main_gui_loop(self):
    self._build_interface()
    print("Running main gui loop in thread", threading.current_thread())
    self.root.mainloop()

  def run_in_thread(self):
    if self.gui_thread is None:
      raise Exception
    self.gui_thread.start()

  def run(self):
    self.main_gui_loop()

  def get_new_window(self):
    return self.generate_window()
