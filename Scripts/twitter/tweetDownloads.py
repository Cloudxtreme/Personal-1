import tweepy #https://github.com/tweepy/tweepy
import csv, pprint

#Don't forget to add keys here ( apps.twitter.com )
consumer_key = "TmA9a642mFLnB1osK0G9s2ZOu"
consumer_secret = "koj4LqnH6nSZa3xRliw7cXdFBJKsvRyEkNsuoDFyl1cAj7bZUh"
access_key = "3302059384-6eYqlUrwChRYTxFemghuxTkAQGObhtB0hbMFlzH"
access_secret = "iY379we0P017I5fmPHUX3PrcgGuAg1IYga1HWXx4zAdRg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def get_LatestTweets(screen_name):

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#50 Tweets are enough ( 200 max )
	new_tweets = api.user_timeline(screen_name = screen_name,count=50)

	#now insert them to alltweets list
	alltweets.extend(new_tweets)

	#new list
	outtweets = []

	#list to 2D array
	for tweet in alltweets:
		outtweets.extend( [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]] )


	# #Generate a new csvf
	# with open('%s_twitter.csv' % screen_name, 'wb') as f:
	# 	writer = csv.writer(f)
	# 	writer.writerow(["id","created_at","text"])
	# 	writer.writerows(outtweets)
	#
	# pass
def home_timeline():
	timeline = api.home_timeline()
	print timeline.text

def search_users(query):
	users = api.search_users(q=query)
	print dir(users)


home_timeline()
