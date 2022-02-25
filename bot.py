import tweepy
import time

FILE_NAME = "last_seen.txt"

consumer_key = "PqXTmSdWPLlFh8wnHwvMbjIAT"
consumer_secret = "jOk79eBZJstDt9MyDNk9ADxY2iTULqB4ltADH3JbHe3KehQkMi"
access_token = "1489285280213446664-DBt2ZNSvUFZTuNOlNzu2rN8n5S6MfO"
access_token_secret = "0ZwjK8sAc7WtlLlML6v1BQfzXypud0jFJjEW1Zf6iMJAg"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# api.update_status('Twitter reporting in live')

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return True

# print(tweets[0].text) # Most recent mentionned text tweet

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended') # return all the mensions 
    for tweet in reversed(tweets):
        if '#ultimatebot' in tweet.full_text.lower(): # verify if an hashtag is present(lower or uppercase)
            print(str(tweet.id) + ' - ' + tweet.full_text) 
            api.update_status("@" + tweet.user.screen_name + " Auto reply, like and retweet works", tweet.id) #reply to tweets 
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)