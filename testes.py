from button import Button

numbers = [(7, 8, 9), (4, 5, 6), (1, 2, 3)]

for row in range(1, 4):
    print("row: " + str(row))
    for column in range(0, 3):
        button_text = str(numbers[row-1][column])
        button_value = numbers[row-1][column]

        button_new = Button(button_text, button_value)

        print("column: ", column)
        print("class text: ", button_new.text, type(button_new.text))
        print("class value: ", button_new.give_value(), type(button_new.value))



