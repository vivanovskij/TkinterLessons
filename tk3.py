from tkinter import *
import time

root = Tk()
root.geometry('600x400+400+300')
root.title('Counter')

def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')

clicks = 0
def count_click():
    global clicks
    clicks += 1
    root.title(f'Counter = {clicks}')

# btn_time = Button(root, text='Time', command=check_time)
btn_cnt = Button(root, text='Counter', command=count_click)

# btn_time.pack()
btn_cnt.pack()

root.mainloop()
