import MySQLdb
import tweepy as tw

class TwitterInfluence(object):
    def __init__(self):
        self.dbConn = MySQLdb.connect(host='localhost', user='twitter_project', passwd='tw33t!123')
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('use twitterinfluence')

    def insert_user(self, username, name):
        print("insert user")
        sql = "INSERT INTO user (username, name) VALUES (%s, %s)"
        vals = (username, name)

        self.dbCursor.execute(sql, vals)
        self.dbConn.commit()

    def insert_tweet( self, url, date, likes, location, username, replies):
        print("insert tweet")
        sql = "INSERT INTO tweet (oc_url, oc_date, oc_likes, oc_location, oc_username, oc_replies) VALUES (%s, %s, %s, %s, %s, %s)"
        vals = (url, date, likes, location, username, replies)

        self.dbCursor.execute(sql, vals)

        self.dbConn.commit()

    def insert_retweet(self, url, date, likes, location, username, replies):
        print("insert retweet")
        sql = "INSERT INTO retweet (re_url, re_date, re_likes, re_location, re_username, re_replies) VALUES (%s, %s, %s, %s, %s, %s)"
        vals = (url, date, likes, location, username, replies)
        self.dbCursor.execute(sql, vals)

        self.dbConn.commit()

    def insert_isa(self, re_url, oc_url, username):
        print("insert isa")
        sql = "INSERT INTO isa (isa_oc_url, isa_re_url, isa_username) VALUES (%s, %s, %s)"
        vals = (oc_url, re_url, username)

        self.dbCursor.execute(sql, vals)

        self.dbConn.commit()

    def insert_posts(self, username, url):
        print("insert posts")

        sql = "INSERT INTO posts (posts_oc_url, posts_username) VALUES (%s, %s)"
        vals = (url, username)

        self.dbCursor.execute(sql, vals)

        self.dbConn.commit()

    def insert_repost(self, url):
        print ("insert repost")
        sql = "INSERT INTO repost (repost_re_url) VALUES (%s)"
        val = url

        self.dbCursor.execute(sql, val)

        self.dbConn.commit()
