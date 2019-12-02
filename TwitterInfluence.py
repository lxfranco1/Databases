import MySQLdb
import tweepy as tw

class TwitterInfluence:
    def __init__(self, url):
        self.dbConn = MySQLdb.connect(host='localhost', user='twitter_project', passwd='tw33t!123')
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('use twitterinfluence')

    def insert_into_database( self, url ):
        print("insert")
        # dbConn = MySQLdb.connect(host='localhost', user='twitter_project', passwd='tw33t!123')
        # dbCursor = dbConn.cursor()

#dbCursor.execute('create database twitterinfluence')
        # dbCursor.execute('use twitterinfluence')

#Create tables
# user_table = 'create table user(username char(15) primary key, name char(50))'
# dbCursor.execute(user_table)

# tweet_table = 'create table tweet(oc_url char(1000) primary key, oc_date DATE, oc_likes int(15), oc_location char(50)'
# dbCursor.execute(tweet_table)
#
# retweet_table = 'create table retweet(re_url char(1000) primary key, re_date DATE, re_likes int(15), re_location char(50)'
# dbCursor.execute(retweet_table)

