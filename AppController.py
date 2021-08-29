import json
import os.path

from PatrouilleGen import *


class AppController(object):
    # instance it self
    _instance = None

    # All app instances
    _scoutController: ScoutController = None
    _patrouilleController: PatrouilleController = None
    _patrouilleGenerator: PatrouilleGenerator = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(AppController, cls).__new__(cls)

        return cls._instance

    def Setup(self, scoutController: ScoutController, patrouilleController: PatrouilleController, patrouilleGenerator: PatrouilleGenerator):
        self._scoutController = scoutController
        self._patrouilleController = patrouilleController
        self._patrouilleGenerator = patrouilleGenerator

    def GetData(self, data: str):
        dataSwitch = {
            "Scouts": self._scoutController.GetScouts,
            "UnassignedScouts": self._scoutController.GetUnassignedScouts,
            "InsigneLevel": self._scoutController.InsigneLevel,
            "GetPatrouille": self._patrouilleController.GetPatrouille,
            "GetPatrouilles": self._patrouilleController.GetPatrouilles
        }

        return dataSwitch.get(data)

    def GetFunction(self, function: str):
        funcSwitch = {
            "NewScout": self._scoutController.NewScout,
            "DeleteScout": self._scoutController.DeleteScout,
            "RemoveUnassigned": self._scoutController.RemoveFromUnassigned,
            "EditScout": self._scoutController.EditScout,
            "AddPatrouille": self._patrouilleController.AddPatrouille,
            "RemovePatrouille": self._patrouilleController.RemovePatrouille,
            "ChangeNamePatrouille": self._patrouilleController.ChangeNamePatrouille,
            "AddScoutToPatrouille": self._patrouilleController.AddScoutToPatrouille,
            "RemoveScoutFromPatrouille": self._patrouilleController.RemovePatrouille,
            "TransferScoutToPatrouille": self._patrouilleController.TransferScoutToPatrouille,
            "GeneratePatrouilles": self._patrouilleGenerator.GeneratePatrouilles3,
            "PrintPatrouilles": self._patrouilleController.printPatrouilles
        }

        return funcSwitch.get(function)

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