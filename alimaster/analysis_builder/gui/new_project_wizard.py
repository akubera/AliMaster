#
# alimaster/analysis_builder/gui/new_project_wizard.py
#
from tkinter import *       # noqa
from tkinter.ttk import *   # noqa
from PIL import ImageTk

import os

from alimaster.gui.style import use_alimaster_style
from alimaster.gui.fontawesome import FontAwesome


class NewProjectWizard(Notebook):
    """
    The gui window for creating a new analysis project.
    """
    title = 'AnalysisBuilder - New Project'

    def __init__(self, master=None, callback=None, **kw):
        """
        Construct a NewProjectWizard.
        @param master: A Toplevel for which to place the wizard
        @param **kw: Keywords for the Notebook
        """
        self.on_finish = callback
        self.master_frame = Frame(master)
        self.label = Label(self.master_frame,
                           text=self.title,
                           style='Title.Wizard.TLabel'
                           )
        self.label.pack(fill=X, pady=(12, 0), padx=24)

        photoimage = ImageTk.PhotoImage(FontAwesome.generate_icon('magic', 50))
        self.lbl = Label(self.master_frame, image=photoimage)
        self.lbl.photo = photoimage
        self.lbl.pack(side=LEFT, padx=(20, 10))

        self.args = {
            'name': StringVar(),
            'author': StringVar(),
            'location': StringVar()
        }
        self.args['name'].set("My New Project")
        self.args['author'].set(os.environ['USER'])
        self.args['location'].set(os.getcwd())

        kw['style'] = 'Wizard.TNotebook'

        # This line removes the tabs from the notebook
        Style(master).layout('Wizard.TNotebook.Tab', '')
        super().__init__(self.master_frame, **kw)

        self._children = [
            self.setup_page_0(self.add_empty_page()),
            self.setup_page_1(self.add_empty_page())
        ]

        # for page in range(1, 3):
        #     self.add_empty_page()

        # self.setup_page_0(self.page_container(0))

        self.current_tab_index = 0
        self.master_frame.pack(fill='both', expand=True)
        self.pack(fill='both', expand=True)

        button_frame = Frame(self.master_frame)
        self.prev_button = Button(button_frame,
                                  text="Previous",
                                  state=DISABLED,
                                  command=self.prev_page)
        self.prev_button.pack(side=LEFT)
        self.next_button = Button(button_frame,
                                  text="Next",
                                  command=self.next_page)
        self.next_button.pack(side=LEFT)
        button_frame.pack(anchor=SE, padx=3, pady=(1, 3))

    def setup_page_0(self, frame):
        from tkinter.filedialog import askdirectory

        self.page_0 = Frame(frame)

        entry_width = 45

        Label(self.page_0,
              text='Details',
              style='Heading.Wizard.TLabel').grid(column=0,
                                                  row=0,
                                                  columnspan=2)

        Label(self.page_0, text='Name: ', justify=RIGHT).grid(column=0, row=1)
        Entry(self.page_0,
              textvariable=self.args['name'],
              width=entry_width,
              takefocus=True).grid(column=1, row=1)

        Label(self.page_0, text='Author: ', anchor=E).grid(column=0, row=2)
        Entry(self.page_0,
              width=entry_width,
              textvariable=self.args['author']).grid(column=1, row=2)

        Label(self.page_0, text='Location: ', anchor=E).grid(column=0, row=3)
        Entry(self.page_0,
              width=entry_width,
              textvariable=self.args['location']).grid(column=1,
                                                       row=3,
                                                       pady=(0, 10))

        def set_file_name():
            filename = askdirectory()  # filetypes=('*'))
            if filename:
                self.args['location'].set(filename)

        Button(self.page_0,
               text="...",
               command=set_file_name).grid(column=2, row=3, padx=6, pady=(0,10))

        self.page_0.pack(padx=3, pady=3)

    def setup_page_1(self, frame):
        self.page_1 = Frame(frame)

        Label(self.page_1,
              text='Next!',
              style='Heading.Wizard.TLabel').grid(column=0,
                                                  row=0,
                                                  columnspan=2)

    def next_page(self):
        if self.current_tab_index + 1 == len(self._children):
            return
        self.current_tab_index += 1
        self.update_page()

    def prev_page(self):
        if self.current_tab_index == 0:
            return
        self.current_tab_index -= 1
        self.update_page()

    def update_page(self):
        self.select(self.current_tab_index)
        if len(self._children) == self.current_tab_index + 1:
            self.prev_button.state(['!disabled'])
            self.next_button.state(['disabled'])
        elif self.current_tab_index == 0:
            self.prev_button.state(['disabled'])
            self.next_button.state(['!disabled'])

    def close(self):
        self.master.destroy()

    def add_empty_page(self):
        child = Frame(self)
        # self._children[len(self._children)] = child
        self.add(child)
        return child

    def add_page_body(self, body):
        body.pack(side='top', fill='both', padx=6, pady=12)

    def page_container(self, page_num):
        if page_num in self._children:
            return self._children[page_num]
        else:
            raise KeyError("Invalid page: %s" % page_num)

    def _get_current(self):
        return self.current_tab_index

    def _set_current(self, curr):
        if self.current_tab_index == curr:
            return
        if curr not in self._children:
            raise KeyError("Invalid page: %s" % curr)
        self.current_tab_index = curr
        self.select(self._children[self.current_tab_index])

    current = property(_get_current, _set_current)


def demo():
    root = Tk()
    f = Frame(root)

    def open_wizard():
        top = Toplevel(root)
        NewProjectWizard(top)
        top.minsize(300, 200)

    use_alimaster_style()
    b = Button(f, text='open_window', command=open_wizard)
    b.pack()
    # f.pack()

    NewProjectWizard(root)

    root.mainloop()

if __name__ == "__main__":
    demo()
