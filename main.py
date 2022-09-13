import sqlite3
from tkinter import *
import datetime
import time
import winsound

con = sqlite3.connect("baza.db")
cur = con.cursor()
con.execute("""CREATE TABLE IF NOT EXISTS data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, hours INTEGER NOT NULL, minutes INTEGER NOT NULL, seconds INTEGER NOT NULL)""")
con.commit()
con.close()


# Функція яка свіряє введену дату з глобальной датой та записує в базу даних
def alarm(set_alarm_timer):
    sc = sec.get()
    hr = hour.get()
    mn = min.get()
    con = sqlite3.connect("baza.db")
    cur = con.cursor()
    my_data = (hr,mn,sc)
    my = "INSERT INTO data (hours, minutes, seconds) VALUES (?,?,?)"
    con.execute(my,my_data)
    con.commit()
    con.close()
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
                print("Time to Wake up ")
                break
# Функція яка приймає данні 
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

#Интерфейс
clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")

addTime = Label(clock,text = "Hour   Min   Sec",font=60).place(x = 100)

hour = StringVar()
min = StringVar()
sec = StringVar()



hourTime= Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=90,y=30)
minTime= Entry(clock,textvariable = min,bg = "white",width = 15).place(x=130,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 15).place(x=170,y=30)


submit = Button(clock,text = "Set Alarm",fg="black",width = 10,command = actual_time).place(x =145,y=70)

clock.mainloop()
