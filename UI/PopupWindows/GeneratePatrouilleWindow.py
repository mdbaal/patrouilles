from tkinter import *

from UI.UIListFrame import UIListFrame
from .PopupWindow import PopupWindow


class GeneratePatrouilleWindow(PopupWindow):
    def __init__(self, master, title, bg="lightgrey", submit_command=None):
        super().__init__(master, bg=bg, title=title, submit_command=submit_command)
        self.geometry("250x400")

        Grid.rowconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=0)
        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.entry_patrouille = Entry(self)
        self.entry_patrouille.grid(row=0, sticky="EW", padx=10, pady=5)
        self.list_patrouilles = UIListFrame(master=self)
        self.list_patrouilles.grid(row=1, sticky="EW", padx=10, pady=5)
        self.entry_patrouille.bind('<Return>', self.add_to_list)
        self.list_patrouilles.listItems.bind('<Delete>', self.remove_from_list)

        self.button = Button(self, text="Submit", command=self.submit)
        self.button.grid(row=2, columnspan=2, sticky="EW", padx=10, pady=5)

    def submit(self):
        self._input["Patrouilles"] = self.list_patrouilles.get_all_items()
        super().submit()

    def add_to_list(self, e):
        self.list_patrouilles.add_item(self.entry_patrouille.get())
        self.entry_patrouille.delete(0, END)

    def remove_from_list(self, e):
        self.list_patrouilles.remove_item()




