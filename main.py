from tkinter import *
from buttons import Buttons

numbers = [(7, 8, 9), (4, 5, 6), (1, 2, 3)]

root = Tk()
root.title("My first calculator")
entry_box = Entry(root, width=40, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

for row in range(1, 4):
    for column in range(0, 3):
        button_value = numbers[row - 1][column]
        calc_button = Buttons(button_value, entry_box)
        Button(root, text=calc_button.text(), padx=40, pady=20,
               command=calc_button.click_button).grid(row=row, column=column)

# zero button
zero_button_value = 0
zero_button = Buttons(zero_button_value, entry_box)
button_0 = Button(root, text=str(zero_button_value), padx=87, pady=20,
                  command=zero_button.click_button).grid(row=5, column=0, columnspan=2)

mainloop()
