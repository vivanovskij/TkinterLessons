from tkinter import *

root = Tk()
root.geometry('600x400+400+300')

l1 = Label(root, text='Однажды в студёную зимнюю пору', font=16, bg='#333', fg='#fff', padx=20, pady=10)
l2 = Label(root, text='Я из лесу вышел, был сильный мороз', font=16, bg='#333', fg='#fff', padx=20, pady=10)

l1.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
