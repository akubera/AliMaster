#!/usr/bin/env python3.4
#
# alimaster/__main__.py
#

import alimaster

from tkinter import *
from tkinter.ttk import *

from argparse import ArgumentParser

import logging

ARGUMENTS = [
    {
        "tacks" : ['-c', '--conf'],
        "metavar" : "FILE",
        "help" : "Load Configuration"
    },
    {
        "tacks" : ['-v', '--verbose'],
        "dest" : "verbose",
        "action" : "store_true",
        "help": "Print helpful debugging information"
    },
    {
        "tacks" : ['--use_separate_gui_thread'],
        "dest" : "gui_thread",
        "action" : "store_true",
        "help": "Runs gui in separate thread. Will probably break things!"
    }
]

def main(args):
  """
  Main function of the alimaster suite.
  This sets up the environment and loads the alimaster application
  """
  global ARGUMENTS
  parser = ArgumentParser('alimaster')
  for arg in ARGUMENTS:
      tacks = arg['tacks']
      del arg['tacks']
      parser.add_argument(*tacks, **arg)
  args = parser.parse_args()

  log = logging.getLogger('lout')
  log.setLevel(logging.DEBUG if args.verbose else logging.INFO)

  log.info("Alimaster starting with config file '%s'" % (args.conf))

  app  = alimaster.Application(opts=args, gui_thread=args.gui_thread)
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
  sys.exit(main(sys.argv[1:]))
