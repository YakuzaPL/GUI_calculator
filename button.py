from tkinter import END


class My_button:
    def __init__(self, value, entry_box):
        self.value = value
        self.entry_box = entry_box

    def text(self):
        return str(self.value)

    def value(self):
        return int(self.value)

    def click_button(self):
        current = self.entry_box.get()
        self.entry_box.delete(0, END)
        self.entry_box.insert(0, str(current) + str(self.value))
