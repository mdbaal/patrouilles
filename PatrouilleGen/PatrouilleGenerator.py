import math
from typing import List

from .Patrouille import Patrouille
from .PatrouilleController import PatrouilleController
from .Scout import Scout
from .ScoutController import ScoutController


class PatrouilleGenerator:

    def __init__(self):
        pass

    def generate_patrouilles(self, patrouille_controller: PatrouilleController, scout_controller: ScoutController,
                             patrouille_names: List):
        _unassigned = scout_controller.get_unassigned_scouts()
        _patrouilleSize = math.ceil(len(_unassigned) / len(patrouille_names))

        for patrouille_name in patrouille_names:
            patrouille_controller.add_patrouille(patrouille_name)

        patrouille: Patrouille
        while len(_unassigned) > 0:
            for patrouille in patrouille_controller.get_patrouilles():
                # ignore full patrouilles
                if len(patrouille.leden) == _patrouilleSize:
                    continue

                scout: Scout
                for scout in _unassigned:
                    if scout.title == "pl" and patrouille.pl is not None:
                        break
                    if scout.title == "apl" and patrouille.apl is not None:
                        break

                    if len(patrouille.leden) == 2 or patrouille.is_scout_compatible(scout):
                        patrouille.add_scout(scout)
                        scout.set_patrouille(patrouille.name)
                        _unassigned.remove(scout)
                        break

        for patrouille in patrouille_controller.get_patrouilles():
            patrouille.sort_on_title()
