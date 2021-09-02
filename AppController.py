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

    def __init__(self):
        self._app: App = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
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

        except IOError:
            raise IOError()

    def save_scouts_to_json(self, path='data/scouts.json'):
        pass

    def sort_by_title(self, scout):
        title = scout["title"]

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
            "new_scout": partial(self._app.new_scout_window, submit_command=self.create_scout),
            "delete_scout": self.delete_scout,
            "AssignScout": partial(self._app.assign_scout_window,submit_command=self.assign_scout),
            "SelectPatrouille": self.select_patrouille
        }

        switch.get(action)()

    def create_patrouille(self, data: Dict):
        self._patrouilleController.add_patrouille(data["Name"])
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
        self._app.unassigned_scouts.add_item(f"{data['Name']} - {str.upper(data['title'])}")
        self._scoutController.new_scout(data["Name"], data["Age"], data["Insigne"], data["title"])

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

    def select_patrouille(self):
        patrouille_naam = self._app.patrouilles_list.get_current_item_name()
        if patrouille_naam is None:
            return
        patrouille = self._patrouilleController.get_patrouille(patrouille_naam)
        self._app.select_patrouille(patrouille.leden)
