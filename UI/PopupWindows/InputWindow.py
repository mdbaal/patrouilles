from tkinter import *


class InputWindow(Toplevel):
    def __init__(self, title=None, master=None, bg="lightgrey"):
        super().__init__(master, bg=bg)
        self.geometry("250x100")

        if title is not None:
            self.title(title)

        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.entry: Entry = Entry(self)
        self.entry.grid(row=0, columnspan=2, sticky="EW", padx=20, pady=10)
        self.entry.focus()
        self.button = Button(self, text="Submit", command=self._saveData)
        self.button.grid(row=1, columnspan=2, sticky="EW", padx=20, pady=10)
        self._input = ""

    def _saveData(self):
        self._input = self.entry.get()
        self.withdraw()

    # To get the input after window is closed
    def GetInput(self):
        return self._input
