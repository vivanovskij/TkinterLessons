from tkinter import *
# from tkinter import ttk


def clicked():
    print('Done')


root = Tk()
root.geometry('400x300+500+300')

# btn = Button(root, text='Кнопка', command=clicked,
# width=8, height=2, font='Consolas 16 italic')

btn = Button(root, text='Button', command=clicked)
btn.configure(width=8, height=5)
btn['font'] = 'Consolas 16 italic'

btn.pack()
# btn2 = ttk.Button(root, text='Кнопка')
# btn2.pack()


root.mainloop()
