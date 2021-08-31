import json
import os.path
from typing import Dict
from UI.UIApp import App
from PatrouilleGen import *


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

    def Setup(self, scoutController: ScoutController, patrouilleController: PatrouilleController,
              patrouilleGenerator: PatrouilleGenerator, app: App):
        self._scoutController = scoutController
        self._patrouilleController = patrouilleController
        self._patrouilleGenerator = patrouilleGenerator
        self._app = app
        app.attach(self)

    def LoadScoutsFromJson(self, path='data/scouts.json'):
        if os.path.isfile(path) and os.path.getsize(path) > 0:
            with open(path) as scoutsJson:
                scoutData = json.load(scoutsJson)

            for s in scoutData["Scouts"]:
                self._scoutController.NewScout(s["Naam"], s["Leeftijd"], s["Insignelevel"], title=s["Title"])
        else:
            return

    def SaveScoutsToJson(self, path='data/scouts.json'):
        pass

