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
    def add_item(self, labelText):
        if labelText is not None or "":
            self.listItems.insert(END, labelText)

    # Remove an item from the list via index
    def remove_item(self):
        self.listItems.delete(self.listItems.curselection())

    def get_item(self, index):
        return self.listItems.get(index)

    def get_index_by_name(self, name):
        for i, item in enumerate(self.listItems.get(0, END)):
            if item == name:
                return i
        return 0

    def get_current_item(self):
        return self.get_item(self.listItems.curselection())
