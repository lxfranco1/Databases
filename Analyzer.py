import twitter
import tweepy

#api = twitter.Api(consumer_key='TEQxvBQ2BVUAt0OnoAMIA0yWh',
#                  consumer_secret='8YbxHRXnVTzKYPs8Qg4mzd7oD9DFAvbwDfVxdhmljeOlFuSP5j',
#                  access_token_key='2173222812-UpKnOtwJI2TEd29ubii368C9mzE0KZOYw2qUz4y ',
#                  access_token_secret='yGXhsuTrXJ3zJV5P4oizxGc7lq2CV5TlOZTChjR0ApWII')

consumer_key='TEQxvBQ2BVUAt0OnoAMIA0yWh'
consumer_secret='8YbxHRXnVTzKYPs8Qg4mzd7oD9DFAvbwDfVxdhmljeOlFuSP5j'
access_token='2173222812-UpKnOtwJI2TEd29ubii368C9mzE0KZOYw2qUz4y '
access_token_secret='yGXhsuTrXJ3zJV5P4oizxGc7lq2CV5TlOZTChjR0ApWII'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

