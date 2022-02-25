import tweepy
import time


consumer_key = "PqXTmSdWPLlFh8wnHwvMbjIAT"
consumer_secret = "jOk79eBZJstDt9MyDNk9ADxY2iTULqB4ltADH3JbHe3KehQkMi"
access_token = "1489285280213446664-DBt2ZNSvUFZTuNOlNzu2rN8n5S6MfO"
access_token_secret = "0ZwjK8sAc7WtlLlML6v1BQfzXypud0jFJjEW1Zf6iMJAg"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# api.update_status('Twitter reporting in live')


