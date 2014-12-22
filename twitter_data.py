import tweepy
consumer_key = 'YUV7jXYy6CfokA2Q2rEQShy3A'
consumer_secret = 'sWZIH0gY8kmY4Dxq2fZykyP0vL99cMlogkoAAg8SKpzYtSWWyR'
access_token = '2862312312-Mevmn5Y3FlKptTc2QgqAxFS5Z9LUp0fNKUGqGHe'
access_token_secret = 'rJEVQCvPfJjmKRkJ1nPiDBVy6F8HU5kDQJxdko6TB8weS'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
#api = tweepy.API(auth,timeout=30.0)
api = tweepy.API(auth)
# Sample method, used to update a status
# public_tweets = api.home_timeline()
# print "started printing public_tweets"
# for tweet in public_tweets:
# 	print unicode(tweet.text).encode('ascii','ignore')
#     #print tweet.text
# #api.update_status('Welcome to DataAspirant!')
print "Status Successfuly update"

user = api.get_user('saimadhup')
time_line = user.timeline()
for single_tweet in time_line:
	print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
	print ("ID:", single_tweet.id)
	print ("User ID:", single_tweet.user.id)
   	print ("Text:", single_tweet.text)
  	print ("Created:", single_tweet.created_at)
  	print ("Contributors:", single_tweet.contributors)
  	print ("Favorited:", single_tweet.favorited)
  	print ("In reply to screen name:", single_tweet.in_reply_to_screen_name)
  	print ("In reply to status ID:", single_tweet.in_reply_to_status_id)
  	print ("In reply to status ID str:", single_tweet.in_reply_to_status_id_str)
  	print ("In reply to user ID:", single_tweet.in_reply_to_user_id)
  	print ("In reply to user ID str:", single_tweet.in_reply_to_user_id_str)
  	print ("Place:", single_tweet.place)
  	print ("Retweeted:", single_tweet.retweeted)
   	print ("Retweet count:", single_tweet.retweet_count)
   	print ("Source:", single_tweet.source)
   	print ("Truncated:", single_tweet.truncated)