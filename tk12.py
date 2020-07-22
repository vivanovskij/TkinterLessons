from tkinter import *

root = Tk()
root.geometry('600x400+100+100')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    print('Super mega program!')

# main_menu.add_command(label='File')
# main_menu.add_command(label='About')


# Menu File
menu_file = Menu(main_menu, tearoff=0)
menu_file.add_command(label='Open')
menu_file.add_command(label='Save')
menu_file.add_separator()
menu_file.add_command(label='Exit')
main_menu.add_cascade(label='File', menu=menu_file)

# Menu About
menu_about = Menu(main_menu, tearoff=0)
menu_about_sub = Menu(menu_about, tearoff=0)
menu_about_sub.add_command(label='Online')
menu_about_sub.add_command(label='Offline')
menu_about.add_cascade(label='Help', menu=menu_about_sub)
menu_about.add_separator()
menu_about.add_command(label='About', command=about_program)
main_menu.add_cascade(label='Help', menu=menu_about)

frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=True)


txt_area = Text(frame_text, bg='#343d46', fg='#c6dec1', padx=10,
                pady=10, wrap=WORD, insertbackground='#fff', spacing3=10)
txt_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=txt_area.yview)
scroll.pack(fill=Y, side=LEFT)
txt_area.config(yscrollcommand=scroll.set)

root.mainloop()
