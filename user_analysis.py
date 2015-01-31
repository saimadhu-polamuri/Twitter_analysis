# Quick Python script to analysis twitter user.
__autor__ = 'saimadhu'
__createdon__ = '21-jan-2015'

import tweepy
import re
import commands
import os
import datetime
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
from dateutil import parser
import collections
from collections import Counter

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
        self.user = self.api.get_user(screen_name = self.profile_screen_name)
        # self.now = datetime.datetime.now()
        # print self.now
        self.now =  parse(commands.getoutput("date"))
        self.today =  self.get_datetime(self.now.ctime()) 
        #print self.today

    def user_latest_tweets(self):

        """ Function to get user latest tweets """

        
        time_line = self.user.timeline()
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

    def avg_tweets_month(self):

        """ Returns the average tweets per month """

        tweets_and_dates_dict = {}
        time_line = self.user.timeline()
        for single_tweet in time_line:
            tweets_and_dates_dict[single_tweet.created_at] = self.tweet_purely(single_tweet.text)
        od = collections.OrderedDict(sorted(tweets_and_dates_dict.items()))
        datetime_list = od.keys()
        datetime_list.reverse()
        # print datetime_list
        result = self.time_difference_seconds(datetime_list[0],datetime_list[-1]) / (len(datetime_list)-1)
        return result,datetime_list
        # return datetime_list

        

    def get_datetime(self,date):

        """ Returns date from string """

        self.date = date
        result = parser.parse(self.date,dayfirst=True)
        return result

    def user_followers_following_statistics(self):

        """ Function to analysis user follower and following data to get some statistics """

        # user_following_count = self.user.friends_count
        # user_followers_count = self.user.followers_count
        # created_date = self.user.created_at
        statistics_dict = {}
        statistics_dict['user_following_count'] = self.user.friends_count
        statistics_dict['user_followers_count'] = self.user.followers_count
        statistics_dict['created_date'] = self.user.created_at
        datetime_data = self.get_months(self.user.created_at)
        statistics_dict['number_of_seconds'] = datetime_data['seconds']
        statistics_dict['number_of_monts'] = datetime_data['months']
        #statistics_dict['total_months'] = 
        #statistics_dict['average_month_following'] = 
        #return following_count,followers_count
        #user_follower_members = 
        #return user_following_count,user_followers_count,created_date
        
        return statistics_dict



    def get_months(self,user_created_date):

        """ Function to return number of months passed after user created twitter account """

        self.user_created_date = user_created_date
        datetime = {}
        result = relativedelta(self.today,self.user_created_date)
        total_days = (result.years * 365) + (result.months * 30) + result.days
        total_seconds = (result.years*31556926)+(result.months*2629744)+(result.days*86400)+(result.hours*3600)+(result.minutes*60)+(result.seconds)
        datetime['seconds'] = total_seconds
        datetime['months'] = total_days /30
        return datetime

    def most_retweeted_tweets(self):

        """ Function to get user most retweeted tweets  """
        
        most_retweeted = self.user.retweets_of_me()
        for single_tweet in most_retweeted:
            print single_tweet.text

    def tweet_purely (self,tweet_text):

        """ Function to pure tweet text """

        self.tweet_text = tweet_text

        s = unicode(self.tweet_text).encode('ascii','ignore')
        return s.encode("utf-8")

    def seconds_ymwdhms(self,seconds,granularity = 5):

        """ return years, months, weeks, days, hours, min, sec from seconds """

        self.seconds = seconds
        self.granularity = granularity
        result = []
        intervals = (
            ('years',31556926), # 60 *  60 * 24 * 30 * 12
            ('months',2629744), # 60 *  60 * 24 * 30
            ('weeks', 604800),  # 60 * 60 * 24 * 7
            ('days', 86400),    # 60 * 60 * 24
            ('hours', 3600),    # 60 * 60
            ('minutes', 60),
            ('seconds', 1),
            )
        for name, count in intervals:
            value = self.seconds // count
            if value:
                self.seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return ', '.join(result[:self.granularity])

    def time_difference_seconds(self, first_datetime, second_datetime):

        """  return the difference between two times in seconds """

        self.first_datetime = first_datetime
        self.second_datetime = second_datetime
        result = relativedelta(self.first_datetime,self.second_datetime)
        total_days = (result.years * 365) + (result.months * 30) + result.days
        total_seconds = (result.years*31556926)+(result.months*2629744)+(result.days*86400)+(result.hours*3600)+(result.minutes*60)+(result.seconds)
        return total_seconds

    def convert_datetime_format(self,datetime):

        """ Converts datetime to specific format """

        self.datetime = datetime
        d = datetime.strptime(str(self.datetime), '%Y-%m-%d %H:%M:%S')
        return d.strftime('%Y %b %d %H:%M:%S')

    def expected_next_tweet(self,last_tweet_datetime,avg_tweets_seconds):

        """ returns user expected next tweet datetime """

        self.last_tweet_datetime = last_tweet_datetime
        self.avg_tweets_seconds = avg_tweets_seconds
        next_tweet_time =  last_tweet_datetime+ timedelta(seconds= avg_tweets_seconds)
        return self.convert_datetime_format(next_tweet_time)

    def favorite_week(self, tweets_datetime_list):

        """ Returns user favorite week """
        weekdays_list = []
        self.tweets_datetime_list = tweets_datetime_list
        for single_datetime in self.tweets_datetime_list:
            weekdays_list.append(self.datetime_weekday(single_datetime))
            #print self.datetime_weekday(single_datetime)
        weeks_count = Counter(weekdays_list)
        weekdays_count_dict = {}
        for key, value in zip(weeks_count.keys(),weeks_count.values()):
            weekdays_count_dict[key] = value
        #return weekdays_list
        #return weekdays_count_dict
        return sorted([(value,key) for (key,value) in weekdays_count_dict.items()])[-1][1],weekdays_count_dict

    def datetime_weekday(self,datetime):

        """ Returns weekday for a given datetime """

        self.datetime = datetime
        return datetime.strptime(str(self.datetime),'%Y-%m-%d %H:%M:%S').strftime('%A')

    
def main():

    """ Main Function for creating UserAnalytics instance to use all the functions in UserAnalytics """

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    screen_name = 'saimadhup'
    useranalytics = UserAnalytics(api,screen_name)
    recent_tweets = useranalytics.user_latest_tweets()
    # print recent_tweets
    statistics_ = useranalytics.user_followers_following_statistics()
    print statistics_
    # print statistics_
    avg_tweets_seconds,tweets_datetime_list = useranalytics.avg_tweets_month()
    avg_datetime_to_tweet = useranalytics.seconds_ymwdhms(avg_tweets_seconds)
    expected_next_tweet = useranalytics.expected_next_tweet(tweets_datetime_list[0],avg_tweets_seconds)
    print avg_datetime_to_tweet
    print expected_next_tweet
    print tweets_datetime_list
    user_favorite_weekday,weekdays_count_dict = useranalytics.favorite_week(tweets_datetime_list)
    print user_favorite_weekday,weekdays_count_dict

if __name__ == "__main__":
    main()