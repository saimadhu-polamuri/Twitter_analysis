import tweepy
import re
consumer_key = 'YUV7jXYy6CfokA2Q2rEQShy3A'
consumer_secret = 'sWZIH0gY8kmY4Dxq2fZykyP0vL99cMlogkoAAg8SKpzYtSWWyR'
access_token = '2862312312-2JWFBNB3ghJBaZGpZSBlfUWYKOsyDQhxKifajzG'
access_token_secret = '0hFQtyOMgyslDdywGaY9rU71a40n394BrqDUzN07UOM6o'

class UserAnalytics():

	""" Analysing user and getting some user statistics  """

	def __init__(self,api,profile_screen_name):

		""" Initial funtion to get profile_screen_name details """

		self.api = api
		self.profile_screen_name = profile_screen_name

	def user_latest_tweets(self):

		""" Function to get user latest tweets """

		user = self.api.get_user(screen_name = self.profile_screen_name)
		time_line = user.timeline()
		recent_tweets_list = []
		tweet_counter = 0
		#print len(time_line)
		for single_tweet in time_line:
			# print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
			# print ("ID:", single_tweet.id)
			# print ("Text:", self.tweet_purely(single_tweet.text))
			# print ("Created:", single_tweet.created_at)
			if (single_tweet.text[0] != '@' and single_tweet.text[:2] != 'RT' and tweet_counter <5):
				recent_tweets_list.append(self.tweet_purely(single_tweet.text))
				tweet_counter +=1

		return recent_tweets_list

	def tweet_purely (self,tweet_text):

		""" Function to pure tweet text """

		self.tweet_text = tweet_text
		
		s = unicode(self.tweet_text).encode('ascii','ignore')
		return s.encode("utf-8")


def main():

	""" Main Function for creating UserAnalytics instance to use all the functions in UserAnalytics """

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	screen_name = 'saimadhup'
	useranalytics = UserAnalytics(api,screen_name)
	recent_tweets = useranalytics.user_latest_tweets()
	print recent_tweets

if __name__ == "__main__":
	main()