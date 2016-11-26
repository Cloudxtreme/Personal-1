import oauth2 as oauth
import xmltodict, json, re
import goodreads
from string import Template
import urllib2

key = "XhzLPiBUeAA7naEBsXV6HQ"
secret= "mXYycHxp0THBZUWizuWJvotbYBheLBpcyZmKyqDqQ"

#oAuth tokens. Use goodreadsOAUTH script to obtain.

oauthtokenKey =    "QZ2pVLqDjmDg3zHT1b0vA"
oauthtokenSecret = "Uk55XKLhOacUjQGcjvr7xAHmaKVgE1nwH7VpSWp2o"

# base URL
url = 'https://www.goodreads.com'

#target_list = 'holding'

consumer = oauth.Consumer(key,secret)

token = oauth.Token(oauthtokenKey,oauthtokenSecret)

client = oauth.Client(consumer, token)

def getUserId():
    response, content = client.request('{}/api/auth_user'.format(url),'GET')
    #convert xml return to json
    userIdJsonDump = json.dumps(xmltodict.parse(content))
    #creates json object
    userIdJson = json.loads(userIdJsonDump)

    return userIdJson['GoodreadsResponse']['user']['@id']


def addABook(isbn):
    #converts isbn to good reads book ID
    book_id = getIdFromIsbn(isbn)
    print book_id
    #response, content = client.request('{}/shelf/add_to_shelf.xml'.format(url),'POST','read',str(book_id))
    # print response
    # print content
    #check that the new resource has been created
    # if response['status'] != '201':
    #     raise Exception('Cannot create resource: {}'.format(response['status']))
    # else:
    #     print 'Book added!'

def getUserShelf():
    userId = getUserId()
    response,content = client.request('{}/shelf/list.xml'.format(url),'GET',key,userId)
    shelfJsonDump = json.dumps(xmltodict.parse(content))
    shelfJson = json.loads(shelfJsonDump)
    shelves = []

    for x in shelfJson['GoodreadsResponse']['shelves']['user_shelf']:
        print x['name']

def getIdFromIsbn(isbn):
        #does not respond with normal XML values
        response,content = client.request('https://www.goodreads.com/book/isbn_to_id/' + isbn + '?key=' + key)
        #api has a bug that returns html comment, the following returns just the ID
        grID = list(content.split('<'))
        return grID[0].strip("\n")

def reviewsFromBookID(isbn):
    #converts isbn to good reads book ID
    book_id = getIdFromIsbn(isbn)
    response, content = client.request('{}/book/show.json'.format(url),'GET','json',key,book_id)
    print response
    print content



isbn = '1503938719'
# addABook(isbn)
reviewsFromBookID(isbn)
