from tkinter import *
from tkinter.ttk import Combobox

from .PopupWindow import PopupWindow


class DropdownInputWindow(PopupWindow):
    def __init__(self, master, title, options, bg="lightgrey", submit_command=None):
        super().__init__(master, bg=bg, title=title, submit_command=submit_command)
        self.geometry("250x100")

        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.entryPatrouille: Combobox = Combobox(self)
        self.entryPatrouille['values'] = options
        self.entryPatrouille.grid(row=0, columnspan=2, sticky="EW", padx=20, pady=10)
        self.entryPatrouille.focus()

        self.button = Button(self, text="Submit", command=self.submit)
        self.button.grid(row=1, columnspan=2, sticky="EW", padx=20, pady=10)

    def submit(self):
        self._input["option"] = self.entryPatrouille.get()
        super().submit()



