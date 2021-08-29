from tkinter import *


class UIListFrame(Frame):
    def __init__(self, master=None, title=None):
        super().__init__(master, borderwidth=10, bg="lightgrey")
        # size rows and columns for full width and height
        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        # Add frame title
        if title is not None or "":
            self.title = Label(self, text=title)
            self.title.grid(row=0, columnspan=2, sticky="EW")

        self.listItems = Listbox(self, selectmode=SINGLE, borderwidth=3, selectbackground="grey")
        self.listItems.grid(row=2, columnspan=2, sticky="NSEW")

    # Add an item to the list
    def AddItem(self, labelText):
        if labelText is not None or "":
            self.listItems.insert(END, labelText)

    # Remove an item from the list via index
    def RemoveItem(self, index):
        self.listItems.delete(index)

