# Enter in an Isbn and get book information via Google books
# and enter it into a local mysql database

import pymysql.cursors, json
import urllib2

url = 'https://www.googleapis.com/books/v1/volumes?q=Isbn:'

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
    cursorclass=pymysql.cursors.DictCursor,
    charset='utf8')

with connection.cursor() as cursor:
     # collect all of the ISBN
     getIdCountQuery = ("select ISBN from booksread;")
     cursor.execute(getIdCountQuery)
     data = cursor.fetchall()

     # add values to databaseISBNs
     for i in data: databaseISBNs.append(i['ISBN'])
     cursor.close()



    # loop through databaseISBNs
for bookISBN in databaseISBNs:
    with connection.cursor() as cursor:
        # using the ISBN, see if there is a summery already
        summeryAvail = cursor.execute("select Summery from booksread where ISBN=(%s)",(bookISBN))
        print summeryAvail
        #print "bookISBN: {}".format(bookISBN)
        #print "summeryAvail: {}".format(summeryAvail)

        try:
            bookData = getBookData(bookISBN)
            if bookISBN is not " " and summeryAvail == 1:
                bookDescription = bookData['items'][0]['volumeInfo']['description']
                bookUpdate = [bookDescription,bookISBN]
                #print bookDescription
                updateQuery = "update booksread set Summery=%s where ISBN=%s"
                print "Updated {}".format(bookISBN)

                cursor.execute(updateQuery,bookUpdate)
                connection.commit()

        except KeyError or UnicodeEncodeError:
            print "Key Error, ISBN: {}. Error: {}".format(bookISBN, KeyError)
            continue




connection.close()
