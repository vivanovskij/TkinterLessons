from tkinter import *

root = Tk()
root.geometry('600x400+100+100')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    print('Super mega program!')


def change_theme(theme):
    txt_area['bg'] = theme_colors[theme]['txt_bg']
    txt_area['fg'] = theme_colors[theme]['txt_fg']
    txt_area['selectbackground'] = theme_colors[theme]['select_bg']
    txt_area['insertbackground'] = theme_colors[theme]['cursor']


    # Menu File
menu_file = Menu(main_menu, tearoff=0)
menu_file.add_command(label='Open')
menu_file.add_command(label='Save')
menu_file.add_separator()
menu_file.add_command(label='Exit')
main_menu.add_cascade(label='File', menu=menu_file)

# Menu Theme
menu_theme = Menu(main_menu, tearoff=0)
menu_theme_sub = Menu(menu_theme, tearoff=0)
menu_theme_sub.add_command(label='Dark', command=lambda: change_theme('dark'))
menu_theme_sub.add_command(
    label='Light', command=lambda: change_theme('light'))
menu_theme.add_cascade(label='Theme', menu=menu_theme_sub)
menu_theme.add_separator()
menu_theme.add_command(label='About', command=about_program)
main_menu.add_cascade(label='Theme', menu=menu_theme)

frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=True)

theme_colors = {
    'dark': {
        'txt_bg': '#343d46',
        'txt_fg': '#c6dec1',
        'cursor': '#fff',
        'select_bg': '#4e5a65'
    },
    'light': {
        'txt_bg': '#fff',
        'txt_fg': '#000',
        'cursor': '#8800ff',
        'select_bg': '#777'
    }
}


txt_area = Text(frame_text, bg=theme_colors['dark']['txt_bg'],
                fg=theme_colors['dark']['txt_fg'],
                padx=10, pady=10,
                wrap=WORD,
                insertbackground=theme_colors['dark']['cursor'],
                selectbackground=theme_colors['dark']['select_bg'],
                spacing3=10)

txt_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=txt_area.yview)
scroll.pack(fill=Y, side=LEFT)
txt_area.config(yscrollcommand=scroll.set)

root.mainloop()
