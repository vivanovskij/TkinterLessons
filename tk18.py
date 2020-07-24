from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x300+300+200')

my_style = ttk.Style()
# my_style.theme_use('xpnative')
# print(my_style.theme_names(), my_style.theme_use())

# my_style.configure('.', background='red')
my_style.configure('TButton', padding=5)
my_style.configure('red.TButton', foreground='red')


Button(root, text='Button 1', padx=40, pady=5).pack(pady=10)
ttk.Button(root, text='Button 2', width=15).pack()
ttk.Button(root, text='Button 3', width=15, style='red.TButton').pack()

Entry(root).pack(pady=10)
ttk.Entry(root).pack()


def choose(event):
    print(cmbx.current(), cmbx.get())


cmbx = ttk.Combobox(root, values=['one', 'two', 'three'])
cmbx.current(1)
cmbx.bind('<<ComboboxSelected>>', choose)
cmbx.pack()

root.mainloop()
