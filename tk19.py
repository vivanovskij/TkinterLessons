# Review ttkthemes

# from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk


root = ThemedTk(theme='elegance')
root.geometry('400x300+300+200')

ttk.Button(root, text='Button').pack(pady=10)
ttk.Entry(root).pack()

root.mainloop()
