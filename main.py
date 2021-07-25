import time

from ScoutController import ScoutController
from PatrouilleController import PatrouilleController
from PatrouilleGenerator import PatrouilleGenerator
import random

scoutController = ScoutController()
patrouilleController = PatrouilleController()
patrouilleGenerator = PatrouilleGenerator()

if __name__ == '__main__':
    random.seed(time.time())
    for i in range(15):
        scoutController.NewScout("scout{}".format(i), 12, random.randint(0, 4))

    patrouilleGenerator.GeneratePatrouilles2(patrouilleController, scoutController, ["Beren", "Vossen", "Panthers"])
    print(patrouilleController.printPatrouilles())

