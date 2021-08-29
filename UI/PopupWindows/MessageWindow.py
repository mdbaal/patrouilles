from tkinter import *


class MessageWindow(Toplevel):
    def __init__(self, title=None, master=None, bg="lightgrey", message="Oops?"):
        super().__init__(master, bg=bg)
        self.geometry("250x100")

        if title is not None:
            self.title(title)

        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.label: Label = Label(self, text=message)
        self.label.grid(row=0, columnspan=2, sticky="EW", padx=20, pady=10)
        self.button = Button(self, text="OK", command=self.confirm)
        self.button.grid(row=1, columnspan=2, sticky="EW", padx=20, pady=10)

    def confirm(self):
        self.withdraw()

