# Enter in an ISBN and get book information via Google books
# and enter it into a local mysql database

import urllib2, json, mysql.connector, time, os

apikey = "AIzaSyDozlghDCtPzYu9ckvt1jhkjinZpM3vhJQ"
cnx = mysql.connector.connect(user='root', database='booksread', buffered=True)
cursor = cnx.cursor()
url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

def enter_book_data(ISBN,Rating,NOTES):
    #ISBN = raw_input('Enter ISBN: ')
    final_url = url + ISBN

    #open url and make a variable
    json_obj = urllib2.urlopen(final_url)

    #parse the url data with json
    jsonData = json.load(json_obj)

    #input pulled from json
    Name = jsonData['items'][0]['volumeInfo']['title']
    AuthorName = jsonData['items'][0]['volumeInfo']['authors'][0]
    DateFinished = time.strftime("%Y-%m-%d")
    Pages = jsonData['items'][0]['volumeInfo']['pageCount']


    book_data = {
      'Name': Name,
      'AuthorName': AuthorName,
      'Rating': Rating,
      'DateFinished': DateFinished,
      'Pages': Pages,
      'ISBN': ISBN,
      'NOTES': NOTES,
    }

    add_book = ("INSERT INTO booksread "
                "(Name,AuthorName,Rating,DateFinished,Pages,ISBN,NOTES) "
                "VALUES (%(Name)s, %(AuthorName)s, %(Rating)s, %(DateFinished)s, %(Pages)s, %(ISBN)s, %(NOTES)s)")

    #enter the data into the database
    cursor.execute(add_book, book_data)
    cnx.commit()
    cursor.close()
    cnx.close()

    print "#################\n"
    print "Book Database\n"
    print "#################\n\n"

    print "Name: " + Name
    print "AuthorName: " + AuthorName
    print "Date Finished: " + DateFinished
    print "Pages of book: %s" % Pages

    print "\nInformation entered into the database.\n\n"

def inputs():


def main():
    # User input for books
    ISBN = raw_input("Enter ISBN: ")
    Rating = raw_input("Rating: ")
    NOTES = raw_input("Notes: ")

    enter_book_data(ISBN, Rating, NOTES)

def notinDatabase():
    print "Unfortunately you'll have to enter a few things again..\n\n"

    ISBN = raw_input("Enter ISBN: ")
    AuthorName = raw_input("Enter Author's Name(First Name, Last Name): ")
    Name = raw_input("Enter Name: ")
    Rating = raw_input("Rating: ")
    NOTES = raw_input("Notes: ")
    DateFinished = time.strftime("%Y-%m-%d")
    Pages = raw_input("Pages: ")

    book_data = {
      'Name': Name,
      'AuthorName': AuthorName,
      'Rating': Rating,
      'DateFinished': DateFinished,
      'Pages': Pages,
      'ISBN': ISBN,
      'NOTES': NOTES,
    }

    add_book = ("INSERT INTO booksread "
                "(Name,AuthorName,Rating,DateFinished,Pages,ISBN,NOTES) "
                "VALUES (%(Name)s, %(AuthorName)s, %(Rating)s, %(DateFinished)s, %(Pages)s, %(ISBN)s, %(NOTES)s)")

    #enter the data into the database
    cursor.execute(add_book, book_data)
    cnx.commit()
    cursor.close()
    cnx.close()

try:
    main()
except:
    notinDatabase()
