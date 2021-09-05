from AppController import AppController
from PatrouilleGen import *

from UI.UIApp import App

scoutController = ScoutController()
patrouilleController = PatrouilleController()
patrouilleGenerator = PatrouilleGenerator()
appControl = AppController()

if __name__ == '__main__':

    app = App()
    appControl.setup(scoutController, patrouilleController, patrouilleGenerator, app)

    app.mainloop()

    # TODO make static tools script with filters etc used in project
    # TODO on delete scout clear all other relations

