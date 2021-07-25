from typing import Dict

from Scout import Scout


class Patrouille:
    def __init__(self, patrouilleNaam):
        self._patrouilleNaam = patrouilleNaam
        self._patrouilleLeden: Dict[str,Scout] = {

        }
        self._patrouilleCount = 0

        self._insigneAvg = 0

    def AddScout(self, scout):
        if scout in self._patrouilleLeden.values():
            if scout.Title == "pl":
                self._patrouilleLeden["pl"] = scout
        elif scout.Title == "apl":
            self._patrouilleLeden["apl"] = scout
        elif scout.Title == "lid":
            self._patrouilleLeden.update({scout.Naam + "{0}".format(self._patrouilleCount + 1): scout})
        self._patrouilleCount += 1
        self.CalcInsigneAvg()

    def RemoveScout(self, scout):
        if scout in self._patrouilleLeden.values():
            if scout.Title == "pl":
                self._patrouilleLeden.pop("pl")
            elif scout.Title == "apl":
                self._patrouilleLeden.pop("apl")
            elif scout.Title == "lid":
                self._patrouilleLeden.pop(scout.Naam + "{0}".format(self._patrouilleCount + 1))
        self.CalcInsigneAvg()

    def IsScoutCompatible(self, scout: Scout):
        s: Scout
        for s in self._patrouilleLeden.values():
            if s.GetRelation(scout) == -1:
                return False
        return True

    @property
    def Naam(self):
        return self._patrouilleNaam

    @property
    def Leden(self):
        return self._patrouilleLeden.values()

    def CalcInsigneAvg(self):
        avg: int = 0
        s: Scout
        for s in self._patrouilleLeden.values():
            avg += s.GetInsigneLevel()
        self._insigneAvg = avg / self._patrouilleCount
        return self._insigneAvg
