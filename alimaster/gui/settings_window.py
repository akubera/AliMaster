#
# alimaster/gui/settings_window.py
#
"""
A GUI window for managing user settings.
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror

from .window import Window

class SettingsWindow(Window):

    title = "Settings | AliMaster"
    min_size = (500, 200)

    def __init__(self, app, mainwindow=None):
        """
        Construct the settings window
        """
        super().__init__(app, mainwindow)

        self.content_frame = Frame(self.frame)

        self.tree_view = Treeview(self.content_frame)
        self.tree_view.pack(fill=Y, side=LEFT, padx=6, pady=6)

        self.tabbed_view = Notebook(self.content_frame)
        self.tabbed_view.pack(fill=BOTH, side=RIGHT, expand=2, padx=6, pady=6)

        self.content_frame.pack(fill=BOTH, expand=1)
        self.tab_frames = dict()

        # self.add_tab("General")
        self.authentication_tab(self.add_tab("Authentication"))

        self.button_frame = Frame(self.frame)
        Button(self.button_frame,
               text="SAVE",
               command=self.save_settings,
               ).pack(side=RIGHT, padx=6, pady=(0, 4))
        Button(self.button_frame,
               text="CANCEL",
               command=self.close
               ).pack(side=RIGHT, pady=(0, 4))
        self.button_frame.pack(side=BOTTOM, fill=X)

    def save_settings(self):
        print("Saving settings...")

    def add_tab(self, name, frame=None):
        if name not in self.tab_frames:
            if frame is None:
                frame = Frame(self.tabbed_view)
            frame.pack(fill=BOTH, expand=1)
            self.tabbed_view.add(frame, text=name)
            self.tab_frames[name] = frame
        return self.tab_frames[name]

    def general_tab(self):
        pass

    def authentication_tab(self, frame):
        from os import path

        frame.cert_location = StringVar()
        frame.cert_location.set(path.expanduser("~/.globus/usercert.pem"))

        msg = ("Settings for your authentication to the ALICE grid. This is "
               "usually in the form of a CERN assigned X.509 RSA certificate."
               "")
        Label(frame, text=msg).pack(padx=4, pady=4, anchor=NW, fill=X)

        cert_frame = frame.cert_frame = Frame(frame)
        # location_
        Label(cert_frame, text="Certificate Location: ").pack(anchor=W)
        Entry(cert_frame,
              textvar=frame.cert_location
              ).pack(fill=X)
        Button(cert_frame,
               text="Find"
               ).pack(anchor=E)

        cert_frame.info_frame = Frame(frame)
        # cert_frame.info_frame.grid(row=1, columnspan=3, sticky='ew')
        cert_frame.info_frame.pack(fill=BOTH)

        cert_frame.pack(fill=BOTH, padx=6)

        self.update_certificate_info()

        Button(frame,
               text="Import",
               command=self.import_certificate
               ).pack(padx=6, pady=6, side=BOTTOM, anchor='se')
        # frame.pack(fill=BOTH, padx=3, pady=3)

    def import_certificate(self):
        from tkinter import (filedialog, messagebox)
        from os import path
        from OpenSSL import crypto

        frame = self.tab_frames['Authentication']

        startfile = frame.cert_location.get()
        initialdir = path.dirname(startfile)
        cerfile = filedialog.askopenfilename(initialdir=initialdir,
                                             defaultextension='.p12')
        if not cerfile:
            return

        password = StringVar()

        def on_password(pas):
            password_prompt.destroy()
            password = pas.get().encode()
            print("PASSWORD: ", password)

            try:
                p12 = crypto.load_pkcs12(open(cerfile, 'rb').read(), password)
            except crypto.Error as e:
                print(e)
                print(dir(e))
                print(e.args[0])
                # for x in dir(e):
                    # print(x, e.__getattribute__(x))
                messagebox.showerror("Bad Password",
                                     "Error reading file:\n %s" % e)
                return

            certificate = p12.get_certificate()
            pkey = p12.get_privatekey()

            owner = certificate.get_subject().get_components()[-1]
            print(owner)
            outdir = path.dirname(cerfile)
            msg = "Generate certificate and key for\n%s\n in \
                   directory\n%s?" % (owner[1].decode(), outdir)
            agree = messagebox.askyesno("Generate Files", msg)

            if not agree:
                return

            pemtype = crypto.FILETYPE_PEM

            with open(path.join(outdir, 'usacert.pem'), 'wb') as cert:
                cert.write(crypto.dump_certificate(pemtype, certificate))

            with open(path.join(outdir, 'usakey.pem'), 'wb') as key:
                key.write(crypto.dump_privatekey(pemtype, pkey))

        password_prompt = Toplevel(frame)
        p_frame = Frame(password_prompt)
        Label(p_frame, text='File Password').pack()
        Entry(p_frame, textvar=password, show="*").pack()
        Button(p_frame,
               text="UNLOCK",
               command=lambda: on_password(password)).pack(side=BOTTOM)
        Button(p_frame,
               text="cancel",
               command=lambda: password_prompt.destroy()).pack(side=BOTTOM)
        p_frame.pack(fill=BOTH, expand=1)


    def update_certificate_info(self):
        from os import path
        from OpenSSL import crypto
        from pprint import pprint
        from time import (strptime, strftime)

        aframe = self.tab_frames['Authentication']
        info_frame = Frame(aframe)

        pubname = path.join(aframe.cert_location.get())

        def next_rc():
            row, column = 0, 0
            while True:
                for column in range(0,2):
                    yield {
                        'row': row,
                        'column': column,
                        'sticky': ('e', 'w')[column]
                    }
                row += 1

        with open(pubname, 'r') as pub:
            cert = crypto.load_certificate(crypto.FILETYPE_PEM, pub.read())
            issuer = cert.get_issuer()
            print(cert)
            f = LabelFrame(info_frame, text='Certificate', relief='groove')

            an_rc = next_rc()

            def rc():
                return next(an_rc)

            for component in issuer.get_components():
                k, v = component
                print(k, v)
                Label(f, text=k.decode() + ':').grid(**rc())
                Label(f, text=v.decode()).grid(**rc())

            row=len(issuer.get_components())
            Label(f, text="SN:").grid(**rc())
            Label(f, text=cert.get_serial_number()).grid(**rc())

            try:
                algorithm = cert.get_signature_algorithm()
            except ValueError:
                algorithm = "N/A"

            Label(f, text="Algorithm:").grid(**rc())
            Label(f, text=algorithm).grid(**rc())

            Label(f, text="Expires:").grid(**rc())
            expires = cert.get_notAfter().decode()
            expires = strftime("%b %d, %Y", strptime(expires[:8], '%Y%m%d'))
            # expires = strftime(expires
            Label(f, text=expires).grid(**rc())
            f.pack(fill=X, padx=20)

            c = LabelFrame(info_frame, text='User', relief='groove')
            an_rc = next_rc()
            for k, v in cert.get_subject().get_components():
                Label(c, text=k.decode() + ':').grid(**rc())
                Label(c, text=v.decode()).grid(**rc())
            c.pack(fill=X, padx=20)

        info_frame.pack(fill=BOTH)



        # Label(aframe.cert_frame.info_frame, text="IT WORKS").pack()
