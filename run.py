#!/usr/bin/env python3
#
# run.py
#
'''
Run this script to start the program.
'''

import alimaster

from argparse import ArgumentParser

from tkinter import *
from tkinter.ttk import *

def main():

  parser = ArgumentParser()
  parser.add_argument("-c", "--conf", metavar="FILE", help="Load configuration")
  args = parser.parse_args()

  app  = alimaster.Application(opts = args, gui_thread=False)

  # main = alimaster.MainWindow()

  app.handle_signals()

  #app._build_interface()
  #app.root.mainloop()
  app.run()

  # app.run_in_thread()
  # app.gui_thread.join()
  print ("GUI has finished")

  # root.withdraw()
  # root.mainloop()

if __name__ == '__main__':
  main()
