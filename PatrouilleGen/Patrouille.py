from typing import Dict

from .Scout import Scout


class Patrouille:
    def __init__(self, patrouille_name):
        self._patrouille_name = patrouille_name
        self._patrouille_leden: Dict[str, Scout] = {

        }
        self._patrouille_count = 0

        self._insigne_avg = 0

        self._pl = None
        self._apl = None

    def __copy__(self):
        copy = Patrouille(self.name)
        for scout in self._patrouille_leden.values():
            copy.add_scout(scout)

        copy._pl = self._pl
        copy._apl = self._apl
        copy._insigne_avg = self._insigne_avg
        copy._patrouille_count = self._patrouille_count
        return copy

    def add_scout(self, scout):
        if scout in self._patrouille_leden.values():
            if scout.title == "pl":
                self._pl = scout
        elif scout.title == "apl":
            self._apl = scout

        self._patrouille_leden.update({scout.name: scout})
        self._patrouille_count += 1
        self.calc_insigne_avg()

    def remove_scout(self, scout):
        if scout in self._patrouille_leden.values():
            if scout.title == "pl":
                self._pl = None
            elif scout.title == "apl":
                self._apl = None

            self._patrouille_leden.pop(scout.name)
            self.calc_insigne_avg()

    def is_scout_compatible(self, scout: Scout):
        s: Scout
        for s in self._patrouille_leden.values():
            if s.get_relation(scout) == -1:
                return True
        return True

    @property
    def name(self):
        return self._patrouille_name

    @property
    def leden(self):
        return self._patrouille_leden.values()

    @property
    def pl(self):
        return self._pl

    @property
    def apl(self):
        return self._apl

    def calc_insigne_avg(self):
        avg: int = 0
        s: Scout
        for s in self._patrouille_leden.values():
            avg += s.get_insigne()
        self._insigne_avg = avg / self._patrouille_count
        return self._insigne_avg

    def sort_on_title(self):
        sortedValues: Dict = sorted(self._patrouille_leden.values(), key=self._title_filter)
        sortedDict: Dict[str, Scout] = {}
        scout: Scout
        for scout in sortedValues:
            sortedDict[scout.name] = scout

        self._patrouille_leden = sortedDict

    def _title_filter(self, scout: Scout):
        if scout.title == 'pl':
            return 0
        elif scout.title == 'apl':
            return 1
        else:
            return 2

    def clear(self):
        self._patrouille_leden.clear()

    def get_scout(self, scout_name):
        return self._patrouille_leden[scout_name]