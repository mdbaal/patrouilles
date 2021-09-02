from typing import List

from .Patrouille import Patrouille
from .Scout import Scout


class PatrouilleController:
    def __init__(self):
        self._patrouilles = {

        }

    def add_patrouille(self, name: str):
        patrouille = Patrouille(name)
        self._patrouilles.update({name: patrouille})

    def remove_patrouille(self, name) -> List[Scout]:
        # Get the patrouille and scouts
        patrouille: Patrouille = self._patrouilles.get(name)
        leden: List[Scout] = list(patrouille.leden)
        # Clear the patrouille
        patrouille.clear()
        self._patrouilles.pop(name)
        del patrouille
        # return list of scouts
        return leden

    def rename_patrouille(self, old_name, new_name):
        patrouille: Patrouille = self._patrouilles.get(old_name, None)
        if patrouille is not None:
            self.add_patrouille(new_name)
            self._patrouilles[new_name] = patrouille.__copy__()
            self.remove_patrouille(old_name)

    def get_patrouilles(self):
        return self._patrouilles.values()

    def get_patrouille(self, name) -> Patrouille:
        return self._patrouilles[name]

    def add_scout_to_patrouille(self, name, scout: Scout):
        self._patrouilles[name].add_scout(scout)

    def remove_scout_from_patrouille(self, name, scout: Scout):
        self._patrouilles[name].remove_scout(scout)

    def transfer_scout_to_patrouille(self, name, scout: Scout):
        self.remove_scout_from_patrouille(name, scout)
        self.add_scout_to_patrouille(name, scout)


    # temp methods
    def printPatrouilles(self):
        pat: Patrouille
        for pat in self._patrouilles.values():
            print(f"{pat.name} : Insigne avg: {pat.calc_insigne_avg():.2f}")
            s: Scout
            for s in pat.leden:
                print(f"{s.title} {s.name}  Insigne: {s.get_insigne()} \n")
