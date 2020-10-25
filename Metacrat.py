import tweepy
import random
import os
from os import environ
import time

def init():
    global allTweets, api
    auth = tweepy.OAuthHandler(environ["consumer_key"],environ["consumer_secret"])
    auth.set_access_token(environ["access_key"],environ["access_secret"])
    api = tweepy.API(auth)
    hfileWithTweets = open("BotResults.txt","r")
    allTweets = hfileWithTweets.readlines()
    hfileWithTweets.close()

def tweetIt():
    global allTweets, api
    tweetIndex = random.randint(0, len(allTweets))
    if (isOdd(tweetIndex)):
        tweetIndex -= 1
    api.update_status(status = (allTweets[tweetIndex]))
    print("sending tweet " + allTweets[tweetIndex])

def isOdd(my_number):
    return my_number % 2 == 1

init()
while True:
    tweetIt()
    time.sleep(3 * 60 * 60)