from typing import Dict

from .Scout import Scout


class Patrouille:
    def __init__(self, patrouilleNaam):
        self._patrouilleNaam = patrouilleNaam
        self._patrouilleLeden: Dict[str, Scout] = {

        }
        self._patrouilleCount = 0

        self._insigneAvg = 0

        self._pl = None
        self._apl = None

    def AddScout(self, scout):
        if scout in self._patrouilleLeden.values():
            if scout.Title == "pl":
                self._pl = scout
        elif scout.Title == "apl":
            self._apl = scout

        self._patrouilleLeden.update({scout.Naam: scout})
        self._patrouilleCount += 1
        self.CalcInsigneAvg()

    def RemoveScout(self, scout):
        if scout in self._patrouilleLeden.values():
            if scout.Title == "pl":
                self._pl = None
            elif scout.Title == "apl":
                self._apl = None
            elif scout.Title == "lid":
                self._patrouilleLeden.pop(scout.Naam)
        self.CalcInsigneAvg()

    def IsScoutCompatible(self, scout: Scout):
        s: Scout
        for s in self._patrouilleLeden.values():
            if s.GetRelation(scout) == -1:
                return True
        return True

    @property
    def Naam(self):
        return self._patrouilleNaam

    @property
    def Leden(self):
        return self._patrouilleLeden.values()

    @property
    def PL(self):
        return self._pl

    @property
    def APL(self):
        return self._apl

    def CalcInsigneAvg(self):
        avg: int = 0
        s: Scout
        for s in self._patrouilleLeden.values():
            avg += s.GetInsigneLevel()
        self._insigneAvg = avg / self._patrouilleCount
        return self._insigneAvg

    def SortOnTitle(self):
        sortedValues: Dict = sorted(self._patrouilleLeden.values(), key=self.ScoutTitle)
        sortedDict: Dict[str, Scout] = {}
        scout: Scout
        for scout in sortedValues:
            sortedDict[scout.Naam] = scout

        self._patrouilleLeden = sortedDict

    def ScoutTitle(self, scout: Scout):
        if scout.Title == 'pl':
            return 0
        elif scout.Title == 'apl':
            return 1
        else:
            return 2

    def clear(self):
        self._patrouilleLeden.clear()