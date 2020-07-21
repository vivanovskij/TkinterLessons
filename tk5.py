from tkinter import *

root = Tk()
root.geometry('800x600+400+300')
root['bg'] = '#333'


def add_str():
    e.insert(END, 'Hello!')


def del_str():
    e.delete(0, END)


def get_str():
    l_text['text'] = e.get()


l = Label(root, text='Ввод:')
l.pack()

e = Entry(root, show='*')
e.insert(0, 'Hello ')
e.insert(END, 'world!')
e.pack()

btn_add = Button(root, text='Add', command=add_str)
btn_del = Button(root, text='Delete', command=del_str)
btn_get = Button(root, text='Get', command=get_str)

btn_add.pack()
btn_del.pack()
btn_get.pack()

l_text = Label(root)
l_text.pack(fill=X)

root.mainloop()
