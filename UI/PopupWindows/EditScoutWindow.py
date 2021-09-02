from tkinter import *
from tkinter.ttk import Combobox

from PatrouilleGen import Scout
from .PopupWindow import PopupWindow


class EditScoutWindow(PopupWindow):
    def __init__(self, scout: Scout, title=None, master=None, bg="lightgrey", submit_command=None):
        super().__init__(master, bg=bg, title=title, submit_command=submit_command)
        self.geometry("400x250")

        Grid.columnconfigure(self, 0, weight=1
                             )
        Grid.columnconfigure(self, 1, weight=1)

        # Edit Name
        self.label_name: Label = Label(self, text="name")
        self.label_name.grid(row=0, column=0, sticky="EW", padx=20, pady=10)

        self.entry_name: Entry = Entry(self, textvariable=self._input["name"])
        self.entry_name.insert(END, scout.name)
        self.entry_name.grid(row=1, column=0, sticky="EW", padx=20, pady=5)
        self.entry_name.focus()

        # Edit age
        self.label_age: Label = Label(self, text="age")
        self.label_age.grid(row=0, column=1, sticky="EW", padx=20, pady=10)

        self.entry_age: Spinbox = Spinbox(self, from_=11, to=16, textvariable=self._input["Age"])
        self.entry_age.insert(END, scout.age)
        self.entry_age.grid(row=1, column=1, sticky="EW", padx=20, pady=5)

        # Edit Insigne
        self.label_insigne: Label = Label(self, text="Insigne")
        self.label_insigne.grid(row=2, column=0, sticky="EW", padx=20, pady=5)

        self.entry_insigne: Spinbox = Spinbox(self, from_=0, to=5, textvariable=self._input["Insigne"])
        self.entry_insigne.insert(END, scout.get_insigne())
        self.entry_insigne.grid(row=3, column=0, sticky="EW", padx=20, pady=5)

        # Edit Relations
        self.label_relations: Label = Label(self, text="Relaties")
        self.label_relations.grid(row=2, column=1, sticky="EW", padx=20, pady=5)

        # TODO Test relations with menu buttons
        self.entry_relation: Combobox = Combobox(self, textvariable=self._input["Relations"])
        self.entry_relation.grid(row=3, column=1, sticky="EW", padx=20, pady=5)

        # Edit title
        self.label_title: Label = Label(self, text="title")
        self.label_title.grid(row=4, column=0, sticky="EW", padx=20, pady=5)

        self.entry_title: Combobox = Combobox(self, textvariable=self._input["title"])
        self.entry_title['values'] = ('Lid', 'Pl', 'Apl')
        self.entry_title.set(scout.title)
        self.entry_title['state'] = 'readonly'
        self.entry_title.grid(row=5, column=0, sticky="EW", padx=20, pady=5)

        # Confirm
        self.button = Button(self, text="Submit", command=self.submit)
        self.button.grid(row=6, columnspan=2, sticky="EW", padx=20, pady=10)

