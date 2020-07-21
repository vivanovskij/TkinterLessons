from tkinter import *

root = Tk()
root.geometry('200x300+400+300')
root['bg'] = '#333'


def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)


l = Label(root)
e = Entry(root, width=30, justify=CENTER)
l.pack()
e.pack()

colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}

for k, v in colors.items():
    Button(root, bg=k,
           command=lambda hex=k, name=v:
           get_color(name, hex)
           ).pack(fill=X)

root.mainloop()
