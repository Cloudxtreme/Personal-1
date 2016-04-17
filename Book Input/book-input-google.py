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

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

print "#################\n"
print "Book Database\n"
print "#################\n\n"


# User input for books
ISBN = raw_input("Enter ISBN: ")
Rating = raw_input("Rating: ")
NOTES = raw_input("Notes: ")

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

print "Name: " + Name
print "AuthorName: " + AuthorName
print "Date Finished: " + DateFinished
print "Pages of book: %s" % Pages
 
book_data = {
  'Name': Name,
  'AuthorName': AuthorName,
  'Rating': Rating,
  'DateFinished': DateFinished,
  'Pages': Pages,
  'ISBN': ISBN,
  'NOTES': NOTES,
}

#print "Name: %(Name)r" + "AuthorName: %(AuthorName)r" + "Rating: %(Rating)r" + "DateFinished: %(DateFinished)r" + "Pages: %(Pages)r" + "ISBN: %(ISBN)r" + "Notes: %(Notes)r" % (Name, AuthorName, Rating, DateFinished, Pages, ISBN, NOTES)

add_book = ("INSERT INTO booksread "
            "(Name,AuthorName,Rating,DateFinished,Pages,ISBN,NOTES) "
            "VALUES (%(Name)s, %(AuthorName)s, %(Rating)s, %(DateFinished)s, %(Pages)s, %(ISBN)s, %(NOTES)s)")

#enter the data into the database
cursor.execute(add_book, book_data)

print "\n"
print "Information entered into the database.\n\n"

cnx.commit()
cursor.close()
cnx.close()

