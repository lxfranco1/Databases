import os
import twitter
import tweepy as tw
import pandas as pd

#api = twitter.Api(consumer_key='TEQxvBQ2BVUAt0OnoAMIA0yWh',
#                  consumer_secret='8YbxHRXnVTzKYPs8Qg4mzd7oD9DFAvbwDfVxdhmljeOlFuSP5j',
#                  access_token_key='2173222812-UpKnOtwJI2TEd29ubii368C9mzE0KZOYw2qUz4y ',
#                  access_token_secret='yGXhsuTrXJ3zJV5P4oizxGc7lq2CV5TlOZTChjR0ApWII')

consumer_key='TEQxvBQ2BVUAt0OnoAMIA0yWh'
consumer_secret='8YbxHRXnVTzKYPs8Qg4mzd7oD9DFAvbwDfVxdhmljeOlFuSP5j'
access_token='2173222812-UpKnOtwJI2TEd29ubii368C9mzE0KZOYw2qUz4y'
access_token_secret='yGXhsuTrXJ3zJV5P4oizxGc7lq2CV5TlOZTChjR0ApWII'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

'''
search_words = "#wildfires"
date_since = "2019-10-10"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(6)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
'''

#goes to my timeline and prints out the tweets on my timeline
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''

# gets the url from the user
url = input ("Enter a tweet URL: ")

#extrats the tweet_id
url = url.split('/')[-1]

# gets the avaliable information from the tweet
tweet = api.get_status(url)
print("The Number of Retweets is: " + str(tweet.retweet_count))
print("The Number of likes is: " + str(tweet.favorite_count))
