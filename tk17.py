from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import urllib.request
import json


root = Tk()
root.title('Конвертер валют')
root.geometry('300x250+300+200')
root.resizable(False, False)
START_AMOUNT = 1000

# JSON
try:
    html = urllib.request.urlopen(
        'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showinfo('Ошибка', 'Ошибка получения курсов валют')


# Functions
def exchage():
    for i in res_entries:
        count = res_entries.index(i)
        try:
            cash = float(e_uah.get())
            i.delete(0, END)
            exchange = float(JSON_object[count]['sale'])
            res = cash / exchange
            i.insert(0, round(res, 2))
        except:
            messagebox.showwarning('Неверный формат', 'Неверный формат числа')
            return


# Header Frame
header_frame = Frame(root)
header_frame.pack(fill=X)

# Header
h_font = 'Arial 12 bold'
currency_font = 'Arial 10'
h_bg = '#ccc'

header = ('Валюта', 'Покупка', 'Продажа')

for i in header:
    header_frame.grid_columnconfigure(header.index(i),
                                      weight=1)
    header_item = Label(header_frame, text=i, bg=h_bg,
                        font=h_font)
    header_item.grid(row=0, column=header.index(i), sticky=EW)


if JSON_object:
    for item in JSON_object:
        if item['ccy'] == 'BTC':
            continue
        currency = Label(header_frame, text=item['ccy'],
                         font=currency_font)
        currency.grid(row=1 + JSON_object.index(item), column=0, sticky=EW)
        buy = Label(header_frame, text=item['buy'], font=currency_font)
        buy.grid(row=1 + JSON_object.index(item), column=1, sticky=EW)
        sale = Label(header_frame, text=item['sale'], font=currency_font)
        sale.grid(row=1 + JSON_object.index(item), column=2, sticky=EW)


# Calc Frame
calc_frame = Frame(root, bg='#fff')
calc_frame.pack()
calc_frame.grid_columnconfigure(1, weight=1)

# UAH
l_uah = Label(calc_frame, text='UAH', font=currency_font, bg='#fff')
l_uah.grid(row=0, column=0, padx=10)
e_uah = ttk.Entry(calc_frame, font=currency_font, justify=CENTER)
e_uah.grid(row=0, column=1, pady=10, padx=10, sticky=EW)
e_uah.insert(0, START_AMOUNT)

# Button
btn_calc = Button(calc_frame, text='Обмен',
                  font=currency_font, command=exchage)
btn_calc.grid(row=0, column=2, sticky=EW, padx=10)

# Result Frame
res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)


res_entries = []
for item in JSON_object:
    if item['ccy'] == 'BTC':
        continue
    item_count = JSON_object.index(item)
    l_cur = Label(res_frame, text=item['ccy'], padx=10, font=currency_font)
    l_cur.grid(row=item_count, column=0)
    res_entries.insert(item_count, ttk.Entry(
        res_frame, justify=CENTER, font=currency_font))
    res_entries[item_count].grid(
        row=item_count, column=1)
    res_entries[item_count].insert(
        0, round(START_AMOUNT / float(item['sale']), 2))


root.mainloop()
