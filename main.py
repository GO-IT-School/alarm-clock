from email.headerregistry import ContentDispositionHeader
from sys import maxsize
import threading 
from  tkinter import *
from time import sleep
from datetime import timedelta, datetime
from turtle import bgcolor, color, right


win = Tk()
win.configure(bg='#010502') 
win.title('Clock')
win2 = Toplevel()
win2.configure(bg='#010502')
win2.title('Alarms')
lbl_date = Label(font='Franklin 30', bg='#010502', fg = 'white')
lbl_time = Label(font='Franklin 30', bg='#010502', fg = 'white')
hour = Entry(width=3, font=('Arial 24')) 
minute = Entry(width=3, font=('Arial 24')) 
second = Entry(width=3, font=('Arial 24'))
dot = Label(font='Franklin 30', bg='#010502', fg = 'white', text=":")
dot2 = Label(font='Franklin 30', bg='#010502', fg = 'white', text=":")
lbl_date.grid(row=0, column=1)   
lbl_time.grid(row=2, column=1)
hour.grid(row=3, column=0)
dot.place(x=85, y=90)
dot2.place(x=220, y=90)
minute.grid(row=3, column=1)
second.grid(row=3, column=2) 


def data_update():  
    while True:

        lbl_date['text'] = datetime.now().date()
        sleep(0.5)  

def time_update():  
    while True:

        lbl_time['text'] = str(datetime.now().time().strftime('%H:%M:%S'))
        sleep(0.5)


my_canvas = Canvas(win2, bg='#010502', width = 300)
my_canvas.grid(row=5, column=1)



def alarm():
    get_hour = hour.get()
    get_minute = minute.get() 
    get_second = second.get()
    frame = Frame(my_canvas, bg='#010502', highlightbackground="white", highlightthickness=1)
    frame.pack()
    Label(frame, text=f"{get_hour}:{get_minute}:{get_second}",
    font = 10,
    bg='#010502',
    fg = 'white').pack()
    Label(frame, text="Дата призначення:",
    font = 10,
    bg='#010502',
    fg = 'white').pack()
    Label(frame, text=datetime.now().date(),
    font = 10,
    bg='#010502',
    fg = 'white').pack()
    Label(frame, text=str(datetime.now().time().strftime('%H:%M:%S')),
    font = 10,
    bg='#010502',
    fg = 'white').pack()
    def clear_frame():
            frame.destroy()
    Button(frame, text = 'Видалити',  
    width=15,
    bg='#010502',
    fg = 'white',
    font = 10,
    command=clear_frame).pack()
    
       

save_button = Button(text="Зберегти",
    width=15,
    height=1,
    bg='#010502',
    fg = 'white',
    font = 'Franklin 17',
    command=alarm
    ) 
save_button.grid(row=4, column=1)

time_process = threading.Thread(target=time_update)  
time_process.start()  
data_process = threading.Thread(target=data_update) 
data_process.start() 

win.mainloop()
