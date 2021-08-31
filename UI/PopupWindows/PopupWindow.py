from tkinter import *
from typing import Dict


class PopupWindow(Toplevel):

    def __init__(self, master, title, bg="lightgrey", submit_command=None):
        super().__init__(master, bg=bg)

        if title is not None:
            self.title(title)

        self._submit_command = submit_command
        self._input: Dict = {}

    # Submit data from window to function
    def submit(self):
        if self._submit_command is not None:
            self._submit_command(self._input)
        self.withdraw()

    # To get the input after window is closed
    def GetInput(self):
        return self._input
