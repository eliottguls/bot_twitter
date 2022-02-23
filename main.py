
import tweepy
from tkinter import *

consumer_key = "8lwVIFTM02gAPUlPm7fGg93Z0"
consumer_secret = "EYg1x3oWdf13IZ1iEmBia4BxkuB3vFkBpOffyuP2i7UrnJnuyi"
access_token = "1489285280213446664-tM07F0m6QpYT4NiYBU7qEj2LxtPlkS"
access_token_secret = "Ku3PSwOmx2pfpoUxpfAUweVCNpAm5k5VqFdkrsZhoinlr"

# *** Step 1 - Credentials *** #
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# *** Step 2 - Building the bot *** #

# ****** Sep 2.1 - Follow everyone following you ****** #
def followback():
    for follower in tweepy.Cursor(api.get_followers).items():
        follower.follow()
        print(follower + "followed by " + user.name)

# ****** Step 2.2 - Favorite and retweet a Tweet based on keywords ****** #
search = "MOI"  # Keyword
numberOfTweets = 10  # Number of tweets we want to interact with

# RETWEET
def retweet():
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            print("Retweeted the tweet : " + tweet)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# LIKE
def like():
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.favorite()
            print("Liked the tweet : " + tweet)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


# REPLY
def reply():
    tweetId = tweet.user.id  # Store the users username
    username = tweet.user.screen_name  # Store the twitter ID
    reply = "Bot testing reply"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print('ID: @' + str(tweet.user.id))
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            print ("Replied with" + api.update_status("@" + username + " " + reply, in_reply_to_status_id = tweetId))
        except tweepy.TweepError as e:
            print (e.reason)
        except StopIteration:
            break

# *** Step 3 - Creating the GUI with tkinter *** #
root = Tk.Tk(screenName="Box")

# ****** Step 3.1 - Create button ****** #
label1 = Label( root, text="Search")
E1 = Entry(root, bd=5)
label2 = Label( root, text="Number of Tweets")
E2 = Entry(root, bd =5)
label3 = Label( root, text="Response")
E3 = Entry(root, bd =5)
label4 = Label( root, text="Reply?")
E4 = Entry(root, bd =5)
label5 = Label( root, text="Retweet?")
E5 = Entry(root, bd =5)
label6 = Label( root, text="Favorite?")
E6 = Entry(root, bd =5)
label7 = Label( root, text="Follow?")
E7 = Entry(root, bd =5)

# ****** Step 3.2 - Store the user input from GUI ****** #
def getE1():
    return E1.get()
def getE2():
    return E2.get()
def getE3():
    return E3.get()
def getE4():
    return E4.get()
def getE5():
    return E5.get()
def getE6():
    return E6.get()
def getE7():
    return E7.get()


def main():
    getE1()
    search = getE1()

    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets) # make sure to convert in integer

    if reply == "yes":
        reply()

    if retweet == "yes":
        retweet()

    if favorite == "yes":
        like()

    if follow == "yes":
        followback()
# ****** Step 3.3 - Button to submit our requests ****** #
submit = Button(root, text = "Execute", command=main)

# Pack each label (call the root function in a loop so that they
# remain on the screen
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()

root.mainloop()

