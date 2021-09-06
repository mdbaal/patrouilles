from tkinter import *


class UIListFrame(Frame):
    def __init__(self, master=None, title=None, select_command=None):
        super().__init__(master, borderwidth=10, bg="lightgrey")
        # size rows and columns for full width and height
        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        # Add frame title
        self.title_label: Label = None

        if title is not None or "":
            self.title_label = Label(self, text=title)
            self.title_label.grid(row=0, columnspan=2, sticky="EW")

        self.listItems = Listbox(self, selectmode=SINGLE, borderwidth=3, selectbackground="grey")
        self.listItems.grid(row=2, columnspan=2, sticky="NSEW")
        self._current_selected = None
        self.select_command = select_command
        self.listItems.bind("<<ListboxSelect>>", self._select)
        self.listItems.bind("<FocusOut>", self._select)

    # Edit title
    def update_title(self, new_title):
        if self.title_label is None:
            self.title_label = Label(self)
            self.title_label.grid(row=0, columnspan=2, sticky="EW")

        self.title_label.config(text=new_title)

    # Add an item to the list
    def add_item(self, labelText):
        if labelText is not None or "":
            self.listItems.insert(END, labelText)

    # Remove an item from the list via index
    def remove_item(self):
        self.listItems.delete(self.get_current_item())

    def remove_item_by_name(self, item):
        self.listItems.delete(self.get_index_by_name(item))

    def get_item(self, index):
        if self.listItems.size() > 0 or index is not None:
            return self.listItems.get(index)

            return None

    def get_item_by_name(self, name):
        return self.get_item(self.get_index_by_name(name))

    def get_index_by_name(self, name):
        for i, item in enumerate(self.listItems.get(0, END)):
            if item == name:
                return i
        return 0

    def get_current_item(self):
        return self._current_selected

    def get_current_item_name(self):
        return self.get_item(self._current_selected)

    def get_all_items(self):
        return self.listItems.get(0, END)

    def delete(self, start, last=None):
        self.listItems.delete(start, last)

    def _select(self, event):
        index = self.listItems.curselection()
        if index == ():
            return

        self._current_selected = index

        if self.select_command is not None:
            self.select_command()
