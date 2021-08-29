import math
from typing import List

from .Patrouille import Patrouille
from .Scout import Scout
from .PatrouilleController import PatrouilleController
from .ScoutController import ScoutController


class PatrouilleGenerator:

    def __init__(self):
        pass

    def GeneratePatrouilles(self, patrouilleControler: PatrouilleController, scoutController: ScoutController,
                            patrouilleNamen: List, patrouilleSize=5):
        _unassigned = scoutController.GetUnassignedScouts()
        _patrouilleSize = patrouilleSize
        _maxPatrouilles = len(patrouilleNamen)
        _patrouilleCount = 0
        if len(_unassigned) < _patrouilleSize:
            _patrouilleSize = len(_unassigned)

        index = 0
        scout: Scout
        _assigned = []
        for patcount in range(_maxPatrouilles):
            patrouilleControler.AddPatrouille(patrouilleNamen[patcount])

            for i, scout in reversed(list(enumerate(_unassigned))):
                if len(_assigned) == 0:
                    _assigned.append(scout)
                    _unassigned.remove(scout)
                    continue
                else:
                    s: Scout
                    for s in _assigned:
                        if scout.GetInsigneLevel() == s.GetInsigneLevel():
                            break
                        elif s.GetRelation(scout) > -1:
                            _assigned.append(scout)
                            patrouilleControler.AddScoutToPatrouille(patrouilleNamen[patcount], scout)
                            _unassigned.remove(scout)
                            break

                if len(_assigned) == _patrouilleSize:
                    break

    def GeneratePatrouilles2(self, patrouilleControler: PatrouilleController, scoutController: ScoutController,
                             patrouilleNamen: List, patrouilleSize=5):
        _unassigned = scoutController.GetUnassignedScouts()
        _patrouilleSize = patrouilleSize
        _maxPatrouilles = len(patrouilleNamen)
        if len(_unassigned) < _patrouilleSize:
            _patrouilleSize = len(_unassigned)

        for patcount in range(_maxPatrouilles):
            patrouilleControler.AddPatrouille(patrouilleNamen[patcount])

        scout: Scout
        pat: Patrouille
        index = len(_unassigned) - 1
        while len(_unassigned) > 0:
            index = len(_unassigned) - 1
            for pat in patrouilleControler.GetPatrouilles():
                # ignore full patrouilles
                if len(pat.Leden) == _patrouilleSize:
                    continue

                # go through unassigned scouts
                for i in _unassigned:
                    scout = i

                    # if leden empty or scout is compatible
                    if len(pat.Leden) == 0 or pat.IsScoutCompatible(scout):
                        pat.AddScout(scout)
                        _unassigned.remove(scout)
                        break
                    else:
                        _unassigned.remove(scout)
                        break

    def GeneratePatrouilles3(self, patrouilleControler: PatrouilleController, scoutController: ScoutController,
                             patrouilleNamen: List):
        _unassigned = scoutController.GetUnassignedScouts()
        _patrouilleSize = math.ceil(len(_unassigned)/len(patrouilleNamen))

        for patrouilleNaam in patrouilleNamen:
            patrouilleControler.AddPatrouille(patrouilleNaam)

        pat: Patrouille
        while len(_unassigned) > 0:
            for pat in patrouilleControler.GetPatrouilles():
                # ignore full patrouilles
                if len(pat.Leden) == _patrouilleSize:
                    continue

                scout: Scout
                for scout in _unassigned:
                    if scout.Title == "pl" and pat.PL is not None:
                        break
                    if scout.Title == "apl" and pat.APL is not None:
                        break

                    if len(pat.Leden) == 2 or pat.IsScoutCompatible(scout):
                        pat.AddScout(scout)
                        _unassigned.remove(scout)
                        break

        for pat in patrouilleControler.GetPatrouilles():
            pat.SortOnTitle();