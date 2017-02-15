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

def getTime():
    i = datetime.datetime.now()
    #format for column 00-00-0000
    date = "{}-{}-{}".format(i.month, i.day, i.year)
    return date


def createTable():
    c.execute('''CREATE TABLE if not exists workouts(id INTEGER PRIMARY KEY,
                 time text, machineNumber TEXT, weight TEXT, reps TEXT)''')
    print "==> Tables did not exsist. Tables created"

def insertValues(machineNumber, weight, reps):
    t = (getTime(), machineNumber, weight, reps)
    c.execute('INSERT INTO workouts VALUES (NULL, ?, ?, ?, ?)', t)
    conn.commit()
    print "==> Data entered\n"
    print "==============\n"

def questions():
    print "Gym - Data Input\n"

    # Display data of last visit
    machineNumber = raw_input("==> Machine Number: ")
    dataQuery = c.execute("select * from workouts where machineNumber={} order by time desc limit 1".format(machineNumber))
    getData = c.fetchone()
    print "\nLast time: "
    print "==> Date: {}".format(getData[1])
    print "==> Weight: {}".format(getData[3])
    print "==> Reps: {}\n".format(getData[4])

    weight = raw_input("==> Weight: ")
    reps = raw_input("==> Reps: ")
    data = [machineNumber, weight, reps]
    return data

conn = sqlite3.connect('gymDatabase.db')
c = conn.cursor()

try:
    if os.path.getsize('gymDatabase.db') == 0:
        createTable()

    data = questions()

    while str(data[0].lower()) != 'q':
        insertValues(data[0], data[1], data[2])
        questions()
    else:
        pass

finally:
    conn.close()
