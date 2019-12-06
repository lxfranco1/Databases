import os
import twitter
import tweepy as tw
from TwitterInfluence import *
import datetime
import urllib
import re

# Links: https://twitter.com/briannafrank10/status/1145125054524612608
# Links: https://twitter.com/Nataajah_I/status/1201967123008040973

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

    # Get the replies to the tweet
    replies = []
    for t in tw.Cursor(api.search, q='to:'+scr, result_type='recent', timeout=999999).items(1000):
        if hasattr(t, 'in_reply_to_status_id_str'):
            if (t.in_reply_to_status_id_str == url):
                # print("Here")
                replies.append(t)

    print("Num replies: " + str(len(replies)))

    print("For user: " + str(tweet.user.screen_name))
    print("Lifetime tweets: " + str(tweet.user.statuses_count))

    # Amount of likes for all of user's tweets
    numRetweets=0
    for i in api.user_timeline(screen_name=tweet.user.screen_name):
        numRetweets += i.retweet_count

    # Amount of likes for all of user's tweets
    numLikes=0
    for i in api.user_timeline(screen_name=tweet.user.screen_name):
        numLikes += i.favorite_count

    # Total number of replies for user
    numReplies = 0
    for t in tw.Cursor(api.search, q='to:'+scr, result_type='recent', timeout=999999).items(1000):
        if hasattr(t, 'in_reply_to_status_id_str'):
            # print("Lifetime replies")
            if (t.in_reply_to_status_id_str == url):
                numReplies += 1

    print("Lifetime likes: " + str(numLikes))
    print("Lifetime retweets: " + str(numRetweets))
    print("Lifetime comments: " + str(numReplies))

    num = len(replies)

    ti = TwitterInfluence()

    ti.insert_user(str(tweet.user.screen_name), str(tweet.user.name))
    ti.insert_tweet(url, tweet.created_at, tweet.favorite_count, tweet.user.location, tweet.user.screen_name, num)
    ti.insert_posts(tweet.user.screen_name, str(url), str(tweet.user.name))

    # Insert reply tweets to post table

    for usr in replies:
        # print("posts for loop")
        post_url = usr.id_str.split('/')[-1]
        ti.insert_user(api.get_user(usr.user.id_str).screen_name, usr.user.name)
        ti.insert_posts(api.get_user(usr.user.id_str).screen_name, str(post_url), usr.user.name)

    # Insert retweeters into retweet table
    retweeters_list = api.retweeters(url)
    for usr in retweeters_list:
        # print("retweeters loop")
        print(api.get_user(usr).screen_name)
        nm = api.get_user(usr).screen_name
        ti.insert_user(api.get_user(usr).screen_name, api.get_user(usr).user.name)
        ti.insert_retweet(url, tweet.created_at, tweet.favorite_count, tweet.user.location, nm, len(replies))
        ti.insert_repost(url)
        ti.insert_isa(url, url, nm)

    print("Did a specific user reply to this tweet?")
    tw_username = input("Enter specific twitter username: ")

    ti.did_user_reply(url, tw_username)

    print("end")
