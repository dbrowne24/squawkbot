import tweepy
import json
from time import sleep

# Set the sleep time between actions
SLEEP_TIMEOUT = 30
RATE_LIMITING_TIMEOUT = (60 * 30)

class TwitterAPI():
    def __init__(self, twitter_handle, consumer_key, consumer_secret, access_token, access_secret):
        self.twitter_handle = twitter_handle
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

        # authenticate with twitter and get the api
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth)

        # get followers, following
        friends = self.get_friends()
        self.followers = friends['followers']
        self.following = friends['following']


    # TODO -> We have not added whitelisted users or blacklisted users here
    def get_friends(self):
        """
        returns a list of your followers, followings and whitelisted users
        """
        followers = self.api.followers_ids(self.twitter_handle)
        following = self.api.friends_ids(self.twitter_handle)
        total_followed = 0

        return {
            'followers': followers,
            'following': following,
            'total_followed': total_followed
        }


    def follow_all(self, target, limit=100):
        """
        Follows all the followers of another user
        """
        followers = self.followers
        following = self.following

        # The user whose followers that you want to follow
        their_followers = self.api.followers_ids(target)

        # Make a list of non mutual followings
        non_mutual_followers = set(their_followers) - set(following)

        # loop through the list and follow the users
        total_followed = 0
        for f in non_mutual_followers:
            if total_followed >= limit:
                print("[+] Reached the limit, stopped following")
                break
            try:
                self.api.create_friendship(f)
                total_followed += 1
                if total_followed % 10 == 0:
                    print('[+] '+ str(total_followed) + ' users followed so far')
                print('[+] Followed a user. Sleeping for %s seconds' % SLEEP_TIMEOUT)
                sleep(SLEEP_TIMEOUT)
            except(tweepy.RateLimitError, tweepy.TweepError) as e:
                error_handling(e)
        print(total_followed)


    def follow_keyword(self, keywords, limit, count=5):
        """
        Follows the limit number of users for each keyword passed in keywords
        """
        print('[+] limit set to: %s' % limit)
        print('[+] count set to: %s' % count)

        followers = self.followers
        following = self.following

        for keyword in keywords:
            # Get the search result
            search_results = self.api.search(
                q=keyword,
                count=count,
                lang='en'
            )
            # TODO We should remove a list of blacklisted users from the searched_screen_names
            searched_screen_names = [tweet.author._json['screen_name'] for tweet in search_results]
            # only follows limit of each keyword to avoid non-relevant users
            print('[+] Following users who tweeted: %s' % keyword)
            total_followed = 0
            for i in range(0, len(searched_screen_names) - 1):
                try:
                    # follow the user
                    self.api.create_friendship(searched_screen_names[i])
                    total_followed += 1
                    if total_followed % 10 == 0:
                        print(str(total_followed) + ' users followed so far')
                    print('[+] Followed a user. Sleeping %s seconds' % SLEEP_TIMEOUT)
                    sleep(SLEEP_TIMEOUT)
                except(tweepy.RateLimitError, tweepy.TweepError) as e:
                    error_handling(e)

            print('[+] Total followed: %s' % total_followed)


    def unfollow_back(self):
        """
        Unfollows users that don't follow you back
        """
        print("[+] Starting to unfollow users that don't follow you back")

        followers = self.followers
        following = self.following

        # create a list of users that don't follow you back
        non_mutual_followers = set(following) - set(followers)
        total_unfollowed = 0
        for f in non_mutual_followers:
            try:
                self.api.destroy_friendship(f)
                total_unfollowed += 1
                if total_unfollowed % 10 == 0:
                    print(str(total_unfollowed) + ' unfollowed so far')
                # sleep so we don't rate limit...
                print('[+] Unfollowed user. Sleeping for %s seconds' % SLEEP_TIMEOUT)
                sleep(SLEEP_TIMEOUT)
            except(tweepy.RateLimitError, tweepy.TweepError) as e:
                error_handling(e)
            print("[+] Total unfollowed: %s" % total_unfollowed)


def error_handling(e):
    """
    Handle all the error. I think that we should also be saving the error in the
    model somehow
    """
    error = type(e)
    if error == tweepy.RateLimitError:
        print("[+] You've hit a limit!! Sleeping for %s minutes" % RATE_LIMITING_TIMEOUT)
        sleep(RATE_LIMITING_TIMEOUT)
    if error == tweepy.TweepError:
        print('[+] Uh oh!. Could not complete that task. Sleeping for 10 seconds')
        sleep(10)
