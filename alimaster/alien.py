#
# alimaster/alien.py
#

import asyncio
import alimaster

class Alien:
    """
    Abstraction calls to ALICE home
    """

    def __init__(self):
        self.cnx = None

        self.loop = None

        self.is_connected = lambda: self.cnx != None

    def connect(self, username = ''):
        print ("Waiting for ROOT import")

        def _do_connection():
            print ("_do_connection")
            import ROOT
            assert hasattr(ROOT, 'TAlien'), "ROOT does not appear to have 'AliEn'"
            # self.cnx = ROOT.TGrid.Connect("alien://aliendb4.cern.ch:9000", username, 0, "-debug=1")
            self.cnx = ROOT.TGrid.Connect("alien://") # , 0, 0, "-debug=1")
            print ("Connected:", self.cnx)
            #self.cnx = ROOT.TGrid.Connect("alien://", None, None, 't')

        alimaster.on_root_import(_do_connection)


    def start(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        from multiprocessing import Process, Pipe
        parent_conn, child_conn = Pipe()
        # self.start_root_process(None, None)
        self.root_process = Process(target=self.start_root_process, args=(parent_conn, child_conn))
        self.root_process.start()

        self.loop.call_soon(self.root_listen, parent_conn, child_conn)

        # self.loop.call_later(0.2, self.connect, '')
        self.loop.run_forever()
        # print ("run forever is done")

    def start_root_process(self, inpipe, outpipe):
        from threading import current_thread
        # print ("[start_root_process]", current_thread())
        # print ("[start_root_process] Beginning to import ROOT")
        # import ROOT
        # self.connect('')
        # outpipe.send ("[start_root_process] Done")

        # print ("[start_root_process] DONE")

    def root_listen(self, in_pipe, out_pipe):

        @asyncio.coroutine
        def _loop():
            # yield from asyncio.sleep(0.3)
            self.on_root_message(in_pipe.recv())
            print ("[_loop] DONE LOOPING")

        asyncio.async(_loop())

    def on_root_message(self, msg):
        print ("[on_root_message]", msg)


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

    def kill(self):
        print ("KILL")
        self.loop.stop()

    def stop(self):
        """Stops the asyncio loop - thus ending the thread"""
        if self.loop:
            self.loop.call_soon_threadsafe(self.kill)
            print ("Alien Stopped")
