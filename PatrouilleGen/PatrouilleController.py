from typing import List

from .Patrouille import Patrouille
from .Scout import Scout


class PatrouilleController:
    def __init__(self):
        self._patrouilles = {

        }

    def AddPatrouille(self, naam: str):
        patrouille = Patrouille(naam)
        self._patrouilles.update({naam: patrouille})

    def RemovePatrouille(self, naam) -> List[Scout]:
        # Get the patrouille and scouts
        patrouille: Patrouille = self._patrouilles.get(naam)
        leden: List[Scout] = list(patrouille.Leden)
        # Clear the patrouille
        patrouille.clear()
        self._patrouilles.pop(naam)
        del patrouille
        # return list of scouts
        return leden

    def ChangeNamePatrouille(self, oldNaam, newNaam):
        patrouille = self._patrouilles.get(oldNaam, None)
        if patrouille is not None:
            self.AddPatrouille(newNaam)
            self._patrouilles[newNaam] = patrouille
            self.RemovePatrouille(oldNaam)

    def GetPatrouilles(self):
        return self._patrouilles.values()

    def GetPatrouille(self, naam) -> Patrouille:
        return self._patrouilles[naam]

    def AddScoutToPatrouille(self, naam, scout: Scout):
        self._patrouilles[naam].AddScout(scout)

    def RemoveScoutFromPatrouille(self, naam, scout: Scout):
        self._patrouilles[naam].RemoveScout(scout)

    def TransferScoutToPatrouille(self, naam, scout: Scout):
        self.RemoveScoutFromPatrouille(naam, scout)
        self.AddScoutToPatrouille(naam, scout)


    # temp methods
    def printPatrouilles(self):
        pat: Patrouille
        for pat in self._patrouilles.values():
            print(f"{pat.Naam} : Insigne avg: {pat.CalcInsigneAvg():.2f}")
            s: Scout
            for s in pat.Leden:
                print(f"{s.Title} {s.Naam}  Insigne: {s.GetInsigneLevel()} \n")
