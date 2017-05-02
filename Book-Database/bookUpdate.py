# Enter in an Isbn and get book information via Google books
# and enter it into a local mysql database

import pymysql.cursors
import urllib2

apikey = "AIzaSyDozlghDCtPzYu9ckvt1jhkjinZpM3vhJQ"
url = 'https://www.googleapis.com/books/v1/volumes?q=Isbn:'



connection = pymysql.connect(
    user='root',
    password="CuIeyy7j!!",
    database='Booksread',
    host="nonstopflights.ddns.net",
    port=19234,
    cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:

        # getIdCountQuery = ("select ID from booksread;")
        # cursor.execute(getIdCountQuery)
        # data = cursor.fetchall()
        # bookIDs = []
        # for i in data:
        #     bookIDs.append(i['ID'])

        testQuery = "select Summery from booksread where ID={}".format("300")
        cursor.execute(testQuery)
        print cursor.fetchall()





finally:
    connection.close()
