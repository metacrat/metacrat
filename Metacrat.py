import tweepy
import random
import os
from os import environ

def tweetIt():
    auth = tweepy.OAuthHandler(environ["consumer_key"],environ["consumer_secret"])
    auth.set_access_token(environ["access_key"],environ["access_secret"])
    api = tweepy.API(auth)
    hfileWithTweets = open("BotResults.txt","r")
    allTweets = hfileWithTweets.readlines()
    hfileWithTweets.close()
    tweetIndex = random.randint(0, len(allTweets))
    if (isOdd(tweetIndex)):
        tweetIndex -= 1
    api.update_status(status = (allTweets[tweetIndex]))

def isOdd(my_number):
    return my_number % 2 == 1

tweetIt()