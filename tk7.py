from tkinter import *

root = Tk()
root.geometry('200x300+400+300')
root['bg'] = '#333'


class MyButton:
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.btn = Button(root, bg=hex_color,
                          command=self.get_color).pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


l = Label(root)
e = Entry(root, width=30, justify=CENTER)
l.pack(fill=X)
e.pack(fill=X)

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
    MyButton(root, v, k)

root.mainloop()
