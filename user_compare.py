import tweepy
consumer_key = 'YUV7jXYy6CfokA2Q2rEQShy3A'
consumer_secret = 'sWZIH0gY8kmY4Dxq2fZykyP0vL99cMlogkoAAg8SKpzYtSWWyR'
access_token = '2862312312-2JWFBNB3ghJBaZGpZSBlfUWYKOsyDQhxKifajzG'
access_token_secret = '0hFQtyOMgyslDdywGaY9rU71a40n394BrqDUzN07UOM6o'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
#api = tweepy.API(auth,timeout=30.0)
api = tweepy.API(auth)

# Function for comparing two twitter users
def compare_users(user1,user2):
	compare_dic = {}
	compare_dic['user1_followers_count'] = user1.followers_count
	compare_dic['user2_followers_count'] = user2.followers_count
	compare_dic['user1_friends_count'] = user1.friends_count
	compare_dic['user2_friends_count'] = user2.friends_count
	#user2.followers_count
	return compare_dic
user1 = api.get_user('saimadhup')
user2 = api.get_user('poorna145')
d = compare_users(user1,user2)
print d