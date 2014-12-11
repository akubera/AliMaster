#
# alimaster/alien.py
#

import asyncio

class Alien:

  def __init__(self):
    self.cnx = None

    self.loop = asyncio.new_event_loop()

    self.is_connected = lambda: self.cnx != None

  def connect(self, username):

    import ROOT

    assert hasattr(ROOT, 'TAlien'), "ROOT does not appear to have 'AliEn'"

    # self.cnx = ROOT.TGrid.Connect("alien://aliendb4.cern.ch:9000", username, 0, "-debug=1")
    self.cnx = ROOT.TGrid.Connect("alien://", None, None, 't')

  def wait_for_command():
    pass

  @asyncio.coroutine
  def insert_command(self, cmd, *args):
    pass

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



