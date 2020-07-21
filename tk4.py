from tkinter import *
# import time

root = Tk()
root.geometry('800x600+400+300')
root['bg'] = '#333'

# l = Label(root,
#           text='Текст в строке 1\nТекст в строке 2\nСтрока3',
#           bg='#333',
#           fg='#fff',
#           font=('Comic Sans MS', 16, 'bold'),
#           justify=RIGHT,
#           width='40',
#           height='10',
#           anchor='nw'
#           )

# l.pack(anchor=NW)

img = PhotoImage(file='python-logo.png')
l_logo = Label(root, image=img)
l_logo.pack()

root.mainloop()
