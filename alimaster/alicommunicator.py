#
# alimaster/alicommunicator.py
#

import asyncio

class AliCommunicator():
  """
  The AliCommunicator provides a simple interface for sending and retrieving messages
  to the ALICE grid.
  """
  
  def __init__(self, loop = None, run_forever=True):
    """
    Creates a communicator.

    @param loop: The event loop on which to call things asynchronously
    @type loop: asyncio.EventLoop
    """
    if not loop and os.name == 'nt':
      loop = asyncio.ProactorEventLoop()

    self.loop = asyncio.get_event_loop() if not loop else loop
    asyncio.set_event_loop(loop)
    self._start()
    if run_forever: self.run_forever();

  @asyncio.coroutine
  def run(self, args):
    create = asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE)
    proc = yield from create

    # Read one line of output
    data = yield from proc.stdout.readline()
    line = data.decode().rstrip()

    # Wait for the subprocess exit
    yield from proc.wait()
    return line

  def _start(self):
     self.loop.run_until_complete(self._server_listen())

  def run_forever():
     self.loop.run_forever()
