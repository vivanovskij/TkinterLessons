from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import os


def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)


def sort_files():
    cur_path = e_path.get()
    if cur_path:
        for file in os.listdir(cur_path):
            file_path = os.path.join(cur_path, file)
            if os.path.isfile(file_path):
                mtime = os.path.getmtime(file_path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d')
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(file_path, os.path.join(date_folder, file))
        messagebox.showinfo('Success', 'Done!')
        e_path.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Папка не выбрана!')



root = Tk()
root.title('FileSort')
root.geometry('400x110+200+200')
root.resizable(False, False)

style = ttk.Style()
style.configure('my.TButton', font=('Arial', 10, 'bold'))

frame = Frame(root, bg='#56adff', bd=5)
frame.pack(padx=10, pady=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, style='my.TButton',
                        text='Выбрать папку', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, style='my.TButton',
                       text='Начать сортировку', command=sort_files)
btn_start.pack(pady=5)


root.mainloop()
