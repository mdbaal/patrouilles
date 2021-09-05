from typing import Dict, List

from .Scout import Scout


class ScoutController:
    _scouts: Dict = {

    }

    _unassigned_scouts: List = []

    # TODO set input argument to data: Dict
    def new_scout(self, data: Dict) -> Scout:
        scout: Scout = Scout(data)
        self._scouts[data["Name"]] = scout
        self._unassigned_scouts.append(scout)
        self._unassigned_scouts.sort(key=self._insigne_filter)
        return scout

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

    def edit_scout(self, data: Dict):
        scout: Scout = data["Scout"]

        scout.change_name(data["Name"])
        scout.change_age(data["Age"])
        scout.set_insigne(data["Insigne"])
        scout.title = data["Title"]

        for relation, level in data["Relations"].items():
            scout.set_relation(relation, level)
            other_scout: Scout = self.get_scout(relation)
            other_scout.set_relation(scout.name, level)

    def get_scouts(self):
        return self._scouts.values()

    def get_scouts_dict(self):
        return self._scouts

    def get_scout(self, scout_name: str):
        name = self.clean_name(scout_name)
        return self._scouts.get(name)

    def get_unassigned_scouts(self):
        return self._unassigned_scouts

    def add_to_unassigned(self, scout: Scout):
        self._unassigned_scouts.append(scout)

    def remove_from_unassigned(self, scout: Scout):
        self._unassigned_scouts.remove(scout)

    def set_relations(self):
        scout: Scout
        other_scout: Scout

        for scout in self._scouts.values():
            for other_scout in self._scouts.values():
                if other_scout is not scout:
                    if scout.has_relation(other_scout.name) is False:
                        scout.set_relation(other_scout.name, 0)

    def clean_name(self, scout_name: str):
        if " - PL" in scout_name:
            return scout_name.replace(" - PL", "")
        if " - APL" in scout_name:
            return scout_name.replace(" - APL", "")
        if " - LID" in scout_name:
            return scout_name.replace(" - LID", "")

        return scout_name
