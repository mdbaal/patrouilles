import time
import json

from AppController import AppController
from PatrouilleGen import *

import random
from UI.UIApp import App

scoutController = ScoutController()
patrouilleController = PatrouilleController()
patrouilleGenerator = PatrouilleGenerator()
appControl = AppController()

if __name__ == '__main__':
    random.seed(time.time())
    appControl.Setup(scoutController,patrouilleController, patrouilleGenerator)
    print(appControl)
    with open('data/scouts.json') as scoutsJson:
        scoutData = json.load(scoutsJson)

    for s in scoutData["Scouts"]:
        scoutController.NewScout(s["Naam"], s["Leeftijd"], s["Insignelevel"], title=s["Title"])

    patrouilleGenerator.GeneratePatrouilles3(patrouilleController, scoutController, ["Beren", "Vossen", "Panters"])
    # print(patrouilleController.printPatrouilles())

    app = App()

    app.mainloop()

