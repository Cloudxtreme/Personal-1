# Enter in an Isbn and get book information via Google books
# and enter it into a local mysql database

import pymysql.cursors, json
import urllib2

url = 'https://www.googleapis.com/books/v1/volumes?q=Isbn:'

def getBookData(Isbn):
    final_url = url + Isbn
    json_obj = urllib2.urlopen(final_url)
    jsonData = json.load(json_obj)
    return jsonData

def getDescription(bookData):
    description = bookData['items'][0]['volumeInfo']['description']
    print description

#pymysql connection to the server database
connection = pymysql.connect(
    user='root',
    password="CuIeyy7j!!",
    database='Booksread',
    host="nonstopflights.ddns.net",
    port=19234,
    cursorclass=pymysql.cursors.DictCursor,
    charset='utf8')

# Get user input for single summery update
print "Update Summery on Single ISBN:\n"
bookISBN = str(raw_input("ISBN to Update: "))

# loop through bookISBN
with connection.cursor() as cursor:

    try:
        bookData = getBookData(bookISBN)
        if bookISBN is not " ":
            bookDescription = bookData['items'][0]['volumeInfo']['description']
            bookUpdate = [bookDescription,bookISBN]
            #print bookDescription
            updateQuery = "update booksread set Summery=%s where ISBN=%s"
            #print "Updated {}".format(bookISBN)

            cursor.execute(updateQuery,bookUpdate)

            #commits changes to database
            connection.commit()


    except KeyError or UnicodeEncodeError:
        print "Key Error, ISBN: {}. Error: {}".format(bookISBN, KeyError)

    finally:
        connection.close()
