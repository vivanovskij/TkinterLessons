from tkinter import *

root = Tk()
root.geometry('200x100+400+300')

frame_menu = Frame(root, bg='#1F252A', height=40)
frame_text = Frame(root)

frame_menu.pack(fill=X)
frame_text.pack(fill=BOTH, expand=True)

lb_menu = Label(frame_menu, text='Menu', bg='#2b3239', fg='#c6dec1', font='10')
lb_menu.place(x=10, y=10)

txt_area = Text(frame_text, bg='#343d46', fg='#c6dec1', padx=10, pady=10, wrap=WORD, insertbackground='#fff')
txt_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=txt_area.yview)
scroll.pack(fill=Y, side=LEFT)
txt_area.config(yscrollcommand=scroll.set)

root.mainloop()
