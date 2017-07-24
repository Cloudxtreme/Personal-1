from twython import Twython, TwythonError
import datetime
import json
import sqlite3
import argparse
import logging
import os
import sys

# create logger with 'spam_application'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log = logging.FileHandler('logs/tweetToText.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log.setFormatter(formatter)
logger.addHandler(log)

# Don't forget to add keys here ( apps.twitter.com )
consumer_key = "TmA9a642mFLnB1osK0G9s2ZOu"
consumer_secret = "koj4LqnH6nSZa3xRliw7cXdFBJKsvRyEkNsuoDFyl1cAj7bZUh"
access_key = "3302059384-6eYqlUrwChRYTxFemghuxTkAQGObhtB0hbMFlzH"
access_secret = "iY379we0P017I5fmPHUX3PrcgGuAg1IYga1HWXx4zAdRg"

twitter = Twython(consumer_key, consumer_secret, access_key, access_secret)

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
            logger.info("++ Created new database tables.")

    except (RuntimeError, TypeError, NameError) as e:
        print(e)
        logger.error('++ Error creating database/tables')


def getTimeline(username, tweetId):
    """ Takes the user screen name and gets the timeline json
         for it """
    userTimeline = twitter.get_user_timeline(
        screen_name=username,
        exclude_replies=True, since_id=tweetId)
    logger.info('++ Got Timeline for %s with tweetId %s',username, tweetId)
    return userTimeline

def addNewUserToDatabase(username):
    '''
    Function will add new user to database and pull a series of initial
    tweets
    '''
    if os.path.isfile(dbName):
        print("-- Database Already Exists")
        logger.info('-- Database Already Exists')
        pass
    else:
        print("++ Database has been created.")
        createTables()
        logger.info('-- Database created')

    print("-- New User to add: {}".format(username))
    query = c.execute('SELECT count(*) from tweets where username=(?)', [username])
    if c.fetchone()[0] == 0:
        print("-- User Not in Database.")
        logger.info('-- User(%s) Not in Database', username)
        userTimeLine = twitter.get_user_timeline(
            screen_name=username,
            exclude_replies=True
        )
        logger.info('-- Retrieved %s timeline.', [username])

        for tweets in userTimeLine:
             timeCreated = tweets['created_at']
             tweetId = tweets['id']
             tweetText = tweets['text']
             tweetURL = 'https://twitter.com/{}/status/{}'.format(username, tweetId)

             insertTweet(timeCreated, username, tweetId, tweetText, tweetURL)
             print("++ Inserted ID: {}".format(tweetId))
             logger.info('++ Instered ID: %s for User: %s', tweetId, username)
             conn.commit()
    else:
        print("-- Username already exists in Database")
        logger.info('-- Username already exists in Database')
        sys.exit(0)

def insertTweet(timeCreated, username, tweetId, tweetText, tweetURL):
    """ Insert last tweet into sqllite """
    t = (timeCreated, username, tweetId, tweetText, tweetURL, 0)
    try:
        tweetURL = 'https://twitter.com/{}/status/{}'.format(username, tweetId)
        c.execute('INSERT INTO tweets VALUES (?, ?, ?, ?, ?, ?)', t)
        logger.debug('Inserted Data: %s, %s, %s, %s, %s', timeCreated, username, tweetId, tweetText, tweetURL)
    except:
        print(Exception)
        logger.info('Exception: %s', Exception)
    finally:
        conn.commit()


def getLastIdforUser(username):
    """ Query sqlite3 database by username for max value of ID
        Returns: list item of ID """

    query = c.execute('SELECT max(tweetId) FROM tweets WHERE username=(?)', [username])
    logger.info('GetLastIdForUser query: %s', query)
    if query == "None":
        logger.info('-- No previous tweets for User: %s', username)
        return 0
    rows = list(c.fetchone())
    logger.info('-- Last ID is %s for User: %s', rows, username)
    return rows

def listUsers():
    # query returns a tuple. The for loop is to convert to a list
    query = c.execute("SELECT distinct username from tweets;")
    names = []
    for name in query.fetchall():
         names.append(name[0])
         print(name)
    logger.info('Usernames in Database: %s', names)
    return names





###########################################################################
''' Connect to Database '''
conn = sqlite3.connect(dbName)
c = conn.cursor()
logger.info('-- Logging into Database')

###########################################################################
''' Create database if necessary'''
if os.path.isfile(dbName):
    print("-- Database {} exists already.".format(dbName))
    logger.info('--Database %s exists already.', dbName)
    if os.path.getsize(dbName) == 0:
        createTables()
        logger.info('Created database: %s', dbName)

else:
    print("++ Creating Database file: {}".format(dbName))
    logger.info('++ Creating Database file: %s', dbName)
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
    logger.info('++ New user added to database: %s', username)

###########################################################################
#
followedUsers = listUsers()
logger.info('Fetch list of users: %s', followedUsers)
for user in followedUsers:
    # gets a single username to then pull data for
    print("++ Starting User: {}".format(user))
    logger.info('++ Starting User: %s', user)

    # get last ID to not pull duplicate entries
    lastTweetId = getLastIdforUser(user)
    print ("-- Last TweetID: {}".format(lastTweetId))
    logger.info('-- Last TweetId: %s', lastTweetId)

    # twitter timeline object
    userTimeline = getTimeline(user, lastTweetId)
    logger.info('Fetch User %s Timeline: %s', user, userTimeline)

    for tweets in userTimeline:
        # insert each tweet to the database
         timeCreated = tweets['created_at']
         tweetId = tweets['id']
         tweetText = tweets['text']
         tweetURL = 'https://twitter.com/{}/status/{}'.format(user, tweetId)

         insertTweet(timeCreated, user, tweetId, tweetText, tweetURL)

         logger.info('Inserted UserName: %s - Tweet ID: %s', user, tweetId)
         print("++ Inserted ID: {}".format(tweetId))

conn.close()
logger.info('-- Update finished.')

import smtp
logger.info('-- Running smtp.py')
