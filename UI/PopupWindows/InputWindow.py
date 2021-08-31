from tkinter import *
from .PopupWindow import PopupWindow


class InputWindow(PopupWindow):
    def __init__(self, master, title, bg="lightgrey", submit_command=None):
        super().__init__(master, bg=bg, title=title, submit_command=submit_command)
        self.geometry("250x100")

        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.entry: Entry = Entry(self)
        self.entry.grid(row=0, columnspan=2, sticky="EW", padx=20, pady=10)
        self.entry.focus()
        self.button = Button(self, text="Submit", command=self.submit)
        self.button.grid(row=1, columnspan=2, sticky="EW", padx=20, pady=10)

    def submit(self):
        self._input["Name"] = self.entry.get()
        super().submit()



