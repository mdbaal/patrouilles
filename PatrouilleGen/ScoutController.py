import random
import time
from typing import Dict, List

from .Scout import Scout


class ScoutController:
    _scouts: Dict = {

    }

    _unassigned_scouts: List = []

    def new_scout(self, name, age, insigne, title="lid") -> Scout:
        scout: Scout = Scout(name, age, insigne)
        self._scouts[name] = scout
        scout.title = title
        self._unassigned_scouts.append(scout)
        self._unassigned_scouts.sort(key=self._insigne_filter)

        random.seed(time.time())
        if len(self._scouts) > 0:
            for s in self._scouts.values():
                s.set_relation(scout, random.randint(-1, 1))

    def _insigne_filter(self, scout: Scout):
        return scout.get_insigne()

    def delete_scout(self, scout_name: str):
        scout: Scout = self._scouts.get(scout_name.split(' ')[0])

        for s in self._scouts.values():
            s.remove_relation(scout)

        if self._unassigned_scouts.count(scout) > 0:
            self._unassigned_scouts.remove(scout)

        self._scouts.pop(scout.name)
        del scout

    # TODO redo after setting scout relations works
    def EditScout(self, scout, prop, **change):
        # check property to change, then activate function with parameters
        switcher = {
            "name": scout.change_name(change["name"]),
            "leeftijd": scout.change_age(change["leeftijd"]),
            "insigne": scout.set_insigne(change["insigne"], change["boolean"]),
            "relation": scout.set_relation(change["scout"], change["level"]),
            "removeRel": scout.remove_relation(change["scout"]),
        }

        action = switcher.get(prop, None)

        if action is not None:
            action()

    def get_scouts(self):
        return self._scouts

    def get_scout(self, scout_name: str):
        return self._scouts.get(scout_name.split(' ')[0])

    def get_unassigned_scouts(self):
        return self._unassigned_scouts

    def add_to_unassigned(self, scout: Scout):
        self._unassigned_scouts.append(scout)

    def remove_from_unassigned(self, scout: Scout):
        self._unassigned_scouts.remove(scout)
