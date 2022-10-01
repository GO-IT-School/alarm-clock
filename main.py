import sqlite3
from tkinter import *
import datetime
import time
import winsound
from threading import Thread


con = sqlite3.connect("tutorial.db")
cur = con.cursor()
con.execute("""CREATE TABLE IF NOT EXISTS data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, hours INTEGER NOT NULL, minutes INTEGER NOT NULL, seconds INTEGER NOT NULL)""")
con.commit()
con.close()
clock = Tk()
def interface():
    global hour
    global min
    global sec
    clock.title("DataFlair Alarm Clock")
    clock.geometry("400x200")

    addTime = Label(clock,text = "Hour   Min   Sec",font=60).place(x = 110)

    hour = StringVar()
    min = StringVar()
    sec = StringVar()



    hourTime= Entry(clock,textvariable = hour,bg = "white",width = 5).place(x=110,y=30)
    minTime= Entry(clock,textvariable = min,bg = "white",width = 5).place(x=150,y=30)
    ecTime = Entry(clock,textvariable = sec,bg = "white",width = 5).place(x=190,y=30)


    submit = Button(clock,text = "Set Alarm",fg="black",width = 10,command = actual_time).place(x =120,y=70)



# Функція яка свіряє введену дата з глобальной датой
def alarm(set_alarm_timer):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * FROM data ORDER BY ROWID DESC"""
    cur.execute(sqlite_select_query)
    record = cur.fetchone()
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
    sc = sec.get()
    hr = hour.get()
    mn = min.get()
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    my_data = (hr,mn,sc)
    my = "INSERT INTO data (hours, minutes, seconds) VALUES (?,?,?)"
    con.execute(my,my_data)
    con.commit()
    con.close()
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * FROM data ORDER BY ROWID DESC"""
    cur.execute(sqlite_select_query)
    record = cur.fetchone()
    con.commit()
    con.close()
    set_alarm_timer = '{}:{}:{}'.format(record[1],record[2],record[3])
    alarm(set_alarm_timer)



th2= Thread(target=alarm, args=())

th = Thread(target=actual_time, args=())

th3 = Thread(target=interface, args=())
th3.start()
th.start()
th2.start()

interface()
clock.mainloop()