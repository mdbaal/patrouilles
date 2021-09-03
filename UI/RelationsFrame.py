from tkinter import *
from tkinter.ttk import Combobox
from typing import List

from PatrouilleGen import Scout


class RelationsFrame(Frame):
    def __init__(self, master, scout, all_scouts: List):
        super().__init__(master)

        self._scout: Scout = scout
        self._all_scouts = all_scouts
        self._all_scouts.remove(scout)

        self.level_var: IntVar = IntVar(master)
        self.levels_dict = dict(scout.get_relations())

        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.rowconfigure(self, 0, weight=1)

        # Combobox to select scout with
        self.selected_scout: Combobox = Combobox(self)

        leden_names: List = []
        for other_scout in all_scouts:
            leden_names.append(other_scout.name)

        self.selected_scout['values'] = leden_names
        self.selected_scout.set(leden_names[0])
        self.selected_scout['state'] = 'readonly'
        self.selected_scout.grid(row=0, column=0, sticky="EW", padx=20, pady=5)
        self.set_selected(None)

        # Spinbox to set relation level with
        self.relation_level: Spinbox = Spinbox(self, from_=-1, to=1, textvariable=self.level_var, command=self.change_level)
        self.relation_level.grid(row=0, column=1, sticky="EW", padx=20, pady=5)

        self.selected_scout.bind("<<ComboboxSelected>>", self.set_selected)

    def set_selected(self, e):
        self.level_var.set(self.levels_dict[self._all_scouts[self.selected_scout.current()].name])

    def change_level(self):
        self.levels_dict[self._all_scouts[self.selected_scout.current()].name] = self.level_var.get()

    def get(self):
        return self.levels_dict

    def get_scout(self):
        return self._scout
