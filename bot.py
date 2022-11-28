import os
import time
import tweepy
import KEYS

import services

API_KEY = KEYS.TWITTER_API_KEY
API_SECRET_KEY = KEYS.TWITTER_API_SECRET_KEY
ACCESS_TOKEN = KEYS.TWITTER_ACCESS_TOKEN
ACCESS_TOKEN_SECRET = KEYS.TWITTER_ACCESS_TOKEN_SCRET

def get_twitter_api():

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

    return twitter_api

def write_tweet():
    tweet,image = services.get_tweet()
    services.download_image(image)
    twitter_api = get_twitter_api()
    twitter_api.update_with_media('picture.jpg',status=tweet)

def run():
    while True:
        write_tweet()
        time.sleep(3600)

if __name__ == '__main__':
    run()
