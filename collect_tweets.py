# Inspired from this: https://www.data-blogger.com/2017/02/24/gathering-tweets-with-python/


import tweepy
import json

# Specify the account credentials in the following variables:
# TODO: Get them from an env varibale or secret file
consumer_key = 'INSERT CONSUMER KEY HERE'
consumer_secret = 'INSERT CONSUMER SECRET HERE'
access_token = 'INSERT ACCESS TOKEN HERE'
access_token_secret = 'INSERT ACCESS TOKEN SECRET HERE'


# This listener will print out all Tweets it receives
# TODO: Adapt this to write to a CSV or something else.
class PrintListener(tweepy.StreamListener):

    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Python'])
