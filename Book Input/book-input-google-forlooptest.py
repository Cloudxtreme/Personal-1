#Pull page numbers via API
#http://isbndb.com/api/v2/docs/books
# API KEY HD45DAPU

import urllib2
import json
import mysql.connector
import time
import os

cnx = mysql.connector.connect(user='root', database='booksread', buffered=True)
cursor = cnx.cursor()

query = "select ID from booksread where Pages='';"

cursor.execute(query)
results = cursor.fetchall()

for (ID) in results:
	print(ID[0])

cnx.commit()
cursor.close()
cnx.close()
