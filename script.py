import tweepy, requests
from bs4 import BeautifulSoup

consumer_key = "0ychK8sOKKBMF07kDGK8f7hhM"
consumer_secret = "bWuCj0TyraJySFx8NLJ2WUV1hr0slK0OblZ1iJMZzDSmpLPYgI"
access_key = "859114956138192896-jYQO9zeobtLoSdVrqVbjPyFhwjxUEhC"
access_secret = "Sfu3Dm2M9JYZSBQuY9Rz7kP2aMsp468KgQXzTr2OZP4Av"


def share_tweet():
    #tweetcount = input('How many tweets do you want to post ? ')
    try:
        #tweetcount = int(tweetcount)
        tweetcount = 1
    except:
         print("This is not an integer !")
         exit
    tweetcountup = 0

    website = "https://islamvibe.herokuapp.com"
    website = website.strip()
    res = requests.get(website)
    result = res.content
    soup = BeautifulSoup(result, 'html.parser')
    first_link = soup.find('h3').text
    tweet = first_link
    #for a in first_link:
    print(tweet)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    print('logged into twitter')
    try:
        api.update_status(tweet)
    except tweepy.error.TweepError:
        api.update_status(tweet)
    print('Tweets posted!')



def main():
    share_tweet()

if __name__ == '__main__':
    main()
