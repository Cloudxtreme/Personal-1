# Enter in an Isbn and get book information via Google books
# and enter it into a local mysql database

import urllib2, json, mysql.connector, time, os

apikey = "AIzaSyDozlghDCtPzYu9ckvt1jhkjinZpM3vhJQ"
#cnx = mysql.connector.connect(user='root', database='booksread', buffered=True)
#cursor = cnx.cursor()
url = 'https://www.googleapis.com/books/v1/volumes?q=Isbn:'

class book_data():

        def __init__(self, Isbn):
            self.Isbn = Isbn

        def grab_json(self, Isbn):

            final_url = url + Isbn
            json_obj = urllib2.urlopen(final_url)
            jsonData = json.load(json_obj)
            return jsonData

        def check_for_book(self, Isbn):

            if self.grab_json(Isbn)['totalItems'] == 0:
                return False
            else:
                # entry exsists on google books
                return True

        def Isbn_false(self, Isbn):
            print "\n Google Books does not have this book :( \n"
            # Google books doesn't have the book, so all values must
            # be manually put in
            Name = raw_input("Name: ")
            AuthorName = raw_input("Author's Name: ")
            DateFinished = raw_input("Date Finished (year-month-day): ")
            Pages = raw_input("Pages: ")
            Rating = raw_input("raw_input: ")
            Notes = raw_input("Notes: ")

            book_data = {
                'Name': Name,
                'AuthorName': AuthorName,
                'Rating': Rating,
                'DateFinished': DateFinished,
                'Pages': Pages,
                'Isbn': Isbn,
                'Notes': Notes }

            return book_data

        def Isbn_true(self, Isbn):

            #all the json data from google books
            jsonData = self.grab_json(Isbn)

            #Pulling information for the dict from the json
            Name = jsonData['items'][0]['volumeInfo']['title']
            AuthorName = jsonData['items'][0]['volumeInfo']['authors'][0]
            DateFinished = time.strftime("%Y-%m-%d")
            Pages = jsonData['items'][0]['volumeInfo']['pageCount']
            Rating = raw_input("Rating: ")
            Notes = raw_input("Notes: ")

            #A dict of the information above
            book_data = {
                 'Name': Name,
                 'AuthorName': AuthorName,
                 'Rating': Rating,
                 'DateFinished': DateFinished,
                 'Pages': Pages,
                 'Isbn': Isbn,
                 'Notes': Notes,
                 }

            return book_data

        def insert_into_database(self, Isbn):

            if self.check_for_book(Isbn) == True:
                book_dict = self.Isbn_true(Isbn)
            else:
                book_dict = self.Isbn_false(Isbn)

            cnx = mysql.connector.connect(user='root', password='CuIeyy7j!!', database='booksread', buffered=True)
            cursor = cnx.cursor()

            #enter the data into the database
            add_book = ("INSERT INTO booksread "
                             "(Name,AuthorName,Rating,DateFinished,Pages,Isbn,Notes) "
                             "VALUES (%(Name)s, %(AuthorName)s, %(Rating)s, %(DateFinished)s, %(Pages)s, %(Isbn)s, %(Notes)s)")
            cursor.execute(add_book, book_dict)

            print "\n"
            print "Entered into the database:\n\n"

            for k,v in book_dict:
                print k,v

            cnx.commit()
            cursor.close()
            cnx.close()

def main():
    print "#################\n"
    print "Book Database\n"
    print "#################\n\n"

    Isbn = raw_input("Isbn: ")
    books = book_data(Isbn)
    books.insert_into_database(Isbn)

main()
