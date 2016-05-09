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
ID = raw_input("Enter ID: ")
ISBN = raw_input("Enter ISBN: ")

#ISBN = raw_input('Enter ISBN: ')
final_url = url + ISBN

#open url and make a variable
json_obj = urllib2.urlopen(final_url)

#parse the url data with json
jsonData = json.load(json_obj)

#input pulled from json
Name = jsonData['items'][0]['volumeInfo']['title']
AuthorName = jsonData['items'][0]['volumeInfo']['authors'][0]
Pages = jsonData['items'][0]['volumeInfo']['pageCount']

#time.sleep(2)

book_data = {
  'ID': ID,
  'Name': Name,
  'AuthorName': AuthorName,
  'Pages': Pages,
  'ISBN': ISBN,
}

add_book = ("update booksread set Name=%(Name)s,AuthorName=%(AuthorName)s,\
Pages=%(Pages)s, ISBN=%(ISBN)s where ID=%(ID)s")

print "Name: " + Name
print "AuthorName: " + AuthorName
print "Pages of book: %s" % Pages
print "ISBN: " + ISBN

#enter the data into the database
cursor.execute(add_book, book_data)

print "\n"
print "Information entered into the database.\n\n"

#time.sleep(1)

cnx.commit()
cursor.close()
cnx.close()