import os
import twitter
import tweepy as tw
from TwitterInfluence import *
import datetime
import urllib
import re
import twarc

def Analyze(url):
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

    #extracts the tweet_id
    url = url.split('/')[-1]

    # gets the avaliable information from the tweet
    tweet = api.get_status(url)

    print("Tweet url:" + url)
    print("Posted by: " + str(tweet.user.screen_name) +" " + str(tweet.user.name))
    print("Date posted: " + str(tweet.created_at) )
    print("The Number of likes is: " + str(tweet.favorite_count))
    print("The Number of retweets is: " + str(tweet.retweet_count))
    print("Posted in: " + str(tweet.user.location))


    scr= str(tweet.user.screen_name)
    # get number of likes retweets and replies
    replies = []
    for t in tw.Cursor(api.search, q='to:'+scr, result_type='recent', timeout=999999).items(1000):
        if hasattr(t, 'in_reply_to_status_id_str'):
            if (t.in_reply_to_status_id_str == url):
                print("Here")
                replies.append(t)

    print("Num replies: " + str(len(replies)))

    print("For user: " + str(tweet.user.screen_name))
    print("Lifetime tweets: " + str(tweet.user.statuses_count))

    # Amount of likes for all of user's tweets
    numRetweets=0
    for i in tweet.GetUserTimeline(tweet.user.screen_name):
        numRetweets += i.retweet_count

    # Amount of likes for all of user's tweets
    numLikes=0
    for i in tweet.GetUserTimeline(tweet.user.screen_name):
        numLikes += i.favorite_count

    numReplies = 0
    for t in tw.Cursor(api.search, q='to:'+scr, result_type='recent', timeout=999999).items(1000):
        if hasattr(t, 'in_reply_to_status_id_str'):
            if (t.in_reply_to_status_id_str == url):
                numReplies += 1



    print("Lifetime likes: " + str(numLikes))
    print("Lifetime retweets: " + str(numRetweets))
    print("Lifetime comments: " + str(numReplies))

    num = len(replies)
    #print(replies[0].user.screen_name)

    ti = TwitterInfluence()

    ti.insert_user(str(tweet.user.screen_name), str(tweet.user.name))
    ti.insert_tweet(url, tweet.created_at, tweet.favorite_count, tweet.user.location, tweet.user.screen_name, num)
    ti.insert_posts(tweet.user.screen_name, str(url))

    for usr in replies:
        ti.insert_retweet(str(url), tweet.created_at, tweet.favorite_count, tweet.user.location, usr.user.screen_name)

    # Problem with isa table
        #!!!!! All retweets have same tweet id




#retweeters_list = api.retweeters(url))

#for id in api.retweeters(url):
#    print (api.get_user(id).screen_name)
