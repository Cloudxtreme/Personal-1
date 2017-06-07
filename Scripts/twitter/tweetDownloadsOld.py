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

screenNames = ['neverminding']


def getTimeline(userName):
    """ Takes the user screen name and gets the timeline json
         for it """
    try:
        userTimeline = twitter.get_user_timeline(screen_name=userName,
                                                 exclude_replies=True)
        return userTimeline

    except TwythonError as e:
        print(e)


def createTable():
    c.execute('''CREATE TABLE if not exists tweets(id INTEGER PRIMARY KEY,
                 time text, username TEXT, lastTweetId TEXT)''')
    print "==> Tables did not exsist. Tables created"

def insertValues(username, lastTweetId):
    t = (username, lastTweetId)
    c.execute('INSERT INTO tweets VALUES (NULL, ?, ?)', t)
    conn.commit()
    print "==> Data entered\n"
    print "==============\n"


conn = sqlite3.connect('tweetIds.db')
c = conn.cursor()

for users in screenNames:
    """ Iterates through each user in screenNames """
    timeline = getTimeline(users)
    """ Iterates through tweets of that user """
    for tweets in timeline:
        # Dict for the tweet Ids to store MAX ID for future retrieval
        tweetsIdDicts = []

        for output in timeline:
            tweetId = output['id']
            tweetText = output['text']
            # tweetCreatedAt = output['created_at']
            # DEBUG
            # print(tweetId)
            # print(tweetText)
            # print(tweetCreatedAt)
            # print('\n')

            tweetsIdDicts.append(tweetId)

    maxTweetId = max(tweetsIdDicts)
    maxTweetIdDict = {users: maxTweetId}
    # DEBUG
    # print(maxTweetIdDict)
    # Write max ID to json file
    # with open('data.json', 'w') as fp:
    #    json.dump(maxTweetIdDict, fp)
