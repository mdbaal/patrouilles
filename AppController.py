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

        self.load_scouts_from_json()

    def load_scouts_from_json(self, path='data/scouts.json'):
        try:
            with open(path) as scoutsJson:
                scoutData: Dict = json.load(scoutsJson)

            sortedData = sorted(scoutData["Scouts"], key=self.sort_by_title)

            for scout in sortedData:
                self.create_scout(scout)

            self._scoutController.set_relations()

        except IOError:
            raise IOError()

    def save_scouts_to_json(self, path='data/scouts.json'):
        pass

    def sort_by_title(self, scout):
        title = scout["Title"]

        if title == "pl":
            return 0
        elif title== "apl":
            return 1
        else:
            return 2

    def update(self, action: str):
        switch = {
            "NewPatrouille": partial(self._app.new_patrouille_window, submit_command=self.create_patrouille),
            "DeletePatrouille": self.delete_patrouille,
            "RenamePatrouille": partial(self._app.rename_patrouille_window, submit_command=self.rename_patrouille),
            "new_scout": partial(self._app.new_scout_window, submit_command=self.create_scout),
            "edit_scout": self.edit_scout_window_setup,
            "delete_scout": self.delete_scout,
            "AssignScout": partial(self._app.assign_scout_window, submit_command=self.assign_scout),
            "UnAssignScout": self.unassign_scout,
            "SelectPatrouille": self.select_patrouille
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

    # TODO add arg to check if scout is created unassigned or directly into patrouille
    def create_scout(self, data: Dict):
        self._app.unassigned_scouts.add_item(f"{data['Name']} - {str.upper(data['Title'])}")
        self._scoutController.new_scout(data["Name"], data["Age"], data["Insigne"], title=data["Title"], relations=data["Relations"])

    def edit_scout(self, data: Dict):
        self._scoutController.edit_scout(data)

    def edit_scout_window_setup(self):
        scout: Scout = self._scoutController.get_scout(self._app.unassigned_scouts.get_current_item_name())
        if scout is None:
            return
        all_scouts = list(self._scoutController.get_scouts())
        self._app.edit_scout_window(scout, all_scouts, submit_command=self.edit_scout)

    # TODO add arg to check if scout is in unassigned in patrouille
    def delete_scout(self):
        scout_name: str = self._app.unassigned_scouts.get_current_item()
        self._app.unassigned_scouts.remove_item()
        self._scoutController.delete_scout(scout_name)

    def assign_scout(self, data: Dict):
        scout_name = self._app.unassigned_scouts.get_current_item_name()
        self._app.unassigned_scouts.remove_item()
        scout: Scout = self._scoutController.get_scout(scout_name)
        self._patrouilleController.add_scout_to_patrouille(data["option"], scout)

    # TODO use return of remove_item to get scout_name
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

    def select_patrouille(self):
        patrouille_naam = self._app.patrouilles_list.get_current_item_name()
        if patrouille_naam is None:
            return
        patrouille = self._patrouilleController.get_patrouille(patrouille_naam)
        self._app.select_patrouille(patrouille.leden)
