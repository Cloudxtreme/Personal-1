from twython import Twython, TwythonError
import datetime
import json
import sqlite3
import argparse
import pprint
import os
import sys


# Don't forget to add keys here ( apps.twitter.com )
consumer_key = "TmA9a642mFLnB1osK0G9s2ZOu"
consumer_secret = "koj4LqnH6nSZa3xRliw7cXdFBJKsvRyEkNsuoDFyl1cAj7bZUh"
access_key = "3302059384-6eYqlUrwChRYTxFemghuxTkAQGObhtB0hbMFlzH"
access_secret = "iY379we0P017I5fmPHUX3PrcgGuAg1IYga1HWXx4zAdRg"

twitter = Twython(consumer_key, consumer_secret, access_key, access_secret)

screenNames = []
dbName = "tweets.db"


def createTables():
    """ Make sure table is created in databse file """

    try:
        if conn is not None:
            c.execute('''CREATE TABLE if not exists tweets(
                         timeCreated TEXT,
                         username TEXT,
                         tweetId TEXT,
                         tweetText TEXT,
                         tweetURL TEXT,
                         mailed INTEGER DEFAULT 0
                         )''')

    except (RuntimeError, TypeError, NameError) as e:
        print(e)


def getTimeline(username, tweetId):
    """ Takes the user screen name and gets the timeline json
         for it """
    userTimeline = twitter.get_user_timeline(
        screen_name=username,
        exclude_replies=True, since_id=tweetId)
    return userTimeline

def addNewUserToDatabase(username):
    '''
    Function will add new user to database and pull a series of initial
    tweets
    '''
    if os.path.isfile(dbName):
        print("-- Database Already Exists")
        pass
    else:
        print("++ Database has been created.")
        createTables()

    print("-- New User to add: {}".format(username))
    query = c.execute('SELECT count(*) from tweets where username=(?)', [username])
    if c.fetchone()[0] == 0:
        print("-- User Not in Database.")
        userTimeLine = twitter.get_user_timeline(
            screen_name=username,
            exclude_replies=True
        )

        for tweets in userTimeLine:
             timeCreated = tweets['created_at']
             tweetId = tweets['id']
             tweetText = tweets['text']
             tweetURL = 'https://twitter.com/{}/status/{}'.format(username, tweetId)

             insertTweet(timeCreated, username, tweetId, tweetText, tweetURL)
             print("++ Inserted ID: {}".format(tweetId))
             conn.commit()
    else:
        print("-- Username already exsists in Database")
        sys.exit(0)

def insertTweet(timeCreated, username, tweetId, tweetText, tweetURL):
    """ Insert last tweet into sqllite """
    t = (timeCreated, username, tweetId, tweetText, tweetURL, 0)
    try:
        tweetURL = 'https://twitter.com/{}/status/{}'.format(username, tweetId)
        c.execute('INSERT INTO tweets VALUES (?, ?, ?, ?, ?, ?)', t)
    except:
        print(Exception)
    finally:
        conn.commit()


def getLastIdforUser(username):
    """ Query sqlite3 database by username for max value of ID
        Returns: list item of ID """

    query = c.execute('SELECT max(tweetId) FROM tweets WHERE username=(?)', [username])

    if query == "None":
        return 0
    rows = list(c.fetchone())
    return rows

def listUsers():
    # query returns a tuple. The for loop is to convert to a list
    query = c.execute("SELECT distinct username from tweets;")
    names = []
    for name in query:
        names.append(name[0])
    return names



###########################################################################
''' Connect to Database '''
conn = sqlite3.connect(dbName)
c = conn.cursor()

###########################################################################
''' Create database if necessary'''
if os.path.isfile(dbName):
    print("-- Database {} exists already.".format(dbName))
    if os.path.getsize(dbName) == 0:
        createTables()
    else:
        pass

else:
    print("++ Creating Database file: {}".format(dbName))
    createTables()

###########################################################################
'''
* Establish argparse
* --add - adds a new user to the database and fetches last tweets
'''
# If there are arguments
if len(sys.argv) > 2:
    parser = argparse.ArgumentParser(description='Add/Edit/Delete users')
    parser.add_argument('--add',
                        nargs=1,
                        help="add a username to be followed")

    # parser.add_argument('--delete',
    #                     nargs=1,
    #                     help="stop following a user")
    args = parser.parse_args()
    username = args.add[0]

    addNewUserToDatabase(username)
    print("++ New user added to database")

else:
    pass

###########################################################################

followedUsers = listUsers()

for user in followedUsers:
    print("++ Starting User: {}".format(user))

    lastTweetId = getLastIdforUser(user)
    print ("-- Last TweetID: {}".format(lastTweetId))

    userTimeline = getTimeline(user, lastTweetId)

    for tweets in userTimeline:
         timeCreated = tweets['created_at']
         tweetId = tweets['id']
         tweetText = tweets['text']
         tweetURL = 'https://twitter.com/{}/status/{}'.format(user, tweetId)

         insertTweet(timeCreated, user, tweetId, tweetText, tweetURL)
         print("++ Inserted ID: {}".format(tweetId))

conn.close()
