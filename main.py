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
h = Entry(width=3, font=('Arial 24')) 
m = Entry(width=3, font=('Arial 24')) 
s = Entry(width=3, font=('Arial 24'))
lbl_date.grid(row=0, column=1)   
lbl_time.grid(row=2, column=1)
h.grid(row=3, column=0)
m.grid(row=3, column=1)
s.grid(row=3, column=2) 


def data_update():  
    while True:

        lbl_date['text'] = datetime.now().date()
        sleep(0.5)  

def time_update():  
    while True:

        lbl_time['text'] = str(datetime.now().time().strftime('%H:%M:%S'))
        sleep(0.5)


my_canvas = Canvas(win2, bg='#010502', width=190)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)



def alarm():
    a = h.get()
    b = m.get() 
    c = s.get()
    frame = Frame(my_canvas, bg='#010502', highlightbackground="white", highlightthickness=1)
    frame.pack()
    Label(frame, text=f"{a}:{b}:{c}",
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
    
       

button = Button(text="Зберегти",
    width=15,
    height=1,
    bg='#010502',
    fg = 'white',
    font = 'Franklin 17',
    command=alarm
    ) 
button.grid(row=4, column=1)

process = threading.Thread(target=time_update)  
process.start()  
process2 = threading.Thread(target=data_update) 
process2.start() 

win.mainloop()
