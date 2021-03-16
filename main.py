from tkinter import *
from button import My_button

numbers = [(7, 8, 9), (4, 5, 6), (1, 2, 3)]

root = Tk()
root.title("My first calculator")
entry_box = Entry(root, width=40, borderwidth=6)
entry_box.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


def button_clear():
    entry_box.delete(0, END)


def button_add():
    first_number = entry_box.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry_box.delete(0, END)


def button_equal():
    second_number = entry_box.get()
    entry_box.delete(0, END)

    if math == "addition":
        entry_box.insert(0, f_num + int(second_number))
    if math == "subtraction":
        entry_box.insert(0, f_num - int(second_number))
    if math == "multiplication":
        entry_box.insert(0, f_num * int(second_number))
    if math == "division":
        entry_box.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = entry_box.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry_box.delete(0, END)


def button_multiply():
    first_number = entry_box.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry_box.delete(0, END)


def button_divide():
    first_number = entry_box.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry_box.delete(0, END)


for row in range(1, 4):
    for column in range(0, 3):
        button_value = numbers[row - 1][column]
        calc_button = My_button(button_value, entry_box)
        Button(root, text=calc_button.text(), padx=40, pady=20,
               command=calc_button.click_button).grid(row=row, column=column)

# zero button
zero_button_value = 0
zero_button = My_button(zero_button_value, entry_box)
button_0 = Button(root, text=str(zero_button_value), padx=87, pady=20,
                  command=zero_button.click_button).grid(row=5, column=0, columnspan=2)

# equal button
button_equal = Button(root, text='=', padx=40, pady=20, command=button_equal).grid(row=5, column=2)

button_add = Button(root, text='+', padx=38, pady=20, command=button_add).grid(row=2, column=4)
button_clear = Button(root, text='CE', padx=36, pady=20, command=button_clear).grid(row=6, column=4)
button_subtract = Button(root, text='-', padx=40, pady=20, command=button_subtract).grid(row=3, column=4)
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply).grid(row=5, column=4)
button_divide = Button(root, text='/', padx=40, pady=20, command=button_divide).grid(row=1, column=4)

mainloop()
