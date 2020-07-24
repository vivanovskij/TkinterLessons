# Weather application

from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time


API_KEY = '5e1ce895b1f7950c8267adecc8ce4989'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'


def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise_ts = weather['sys']['sunrise']
        sunset_ts = weather['sys']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime('%H:%M:%S', sunrise_struct_time)
        sunset = time.strftime('%H:%M:%S', sunset_struct_time)
        return f'Местоположение: {city}, {country}\
                \nТемпература: {temp}°C\
                \nДавление: {press} гПа\
                \nВлажность: {humidity} %\
                \nСкорость ветра: {wind} м/с\
                \nПогодные условия: {desc}\
                \nВосход: {sunrise}\
                \nЗакат: {sunset}'
    except:
        return 'Ошибка получения данных...'


def get_weather(event=''):
    if entry.get():
        params = {
            'appid': API_KEY,
            'q': entry.get(),
            'units': 'metric',
            'lang': 'ru'
        }
    req = requests.get(API_URL, params=params)
    weather = req.json()
    lbl['text'] = print_weather(weather)


root = ThemedTk(theme='ark')
root.geometry('500x400+300+200')
root.resizable(0, 0)

s = ttk.Style()
s.configure('TLabel', padding=5, font='Arial 12')

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)
entry.bind('<Return>', get_weather)

btn = ttk.Button(top_frame, text='Запрос погоды', command=get_weather)
btn.place(relx=0.7, relwidth=0.3, relheight=1)

low_frame = ttk.Frame(root)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

lbl = ttk.Label(low_frame, anchor='nw')
lbl.place(relwidth=1, relheight=1)


root.mainloop()
