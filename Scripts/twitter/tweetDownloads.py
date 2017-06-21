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
    t = (username, lastTweetId, tweetText, 0)
    try:
        c.execute('INSERT INTO tweets VALUES (?, ?, ?, ?)', t)
    except:
        print("Insert Error")
    finally:
        conn.commit()


def getLastIdforUser(username):
    """ Query sqlite3 database by username for max value of ID
        Returns: list item of ID """
    # return to this query when it's working. Can't use for debug since it
    # only returns if they are new tweets
    query = c.execute('SELECT max(lastTweetId) FROM tweets WHERE username=(?)', (username, ))

    # test query will pull a random lastTweetID
    #query = c.execute('SELECT lastTweetId FROM tweets ORDER BY RANDOM() limit 1;')
    if query == "None":
        return 0
    rows = list(c.fetchone())
    return rows




###########################################################################

conn = sqlite3.connect(dbName)
c = conn.cursor()

createTables()

for user in screenNames:

    lastTweetId = getLastIdforUser(user)
    userTimeline = getTimeline(user, lastTweetId)

    for tweets in userTimeline:
        tweetId = tweets['id']
        tweetText = tweets['text']
        #
        # DEBUG
        #
        #print(tweetId)
        #print(tweetText)

        insertTweet(user, tweetId, tweetText)


conn.close()
