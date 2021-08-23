import time
import json
from ScoutController import ScoutController
from PatrouilleController import PatrouilleController
from PatrouilleGenerator import PatrouilleGenerator
import random

scoutController = ScoutController()
patrouilleController = PatrouilleController()
patrouilleGenerator = PatrouilleGenerator()

if __name__ == '__main__':
    random.seed(time.time())

    with open('data/scouts.json') as scoutsJson:
        scoutData = json.load(scoutsJson)

    for s in scoutData["Scouts"]:
        scoutController.NewScout(s["Naam"], s["Leeftijd"], s["Insignelevel"], title=s["Title"])

    patrouilleGenerator.GeneratePatrouilles3(patrouilleController, scoutController, ["Beren", "Vossen", "Panters"])
    print(patrouilleController.printPatrouilles())

