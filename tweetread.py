import tweepy
#pip3 install tweepy --package to install 
# Set up your Twitter API credentials
#to get this ,create twitter developer account
consumer_key = 'GYQysYUxLJ3s4M7z5mmfP4bSR'
consumer_secret = 'fmstUySOCBa4ydf0FevabAo0IirSw5cuvwU9Wauor29pq4kJf3'
access_token = '1737370553097613312-sqFASvybIGmuDL1RrHdt8fS4Y0Dp17'
access_token_secret = '7yFVtfLkk0PRExemVYgy4vomDddiWsGgyqDkcxEYbvOd1'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Screen name of the user whose tweets you want to read
screen_name = 'username'

# Number of tweets to retrieve
tweet_count = 10

# Retrieve tweets
tweets = api.user_timeline(screen_name=screen_name, count=tweet_count)

# Display the tweets
for tweet in tweets:
    print(tweet.text)
    print("-------------")

