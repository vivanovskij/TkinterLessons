from tkinter import *

root = Tk()
# root.geometry('600x400+400+300')

# f = Frame(root)
# f.pack(pady=10)

# btns = ('7', '8', '9',
#         '4', '5', '6',
#         '1', '2', '3',
#         '0')

# row = 0
# col = 0
# colspan = 1

# for b in btns:
#     Button(f, text=b, padx=10, pady=5).grid(
#         row=row, column=col, columnspan=colspan)
#     col += 1
#     if col == 3:
#         col = 0
#         row += 1
#     if row == 3:
#         colspan = 3

lb_login = Label(root, text='login:').grid(
    row=0, column=0, padx=10, pady=10, sticky=W)
entry_login = Entry(root).grid(
    row=0, column=1, columnspan=2, padx=10, sticky=W + E)
lb_pass = Label(root, text='password:').grid(
    row=1, column=0, padx=10, sticky=W)
entry_pass = Entry(root, show='*').grid(
    row=1, column=1, columnspan=2, padx=10, sticky=W + E)

btn_login = Button(root, text='Вход', padx=5).grid(
    row=2, column=0, padx=10, pady=10, sticky=W)
btn_reg = Button(root, text='Регистрация', padx=5).grid(row=2, column=1)
btn_forgot = Button(root, text='Забыли пароль',
                    padx=5).grid(row=2, column=2, padx=10)

root.mainloop()
