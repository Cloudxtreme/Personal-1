# Enter in an Isbn and get book information via Google books
# and enter it into a local mysql database

import pymysql.cursors, json
import urllib2, pprint

apikey = "AIzaSyDozlghDCtPzYu9ckvt1jhkjinZpM3vhJQ"
url = 'https://www.googleapis.com/books/v1/volumes?q=Isbn:'

bookISBN = ('0307278255')
databaseISBNs = []

def getBookData(Isbn):
    final_url = url + Isbn
    json_obj = urllib2.urlopen(final_url)
    jsonData = json.load(json_obj)
    return jsonData

def getDescription(bookData):
    description = bookData['items'][0]['volumeInfo']['description']
    print description

connection = pymysql.connect(
    user='root',
    password="CuIeyy7j!!",
    database='Booksread',
    host="nonstopflights.ddns.net",
    port=19234,
    cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
         # collect all of the ISBN
         getIdCountQuery = ("select ISBN from booksread;")
         cursor.execute(getIdCountQuery)
         data = cursor.fetchall()

         # add values to databaseISBNs
         for i in data: databaseISBNs.append(i['ISBN'])

         # loop through databaseISBNs
         for bookISBNs in databaseISBNs:

            # using the ISBN, see if there is a summery already
            summeryAvail = cursor.execute("select Summery from booksread where ISBN=%s",(bookISBNs))

            # skip entry with no ISBN or already has a summery
            if bookISBNs == "" or summeryAvail is not 1:
                 pass
            else:
                 #working
                 bookData = getBookData(bookISBN)
                 bookDescription = bookData['items'][0]['volumeInfo']['description']
                 bookUpdate = [bookDescription,bookISBNs]
                 updateQuery = "update booksread set Summery=%s where ISBN=%s"
                 print "Updated {}".format(bookISBNs)

                 cursor.execute(updateQuery,bookUpdate)

finally:
    connection.commit()
    connection.close()
