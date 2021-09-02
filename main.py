from AppController import AppController
from PatrouilleGen import *

from UI.UIApp import App

scoutController = ScoutController()
patrouilleController = PatrouilleController()
patrouilleGenerator = PatrouilleGenerator()
appControl = AppController()

if __name__ == '__main__':
    # patrouilleGenerator.generate_patrouilles(patrouilleController, scoutController, ["Beren", "Vossen", "Panters"])

    app = App()
    appControl.setup(scoutController, patrouilleController, patrouilleGenerator, app)

    app.mainloop()

