from functools import partial
from tkinter import *
from typing import List

from .PopupWindows.DropdownInputWindow import DropdownInputWindow
from .PopupWindows.EditScoutWindow import EditScoutWindow
from .PopupWindows.GeneratePatrouilleWindow import GeneratePatrouilleWindow
from .PopupWindows.InputWindow import InputWindow
from .PopupWindows.NewScoutWindow import NewScoutWindow
from .UIListFrame import UIListFrame


class App(Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Patrouille Generator")
        self.maxsize()
        self.observer: object = None
        # Configure grid
        Grid.rowconfigure(self, 1, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 2, weight=1)

        # Create all frames
        self.patrouilles_list = UIListFrame(master=self, title="Patrouilles", select_command=partial(self.notify, "SelectPatrouille"))
        self.patrouille_scouts = UIListFrame(master=self, title="Patrouille leden")
        self.unassigned_scouts = UIListFrame(master=self, title="Geen Patrouille")

        self.patrouilles_list.grid(row=1, column=0, sticky="NSEW", padx=10)

        self.patrouille_scouts.grid(row=1, column=1, sticky="NSEW", padx=10)

        self.unassigned_scouts.grid(row=1, column=2, sticky="NSEW", padx=10)

        ## Row 2 column 0 Patrouille control Buttons
        self.patrouillecontrol_frame = Frame(self)
        self.patrouillecontrol_frame.grid(row=2, column=0, padx=5, pady=5)

        ## Row 2 column 1 Patrouille leden control Buttons
        self.patrouilleleden_frame = Frame(self)
        self.patrouilleleden_frame.grid(row=2, column=1, padx=5, pady=5)

        ## Row 2 column 2 Unassigned control Buttons
        self.unassigned_scouts_frame = Frame(self)
        self.unassigned_scouts_frame.grid(row=2, column=2, padx=5, pady=5)

        # Patrouille control buttons
        self.new_patrouille_btn = Button(self.patrouillecontrol_frame, text="New Patrouille", command=partial(self.notify, "NewPatrouille"))
        self.delete_patrouille_btn = Button(self.patrouillecontrol_frame, text="Delete Patrouille", command=partial(self.notify, "DeletePatrouille"))
        self.rename_patrouille_btn = Button(self.patrouillecontrol_frame, text="Rename Patrouille", command=partial(self.notify, "RenamePatrouille"))

        self.new_patrouille_btn.grid(row=0, column=0, padx=2, pady=2)
        self.delete_patrouille_btn.grid(row=0, column=1, padx=2, pady=2)
        self.rename_patrouille_btn.grid(row=0, column=2, padx=2, pady=2)

        # Scout control in patrouille
        self.add_scout_btn = Button(self.patrouilleleden_frame, text="New Scout", command=partial(self.notify, "NewScout"))
        self.delete_scout_patrouille_btn = Button(self.patrouilleleden_frame, text="Remove Scout", command=partial(self.notify, "UnAssignScout"))
        self.edit_scout_patrouille_btn = Button(self.patrouilleleden_frame, text="Transfer Scout", command=partial(self.notify, "TransferScout"))

        self.add_scout_btn.grid(row=0, column=0, padx=2, pady=2)
        self.delete_scout_patrouille_btn.grid(row=0, column=1, padx=2, pady=2)
        self.edit_scout_patrouille_btn.grid(row=0, column=2, padx=2, pady=2)

        # Unassigned scouts control
        self.new_scout_btn = Button(self.unassigned_scouts_frame, text="New Scout", command=partial(self.notify, "NewScout"))
        self.delete_scout_btn = Button(self.unassigned_scouts_frame, text="Delete Scout", command=partial(self.notify, "DeleteScout"))
        self.assign_scout_btn = Button(self.unassigned_scouts_frame, text="Assign Scout", command=partial(self.notify, "AssignScout"))
        self.edit_scout_btn = Button(self.unassigned_scouts_frame, text="Edit Scout", command=partial(self.notify, "EditScout"))

        self.new_scout_btn.grid(row=0, column=0, padx=2, pady=2)
        self.delete_scout_btn.grid(row=0, column=1, padx=2, pady=2)
        self.assign_scout_btn.grid(row=0, column=2, padx=2, pady=2)
        self.edit_scout_btn.grid(row=0, column=4, padx=2, pady=2)

        # Row 3 Generator button
        self.generate_patrouilles_btn = Button(self, text="Generate Patrouilles", command=partial(self.notify, "GeneratePatrouilles"))
        self.generate_patrouilles_btn.grid(row=3, column=0, columnspan=4, padx=2, pady=2)

    # attach observer object
    def attach(self, observer: object):
        self.observer = observer

    # notify the observer object
    def notify(self, action: str):
        if self.observer is not None:
            self.observer.update(action)

    def new_patrouille_window(self, submit_command=None):
        InputWindow(self, "New Patrouille", submit_command=submit_command)

    def rename_patrouille_window(self, submit_command=None):
        InputWindow(self, "Rename Patrouille", submit_command=submit_command)

    def new_scout_window(self, submit_command=None):
        NewScoutWindow(self, "New Scout", submit_command=submit_command)

    def edit_scout_window(self, scout, patrouille: List, submit_command=None):
        EditScoutWindow(master=self, scout=scout, patrouille=patrouille, title="Edit Scout", submit_command=submit_command)

    def assign_scout_window(self, submit_command=None):
        DropdownInputWindow(self, "Assign scout to patrouille", self.patrouilles_list.get_all_items(), submit_command=submit_command)

    def select_patrouille(self, patrouille_leden: List):
        self.patrouille_scouts.delete(0, END)

        if len(patrouille_leden) == 0:
            return

        for scout in patrouille_leden:
            self.patrouille_scouts.add_item(f"{scout.name} - {str.upper(scout.title)}")

    def generate_patrouille_window(self, submit_command=None):
        GeneratePatrouilleWindow(self, title="Generate Patrouille", submit_command=submit_command)
