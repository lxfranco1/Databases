import MySQLdb
import tweepy as tw

class TwitterInfluence(object):
    def __init__(self):
        self.dbConn = MySQLdb.connect(host='localhost', user='twitter_project', passwd='tw33t!123')
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('use twitterinfluence')

    def insert_user(self, username, name):
        # print("insert user")
          # Query for existing entry
        sql_select = "SELECT * FROM user WHERE username = %s"
        self.dbCursor.execute(str(sql_select), (str(username),))
        record = self.dbCursor.fetchall()

        if len(record) == 0:
            sql = "INSERT INTO user (username, name) VALUES (%s, %s)"
            vals = (username, name)

            self.dbCursor.execute(sql, vals)
            self.dbConn.commit()

    def insert_tweet( self, url, date, likes, location, username, replies):
        # print("insert tweet")
          # Query for existing entry
        sql_select = "SELECT * FROM tweet WHERE oc_url = %s"
        self.dbCursor.execute(sql_select, (url,))
        record = self.dbCursor.fetchall()

        if len(record) == 0:
            sql = "INSERT INTO tweet (oc_url, oc_date, oc_likes, oc_location,oc_username, oc_replies) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
            vals = (url, date, likes, location, username, replies)

            self.dbCursor.execute(sql, vals)

            self.dbConn.commit()

    def insert_retweet(self, url, date, likes, location, username, replies):
        # print("insert retweet")
          # Query for existing entry
        sql_select = "SELECT * FROM retweet WHERE re_url = %s"
        self.dbCursor.execute(sql_select, (str(url),))
        record = self.dbCursor.fetchall()

        if len(record) == 0:
            sql = "INSERT INTO retweet (re_url, re_date, re_likes, re_location, re_username, re_replies) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            vals = (url, date, likes, location, username, replies)
            self.dbCursor.execute(sql, vals)

            self.dbConn.commit()

    def insert_isa(self, re_url, oc_url, username):
        # print("insert isa")
          # Query for existing entry
        sql_select = "SELECT * FROM isa WHERE isa_oc_url = %s AND isa_username = %s"
        vals = (str(oc_url), (str(username),))
        self.dbCursor.execute(sql_select, vals)
        record = self.dbCursor.fetchall()

        if len(record) == 0:
            sql = "INSERT INTO isa (isa_oc_url, isa_re_url, isa_username) VALUES (%s, %s, %s)"
            vals = (oc_url, re_url, username)

            self.dbCursor.execute(sql, vals)

            self.dbConn.commit()

    def insert_posts(self, username, url, name):
        # print("insert posts")
          # Query for existing entry
        sql_select = "SELECT * FROM posts WHERE posts_oc_url = %s AND posts_username = %s"
        vals = (str(url), str(username),)
        self.dbCursor.execute(sql_select, vals)
        record = self.dbCursor.fetchall()

        if len(record)==0:
            sql_select = "SELECT * FROM user WHERE username = %s"
            self.dbCursor.execute(sql_select, (username,))
            record = self.dbCursor.fetchall()

            if len(record)==0:
                self.insert_user(username, name)
            sql = "INSERT INTO posts (posts_oc_url, posts_username) VALUES (%s, %s)"
            vals = (str(url), str(username),)

            self.dbCursor.execute(sql, vals)

        self.dbConn.commit()

    def insert_repost(self, url):
        # print ("insert repost")
        # Query for existing entry
        sql_select = "SELECT * FROM posts WHERE posts_oc_url = %s AND posts_username = %s"

        self.dbCursor.execute(sql_select, (str(url),))
        record = self.dbCursor.fetchall()

        if len(record) == 0:
            sql = "INSERT INTO repost (repost_re_url) VALUES (%s)"
            val = url

            self.dbCursor.execute(sql, val)

            self.dbConn.commit()

    def did_user_reply(self, url, username):
        # print("advanced query")
        # Query to check if a specific user replied to a tweet 
        # Gets the answer from the intersection from the two tables
        # Tweet will contain the url of the original tweet so you have to intersect the two tables
        # Posts table has the url of the reply
        sql_select = "SELECT posts_username FROM posts WHERE posts_username = %s INTERSECT " \
                     "SELECT oc_username WHERE tweet.url = %s"
        vals = (str(username), str(url),)
        self.dbCursor.execute(sql_select, vals)
        record = self.dbCursor.fetchall()
        
        # If the record is not empty then the user replied to the tweet
        if len(record) != 0:
            print "yes"

        else:
            print "no"
