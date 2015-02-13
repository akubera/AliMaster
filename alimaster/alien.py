#
# alimaster/alien.py
#

import asyncio

class Alien:

  def __init__(self):
    self.cnx = None

    self.loop = None

    self.is_connected = lambda: self.cnx != None

  def connect(self, username):

    import ROOT

    assert hasattr(ROOT, 'TAlien'), "ROOT does not appear to have 'AliEn'"

    # self.cnx = ROOT.TGrid.Connect("alien://aliendb4.cern.ch:9000", username, 0, "-debug=1")
    self.cnx = ROOT.TGrid.Connect("alien://", None, None, 't')

  def wait_for_command(self):
    self.loop = asyncio.new_event_loop()
    self.continue_looping = True
    asyncio.set_event_loop(self.loop)
    self.loop.run_forever()
    # print ("run forever is done")

  def call(self, cb, cmd, *args):
    self.loop.call_soon_threadsafe(self._insert_command, cb, cmd, args)

  def ls(self, cb, path = '.'):
    self.loop.call_soon_threadsafe(self._insert_command, cb, 'ls', path)

  def PWD(self, cb):
    self.loop.call_soon_threadsafe(self._insert_command, cb, 'pwd')

  def _insert_command(self, callback, cmd, *args):
    print ('[_insert_command]', cmd)
    res = [1,2,3]
    callback(res)

  def pwd(self):
    return self.insert_commandself.cnx.Pwd()

  def _pwd(self):
    return self.cnx.Pwd()

  def _ls(self, path = ''):
    res = self.cnx.Ls(path)
    return [res.GetFileName(i) for i in range(0,res.GetEntries())]

  def ls_gen(self, path = ''):
    res = self.cnx.Ls(path)
    yield from [res.GetFileName(i) for i in range(0,res.GetEntries())]


  def stop(self):
    """Stops the asyncio loop - thus ending the thread"""
    if self.loop:
      self.loop.call_soon_threadsafe(self.loop.stop) 
      # print ("Alien Stopped")
