import sqlite3
from tkinter import *
import datetime
import time
import winsound
from threading import Thread


con = sqlite3.connect("baza.db")
cur = con.cursor()
con.execute("""CREATE TABLE IF NOT EXISTS data57 (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, hours TEXT NOT NULL, minutes TEXT NOT NULL)""")
con.commit()
con.close()


global hour
global min

hour = StringVar()
min = StringVar()


# Функція яка свіряє введену дата з глобальной датой
def alarm(set_alarm_timer):
    con = sqlite3.connect("baza.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * FROM data57 ORDER BY ROWID DESC"""
    cur.execute(sqlite_select_query)
    record = cur.fetchone()
    con.commit()
    con.close()
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%Y")
        if now == set_alarm_timer:
                print("Time to Wake up ")
                break
        
# Функція яка приймає данні 
def actual_time():
    hr = hour_val
    mn = minute_val
    con = sqlite3.connect("baza.db")
    cur = con.cursor()
    my_data = (hr,mn)
    my = "INSERT INTO data57 (hours, minutes) VALUES (?,?)"
    con.execute(my,my_data)
    con.commit()
    con.close()
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * FROM data57 ORDER BY ROWID DESC"""
    cur.execute(sqlite_select_query)
    record = cur.fetchone()
    con.commit()
    con.close()
    set_alarm_timer = '{}:{}'.format(record[1],record[2])
    alarm(set_alarm_timer)



th2= Thread(target=alarm, args=())

th = Thread(target=actual_time, args=())


th.start()
th2.start()

# Видалення діючого будильнику
def remove():
    stop_threads = False
    th2= Thread(target=alarm, args=(lambda : stop_threads, ))
    th2.start()
    time.sleep(1)
    stop_threads = True
    th2.join()
    con = sqlite3.connect("baza.db")
    cur = con.cursor()
    sqlite_select_query = """DELETE FROM data57 ORDER BY ROWID DESC"""
    con.commit()
    con.close()