from twython import Twython, TwythonError
import datetime
import json
import sqlite3

# Don't forget to add keys here ( apps.twitter.com )
consumer_key = "TmA9a642mFLnB1osK0G9s2ZOu"
consumer_secret = "koj4LqnH6nSZa3xRliw7cXdFBJKsvRyEkNsuoDFyl1cAj7bZUh"
access_key = "3302059384-6eYqlUrwChRYTxFemghuxTkAQGObhtB0hbMFlzH"
access_secret = "iY379we0P017I5fmPHUX3PrcgGuAg1IYga1HWXx4zAdRg"

twitter = Twython(consumer_key, consumer_secret, access_key, access_secret)

screenNames = ['neverminding', 'jasonisbell']
dbName = "tweets.db"


def createTables():
    """ Make sure table is created in databse file """

    try:
        if conn is not None:
            c.execute('''CREATE TABLE if not exists tweets(
                         id INTEGER PRIMARY KEY,
                         username TEXT,
                         lastTweetId TEXT,
                         tweetText TEXT,
                         mailed INTEGER DEFAULT 0
                         )''')

    except (RuntimeError, TypeError, NameError) as e:
        print(e)


def getTimeline(username, tweetId):
    """ Takes the user screen name and gets the timeline json
         for it """
    userTimeline = twitter.get_user_timeline(
        screen_name=username,
        exclude_replies=True,
        since_id=tweetId)
    return userTimeline


def insertTweet(username, lastTweetId, tweetText):
    """ Insert last tweet into sqllite """
    t = (username, lastTweetId, tweetText)
    try:
        c.execute('INSERT INTO tweets VALUES (NULL, ?, ?, ?, NULL)', t)
    except EnvironmentError as e:
        print(e)
    finally:
        conn.commit()


def getLastIdforUser(username):
    """ Query sqlite3 database for username and max value of ID """
    query = c.execute('SELECT max(lastTweetId) FROM tweets WHERE username=(?)', (username, ))
    rows = list(c.fetchone())
    return rows


###########################################################################

conn = sqlite3.connect(dbName)
c = conn.cursor()

createTables()

for user in screenNames:
    print (getLastIdforUser(user))


conn.close()

    # userTimeline = getTimeline(users)
    # for tweets in userTimeline:
    #     tweetId = tweets['id']
    #     tweetText = tweets['text']
















# Iterates through each user in screenNames
# for users in screenNames:
#     # Get last tweet max value
#     c.execute('SELECT max(tweetId) from tweets where usernam')
#     # Get's user timeline json object
#
#     timeline = getTimeline(users)
#     """ Iterates through tweets of that user """
#     for tweets in timeline:
#         # Dict for the tweet Ids to store MAX ID for future retrieval
#         tweetsIdDicts = []
#
#         for output in timeline:
#             tweetId = output['id']
#             tweetText = output['text']
#             # tweetCreatedAt = output['created_at']
#             # DEBUG
#             # print(tweetId)
#             # print(tweetText)
#             # print(tweetCreatedAt)
#             # print('\n')
#
#             tweetsIdDicts.append(tweetId)
