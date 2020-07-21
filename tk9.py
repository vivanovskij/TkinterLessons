from tkinter import *

root = Tk()
root.geometry('600x400+400+300')

f = Frame(root)
f.pack(pady=10)

btns = ('7', '8', '9',
        '4', '5', '6',
        '1', '2', '3',
        '0')

row = 0
col = 0
colspan = 1

for b in btns:
    Button(f, text=b, padx=10, pady=5).grid(
        row=row, column=col, columnspan=colspan)
    col += 1
    if col == 3:
        col = 0
        row += 1
    if row == 3:
        colspan = 3

test = 'Добавление строки'

root.mainloop()
