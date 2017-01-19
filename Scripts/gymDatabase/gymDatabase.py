import sqlite3
import os
import datetime

#layout
#id
#time (unix)
#machineNumber
#weight
#reps


dbName = "workouts"


def getTime():
    i = datetime.datetime.now()
    #format for column 00-00-0000
    date = "{}-{}-{}".format(i.month,i.day,i.year)
    return date

conn = sqlite3.connect('gymDatabase.db')
c = conn.cursor()

def createTable():
    c.execute('''CREATE TABLE if not exists workouts(id INTEGER PRIMARY KEY, time text, machineNumber TEXT, weight TEXT, reps TEXT)''')

def insertValues(machineNumber,weight,reps):
    t = (getTime(), machineNumber, weight, reps)
    c.execute('INSERT INTO workouts VALUES (NULL,?,?,?,?)',t)
    conn.commit()
    print ("==> Data entered")

def questions():
    machineNumber = input("==> Machine Number: ")
    weight = input("==> Weight: ")
    reps = input("==> Reps: ")
    data = [machineNumber, weight, reps]
    return data


def main():
    data = questions()
    insertValues(data[0], data[1], data[2])

<<<<<<< HEAD
    while data[0:2].lower() != 'q':

    else:
        conn.close()
=======

>>>>>>> cb111f336ec8c8a0727cb4065dd1dadec830afc4

main()
conn.close()
