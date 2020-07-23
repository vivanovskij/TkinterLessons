from tkinter import *

root = Tk()
root.geometry('400x300+500+300')


def f_event(event, key):
    print(key)


# l = Label(root, bg='#333')
# l.pack(expand=1, fill=X)
# l.bind('<Button-1>', f_event)

e = Entry(root, justify=CENTER, font='Arial 15')
e.pack(expand=1, fill=X, padx=10, pady=10)
e.bind('<Button-1>', lambda event, key='Left click': f_event(event, key))
e.bind('<Button-2>', lambda event, key='Middle click': f_event(event, key))
e.bind('<Button-3>', lambda event, key='Right click': f_event(event, key))

root.mainloop()
