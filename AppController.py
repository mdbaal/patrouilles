import json
import tkinter.constants
from functools import partial
from typing import Dict

from PatrouilleGen import *
from UI.UIApp import App


class AppController(object):
    # instance of it self
    _instance = None

    # All app instances
    _scoutController: ScoutController = None
    _patrouilleController: PatrouilleController = None
    _patrouilleGenerator: PatrouilleGenerator = None
    _app: App = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppController, cls).__new__(cls)

        return cls._instance

    def setup(self, scoutController: ScoutController, patrouilleController: PatrouilleController,
              patrouilleGenerator: PatrouilleGenerator, app: App):
        self._scoutController = scoutController
        self._patrouilleController = patrouilleController
        self._patrouilleGenerator = patrouilleGenerator
        self._app = app
        app.attach(self)
        app.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.load_scouts_from_json()
        self.setup_scouts()

    def load_scouts_from_json(self, path='data/scouts.json'):
        try:
            with open(path) as scoutsJson:
                scoutData: Dict = json.load(scoutsJson)

            sortedData = sorted(scoutData["Scouts"], key=self.sort_by_title)

            for scout in sortedData:
                self.create_scout(scout)

        except IOError:
            raise IOError()

    def save_scouts_to_json(self, path='data/scouts.json'):
        all_scouts: Dict = self._scoutController.get_scouts_dict()
        scouts_json: str = '{"Scouts" : ['
        for scout in all_scouts.values():
            scouts_json += json.dumps(scout, default=Scout.to_dict, indent=4)
            scouts_json += ','

        scouts_json = scouts_json[:-1]

        scouts_json += ']}'

        with open(path, "w") as scoutsJson:
            scoutsJson.write(scouts_json)

    def setup_scouts(self):
        for scout in self._scoutController.get_scouts():

            if scout.patrouille is not None:
                self.assign_scout({"Name": scout.name, "Option": scout.patrouille})

        self._scoutController.set_relations()

    def on_exit(self):
        self.save_scouts_to_json()
        self._app.quit()

    def sort_by_title(self, scout):
        title = scout["Title"]

        if title == "pl":
            return 0
        elif title == "apl":
            return 1
        else:
            return 2

    def update(self, action: str):
        switch = {
            "NewPatrouille": partial(self._app.new_patrouille_window, submit_command=self.create_patrouille),
            "DeletePatrouille": self.delete_patrouille,
            "RenamePatrouille": partial(self._app.rename_patrouille_window, submit_command=self.rename_patrouille),
            "NewScout": partial(self._app.new_scout_window, submit_command=self.create_scout),
            "EditScout": self.edit_scout_window_setup,
            "DeleteScout": self.delete_scout,
            "AssignScout": partial(self._app.assign_scout_window, submit_command=self.assign_scout),
            "TransferScout": partial(self._app.assign_scout_window, submit_command=self.transfer_scout),
            "UnAssignScout": self.unassign_scout,
            "SelectPatrouille": self.select_patrouille,
            "GeneratePatrouilles": partial(self._app.generate_patrouille_window, submit_command=self.generate_patrouilles)
        }

        switch.get(action, None)()

    def create_patrouille(self, data: Dict):
        self._patrouilleController.add_patrouille(data["Name"])
        self._app.patrouilles_list.add_item(data["Name"])

    def rename_patrouille(self, data: Dict):
        old_patrouille = self._app.patrouilles_list.get_current_item_name()
        self._patrouilleController.rename_patrouille(old_patrouille, data["Name"])
        self._app.patrouilles_list.remove_item()
        self._app.patrouilles_list.add_item(data["Name"])

    def delete_patrouille(self):
        # Get patrouille after it is destroyed
        patleden = self._patrouilleController.remove_patrouille(self._app.patrouilles_list.get_current_item_name())
        self._app.patrouilles_list.remove_item()
        # If patrouille had scouts then add them back to unassigned
        for scout in patleden:
            self._scoutController.add_to_unassigned(scout)
            self._app.unassigned_scouts.add_item(f"{scout.name} - {str.upper(scout.title)}")
            self._app.patrouille_scouts.delete(0, tkinter.constants.END)

    def create_scout(self, data: Dict):
        scout = self._scoutController.new_scout(data)
        self._app.unassigned_scouts.add_item(f"{scout.name} - {str.upper(scout.title)}")

    def edit_scout(self, data: Dict):
        self._scoutController.edit_scout(data)

    def edit_scout_window_setup(self):
        scout: Scout = self._scoutController.get_scout(self._app.unassigned_scouts.get_current_item_name())
        if scout is None:
            return
        all_scouts = list(self._scoutController.get_scouts())
        self._app.edit_scout_window(scout, all_scouts, submit_command=self.edit_scout)

    # TODO add arg to check if scout is in unassigned in patrouille
    # TODO on delete scout clear all other relations
    def delete_scout(self):
        scout_name: str = self._app.unassigned_scouts.get_current_item()
        self._app.unassigned_scouts.remove_item()
        self._scoutController.delete_scout(scout_name)

    def assign_scout(self, data: Dict):
        if "Name" in data:
            scout_name = data["Name"]
        else:
            scout_name = self._app.unassigned_scouts.get_current_item_name()

        self._app.unassigned_scouts.remove_item_by_name(scout_name)
        scout: Scout = self._scoutController.get_scout(scout_name)

        if self._patrouilleController.get_patrouille(data["Option"]) is None:
            self.create_patrouille({"Name": data["Option"]})
        self._patrouilleController.add_scout_to_patrouille(data["Option"], scout)
        scout.set_patrouille(data["Option"])

    def transfer_scout(self, data: Dict):
        scout_name = self._app.patrouille_scouts.get_current_item_name()
        scout: Scout = self._scoutController.get_scout(scout_name)
        old_patrouille = self._app.patrouilles_list.get_current_item_name()

        self._patrouilleController.transfer_scout_to_patrouille(old_patrouille, data["Option"], scout)
        self._app.patrouille_scouts.remove_item_by_name(scout_name)

    def unassign_scout(self):
        # Get scout name and patrouille name
        scout_name = self._app.patrouille_scouts.get_current_item_name()
        patrouille_name = self._app.patrouilles_list.get_current_item_name()

        # Get scout, remove it from patrouille and text list
        scout: Scout = self._scoutController.get_scout(scout_name)
        self._patrouilleController.remove_scout_from_patrouille(patrouille_name, scout)
        self._app.patrouille_scouts.remove_item()

        # Add scout to unassigned list and text list
        self._scoutController.add_to_unassigned(scout)
        self._app.unassigned_scouts.add_item(f"{scout.name} - {scout.title}")

        scout.set_patrouille(None)

    def select_patrouille(self):
        patrouille_naam = self._app.patrouilles_list.get_current_item_name()
        if patrouille_naam is None:
            return
        patrouille = self._patrouilleController.get_patrouille(patrouille_naam)
        self._app.select_patrouille(patrouille.leden)
        self._app.patrouille_scouts.update_title(f"Patrouille leden: {patrouille_naam}")

    def generate_patrouilles(self, data: Dict):
        # Add check for existing patrouilles, if so open window to ask for keep current or overwrite current

        self._patrouilleGenerator.generate_patrouilles(self._patrouilleController, self._scoutController, data["Patrouilles"])

        # Update patrouille and unassigned list
        patrouille: Patrouille
        for patrouille in self._patrouilleController.get_patrouilles():
            self._app.patrouilles_list.add_item(patrouille.name)
            for scout in patrouille.leden:
                self._app.unassigned_scouts.remove_item_by_name(scout.name)

