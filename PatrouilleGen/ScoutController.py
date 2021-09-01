import random
import time
from typing import Dict, List

from .Scout import Scout


class ScoutController:
    _scouts: Dict = {

    }

    _unassignedScouts: List = []

    def NewScout(self, naam, leeftijd, insigneLevel, title="lid") -> Scout:
        scout: Scout = Scout(naam, leeftijd, insigneLevel)
        self._scouts[naam] = scout
        scout.Title = title
        self._unassignedScouts.append(scout)
        self._unassignedScouts.sort(key=self.InsigneLevel)

        random.seed(time.time())
        if len(self._scouts) > 0:
            for s in self._scouts.values():
                s.SetRelation(scout, random.randint(-1, 1))

    def InsigneLevel(self, scout: Scout):
        return scout.GetInsigneLevel()

    def DeleteScout(self, scout_name: str):
        scout: Scout = self._scouts.get(scout_name.split(' ')[0])

        for s in self._scouts.values():
            s.RemoveRelation(scout)

        if self._unassignedScouts.count(scout) > 0:
            self._unassignedScouts.remove(scout)

        self._scouts.pop(scout.Naam)
        del scout

    def EditScout(self, scout, prop, **change):
        # check property to change, then activate function with parameters
        switcher = {
            "naam": scout.ChangeNaam(change["naam"]),
            "leeftijd": scout.ChangeLeeftijd(change["leeftijd"]),
            "insigne": scout.SetInsigne(change["insigne"], change["boolean"]),
            "relation": scout.SetRelation(change["scout"], change["level"]),
            "removeRel": scout.RemoveRelation(change["scout"]),
        }

        action = switcher.get(prop, None)

        if action is not None:
            action()

    def GetScouts(self):
        return self._scouts

    def GetScout(self, scout_name: str):
        return self._scouts.get(scout_name.split(' ')[0])

    def GetUnassignedScouts(self):
        return self._unassignedScouts

    def add_to_unassigned(self, scout: Scout):
        self._unassignedScouts.append(scout)

    def RemoveFromUnassigned(self, scout: Scout):
        self._unassignedScouts.remove(scout)
