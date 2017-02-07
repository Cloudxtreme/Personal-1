import sqlite3
import os
import datetime

#layout
#id
#time (unix)
#machineNumber
#weight
#reps

# no need to check for databasefile. If it doesn't exsist
# sqlite3 will create the database file for us.

dbName = "workouts"

def getTime():
    i = datetime.datetime.now()
    #format for column 00-00-0000
    date = "{}-{}-{}".format(i.month,i.day,i.year)
    return date


def createTable():
    c.execute('''CREATE TABLE if not exists workouts(id INTEGER PRIMARY KEY, time text, machineNumber TEXT, weight TEXT, reps TEXT)''')
    print "==> Does not exist. Database created"

def insertValues(machineNumber,weight,reps):
    t = (getTime(), machineNumber, weight, reps)
    c.execute('INSERT INTO workouts VALUES (NULL,?,?,?,?)',t)
    conn.commit()
    print ("==> Data entered")

def questions():
    machineNumber = raw_input("==> Machine Number: ")
    weight = raw_input("==> Weight: ")
    reps = raw_input("==> Reps: ")
    data = [machineNumber, weight, reps]
    return data

conn = sqlite3.connect('gymDatabase.db')
c = conn.cursor()

try:
    data = questions()
    while data[0].lower() != 'q':
            insertValues(data[0], data[1], data[2])
            questions()
except as e:
    print (e)

finally:
    conn.close()
