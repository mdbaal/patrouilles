from functools import partial
from tkinter import *

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
        self.patrouillesList = UIListFrame(master=self, title="Patrouilles")
        self.patrouilleScouts = UIListFrame(master=self, title="Patrouille Leden")
        self.unAssignedScouts = UIListFrame(master=self, title="Geen Patrouille")

        self.patrouillesList.grid(row=1, column=0, sticky="NSEW", padx=10)

        self.patrouilleScouts.grid(row=1, column=1, sticky="NSEW", padx=10)

        self.unAssignedScouts.grid(row=1, column=2, sticky="NSEW", padx=10)

        ## Row 2 column 0 Patrouille control Buttons
        self.patrouillecontrol_frame = Frame(self)
        self.patrouillecontrol_frame.grid(row=2, column=0, padx=5, pady=5)

        ## Row 2 column 1 Patrouille Leden control Buttons
        self.patrouilleleden_frame = Frame(self)
        self.patrouilleleden_frame.grid(row=2, column=1, padx=5, pady=5)

        ## Row 2 column 2 Unassigned control Buttons
        self.unassigned_scouts_frame = Frame(self)
        self.unassigned_scouts_frame.grid(row=2, column=2, padx=5, pady=5)

        # Patrouille control buttons
        self.new_patrouille_btn = Button(self.patrouillecontrol_frame, text="New Patrouille", command=partial(self.notify, "NewPatrouille"))
        self.delete_patrouille_btn = Button(self.patrouillecontrol_frame, text="Delete Patrouille", command=partial(self.notify, "DeletePatrouille"))
        self.edit_patrouille_btn = Button(self.patrouillecontrol_frame, text="Edit Patrouille")

        self.new_patrouille_btn.grid(row=0, column=0, padx=2, pady=2)
        self.delete_patrouille_btn.grid(row=0, column=1, padx=2, pady=2)
        self.edit_patrouille_btn.grid(row=0, column=2, padx=2, pady=2)

        # Scout control in patrouille
        self.add_scout_btn = Button(self.patrouilleleden_frame, text="New Scout")
        self.delete_scout_patrouille_btn = Button(self.patrouilleleden_frame, text="Delete Scout")
        self.edit_scout_patrouille_btn = Button(self.patrouilleleden_frame, text="Edit Scout")

        self.add_scout_btn.grid(row=0, column=0, padx=2, pady=2)
        self.delete_scout_patrouille_btn.grid(row=0, column=1, padx=2, pady=2)
        self.edit_scout_patrouille_btn.grid(row=0, column=2, padx=2, pady=2)

        # Unassigned scouts control
        self.new_scout_btn = Button(self.unassigned_scouts_frame, text="New Scout",command=partial(self.notify, "NewScout"))
        self.delete_scout_btn = Button(self.unassigned_scouts_frame, text="Delete Scout",command=partial(self.notify, "DeleteScout"))
        self.assign_scout_btn = Button(self.unassigned_scouts_frame, text="Assign Scout")
        self.edit_scout_btn = Button(self.unassigned_scouts_frame, text="Edit Scout")

        self.new_scout_btn.grid(row=0, column=0, padx=2, pady=2)
        self.delete_scout_btn.grid(row=0, column=1, padx=2, pady=2)
        self.assign_scout_btn.grid(row=0, column=2, padx=2, pady=2)
        self.edit_scout_btn.grid(row=0, column=4, padx=2, pady=2)

    def attach(self,observer:object):
        self.observer = observer

    def notify(self,action:str):
        if self.observer is not None:
            self.observer.update(action)

    def new_patrouille_window(self, submit_command=None):
        InputWindow(self, "New Patrouille", submit_command=submit_command)

    def new_scout_window(self,submit_command=None):
        NewScoutWindow(self, "New Scout", submit_command=submit_command)
