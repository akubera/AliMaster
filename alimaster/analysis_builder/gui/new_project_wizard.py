#
# alimaster/analysis_builder/gui/new_project_wizard.py
#

from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk

import os

from alimaster.gui.style import use_alimaster_style

class NewProjectWizard(Notebook):

    def __init__(self, master=None, **kw):
        """
        Construct a NewProjectWizard.
        @param master: A Toplevel for which to place the wizard
        @param **kw: Keywords for the Notebook
        """
        self.master_frame = Frame(master)
        self.label = Label(self.master_frame,
            text='New Project Wizard',
            style='Heading.TLabel'
            )
        self.label.pack(fill=X, pady=(12,0), padx=24)

        self.args = {
            'name': StringVar(),
            'author': StringVar(),
            'location': StringVar()
        }
        self.args['name'].set("My New Project")
        self.args['author'].set(os.environ['USER'])
        self.args['location'].set(os.getcwd())

        kw['style'] = 'Wizard.TNotebook'
        ttk.Style(master).layout('Wizard.TNotebook.Tab', '')
        super().__init__(self.master_frame, **kw)

        self._children = {}

        for page in range(3):
            self.add_empty_page()

        self.setup_page_0(self.page_container(0))

        self.current = 0
        self.master_frame.pack(fill='both', expand=True)
        self.pack(fill='both', expand=True)

    def setup_page_0(self, frame):
        self.page_0 = Frame(frame)

        Label(self.page_0, text='Name: ').grid(column=0, row=0)
        Entry(self.page_0,
              textvariable=self.args['name']
              ).grid(column=1, row=0)

        Label(self.page_0, text='Author: ').grid(column=0, row=1)
        Entry(self.page_0,
              textvariable=self.args['author']
              ).grid(column=1, row=1)

        Label(self.page_0, text='Location: ').grid(column=0, row=2)
        Entry(self.page_0,
              textvariable=self.args['location']
              ).grid(column=1, row=2)


        self.page_0.pack(padx=3,pady=3)

    def next_page(self):
        self.current += 1

    def prev_page(self):
        self.current -= 1

    def close(self):
        self.master.destroy()

    def add_empty_page(self):
        child = ttk.Frame(self)
        self._children[len(self._children)] = child
        self.add(child)

    def add_page_body(self, body):
        body.pack(side='top', fill='both', padx=6, pady=12)

    def page_container(self, page_num):
        if page_num in self._children:
            return self._children[page_num]
        else:
            raise KeyError("Invalid page: %s" % page_num)

    def _get_current(self):
        return self._current

    def _set_current(self, curr):
        if curr not in self._children:
            raise KeyError("Invalid page: %s" % curr)

        self._current = curr
        self.select(self._children[self._current])

    current = property(_get_current, _set_current)

def demo():
    root = Tk()
    f = Frame(root)

    def open_wizard():
        top = Toplevel(root)
        wizard = NewProjectWizard(top)
        top.minsize(300, 200)

    use_alimaster_style()
    b = Button(f,text='open_window', command=open_wizard)
    b.pack()
    f.pack()

    root.mainloop()

if __name__ == "__main__":
    demo()
