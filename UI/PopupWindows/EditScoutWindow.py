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
        self.labelName: Label = Label(self, text="Naam")
        self.labelName.grid(row=0, column=0, sticky="EW", padx=20, pady=10)

        self.entryName: Entry = Entry(self, textvariable=self._input["Naam"])
        self.entryName.insert(END, scout.Naam)
        self.entryName.grid(row=1, column=0, sticky="EW", padx=20, pady=5)
        self.entryName.focus()

        # Edit Leeftijd
        self.labelAge: Label = Label(self, text="Leeftijd")
        self.labelAge.grid(row=0, column=1, sticky="EW", padx=20, pady=10)

        self.entryAge: Spinbox = Spinbox(self, from_=11, to=16, textvariable=self._input["Age"])
        self.entryAge.insert(END, scout.Leeftijd)
        self.entryAge.grid(row=1, column=1, sticky="EW", padx=20, pady=5)

        # Edit Insigne
        self.labelInsigne: Label = Label(self, text="Insigne")
        self.labelInsigne.grid(row=2, column=0, sticky="EW", padx=20, pady=5)

        self.entryInsigne: Spinbox = Spinbox(self, from_=0, to=5, textvariable=self._input["Insigne"])
        self.entryInsigne.insert(END, scout.GetInsigneLevel())
        self.entryInsigne.grid(row=3, column=0, sticky="EW", padx=20, pady=5)

        # Edit Relations
        self.labelRelations: Label = Label(self, text="Relaties")
        self.labelRelations.grid(row=2, column=1, sticky="EW", padx=20, pady=5)

        # TODO Test relations with menu buttons
        self.entryRelation: Combobox = Combobox(self, textvariable=self._input["Relations"])
        self.entryRelation.grid(row=3, column=1, sticky="EW", padx=20, pady=5)

        # Edit Title
        self.labelTitle: Label = Label(self, text="Title")
        self.labelTitle.grid(row=4, column=0, sticky="EW", padx=20, pady=5)

        self.entryTitle: Combobox = Combobox(self, textvariable=self._input["Title"])
        self.entryTitle['values'] = ('Lid', 'Pl', 'Apl')
        self.entryTitle.set(scout.Title)
        self.entryTitle['state'] = 'readonly'
        self.entryTitle.grid(row=5, column=0, sticky="EW", padx=20, pady=5)

        # Confirm
        self.button = Button(self, text="Submit", command=self.submit)
        self.button.grid(row=6, columnspan=2, sticky="EW", padx=20, pady=10)

