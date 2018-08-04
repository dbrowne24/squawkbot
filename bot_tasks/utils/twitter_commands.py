
import tweepy
import json
from time import sleep


class TwitterAPI():
    def __init(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

        # authenticate with twitter and get the api
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth)

    def get_friends():
        """
        returns a list of your followers, followings and whitelisted users
        """
        followers = self.api.followers_ids(self.screen_name)
        following = self.api.friends_ids(self.screen_name)
        total_followed = 0

        # TODO -> We have not added whitelisted users or blacklisted users here

        return followers, following, total_followed
