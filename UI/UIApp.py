from tkinter import *
from AppController import AppController
from .UIListFrame import UIListFrame
from .PopupWindows.InputWindow import InputWindow
from .PopupWindows.MessageWindow import MessageWindow
from .PopupWindows.EditScoutWindow import EditScoutWindow


class App(Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Patrouille Generator")
        self.maxsize()
        self.appControl = AppController()
        print(self.appControl)
        self.popUpWindow = None
        self.setupFrame()

    def setupFrame(self):
        # Row 1 Info lists
        Grid.rowconfigure(self, 1, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 2, weight=1)
        # TODO 1 Make function to open window for new scout
        # TODO 2 Make function to take data and create scout
        # TODO 3 Make function to add it to unassigned list
        # TODO 4 Make function to remove selected scout from unassigned
        # Todo 5 Make function to open create new Patrouille window
        # TODO 6 Make function to assign scouts to patrouille
        # TODO 7 Make function to see assigned scouts per patrouille and title with insigne level
        # TODO 8 Make function to edit selected scout
        # TODO 9 Make Create / Edit scout so that relations are multi select list
        # Todo 10 Make Make Create / Edit scout so that insignel level is a dropdown/num field

        patrouillesList = UIListFrame(master=self, title="Patrouilles")
        patrouilleScouts = UIListFrame(master=self, title="Patrouille Leden")
        unAssignedScouts = UIListFrame(master=self, title="Geen Patrouille")

        patrouillesList.grid(row=1, column=0, sticky="NSEW", padx=10)

        patrouilleScouts.grid(row=1, column=1, sticky="NSEW", padx=10)

        unAssignedScouts.grid(row=1, column=2, sticky="NSEW", padx=10)

        # Row 2 column 0 Patrouille control Buttons
        patrouilleControl = Frame(self)
        patrouilleControl.grid(row=2, column=0, padx=5, pady=5)

        b1 = Button(patrouilleControl, text="New Scout", command=self.MakeInputWindow)
        b2 = Button(patrouilleControl, text="Delete Scout", command=self.MakeMsgWindow)
        b3 = Button(patrouilleControl, text="Edit Scout", command=self.MakeEditScoutWindow)

        b1.grid(row=0, column=0, padx=2, pady=2)
        b2.grid(row=0, column=1, padx=2, pady=2)
        b3.grid(row=0, column=2, padx=2, pady=2)

        # Row 2 column 1 Patrouille Leden control Buttons
        patrouilleLeden = Frame(self)
        patrouilleLeden.grid(row=2, column=1, padx=5, pady=5)

        bb1 = Button(patrouilleLeden, text="New Patrouille")
        bb2 = Button(patrouilleLeden, text="Delete Patrouille")
        bb3 = Button(patrouilleLeden, text="Edit Patrouille")

        bb1.grid(row=0, column=0, padx=2, pady=2)
        bb2.grid(row=0, column=1, padx=2, pady=2)
        bb3.grid(row=0, column=2, padx=2, pady=2)

        # Row 2 column 2 Geen patrouille control Buttons
        geenPatrouille = Frame(self)
        geenPatrouille.grid(row=2, column=2, padx=5, pady=5)

        bbb1 = Button(geenPatrouille, text="New Scout")
        bbb2 = Button(geenPatrouille, text="Delete Scout")
        bbb3 = Button(geenPatrouille, text="Assign Scout")
        bbb4 = Button(geenPatrouille, text="Edit Scout")

        bbb1.grid(row=0, column=0, padx=2, pady=2)
        bbb2.grid(row=0, column=1, padx=2, pady=2)
        bbb3.grid(row=0, column=2, padx=2, pady=2)
        bbb4.grid(row=0, column=4, padx=2, pady=2)

    def MakeInputWindow(self):
        return InputWindow(master=self, title="New Scout")

    def MakeMsgWindow(self):
        return MessageWindow(master=self, title="Oops")

    def MakeEditScoutWindow(self):
        return EditScoutWindow(master=self, title="Edit this bitch")
