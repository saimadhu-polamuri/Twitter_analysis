import tweepy
consumer_key = 'YUV7jXYy6CfokA2Q2rEQShy3A'
consumer_secret = 'sWZIH0gY8kmY4Dxq2fZykyP0vL99cMlogkoAAg8SKpzYtSWWyR'
access_token = '2862312312-2JWFBNB3ghJBaZGpZSBlfUWYKOsyDQhxKifajzG'
access_token_secret = '0hFQtyOMgyslDdywGaY9rU71a40n394BrqDUzN07UOM6o'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)
# Function to get user tweets
def get_usertweets(user_name):
	user = api.get_user(user_name)
	time_line = user.timeline(count=30)
	for single_tweet in time_line:
		#print single_tweet.text
		print unicode(single_tweet.text).encode('ascii','ignore')

# Fucntion to get followers tweetes
def get_followers_tweets(user):
	for single_user in user.followers():
		print ">>>>>>>>>>>>>>>>>",single_user.screen_name
		get_usertweets(single_user.screen_name)

# Function to get only user tweets
def get_only_usertweets(user):
	time_line = user.timeline()
	for single_tweet in time_line:
		#print ">>>>>>"
		if user.id == single_tweet.user.id:
			if single_tweet.text[0] != '@' and single_tweet.text[0:2] != 'RT':
				#print single_tweet.text
				#print unicode(single_tweet.text).encode('ascii','ignore')
				#print single_tweet.id
				#status_update(single_tweet.text)
				api.update_status(single_tweet.text)
				print "successfully Updated"
# Fuction to update status
def status_update(text):
	#api = tweepy.API(auth)
	api.update_status(text)
	print "successfully updated"
api = tweepy.API(auth)
user = api.get_user('saimadhup')        
get_only_usertweets(user)