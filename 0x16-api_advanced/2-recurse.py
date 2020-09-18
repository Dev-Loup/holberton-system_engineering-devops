#!/usr/bin/python3
""" Reddit method request module
"""
import requests
api_url = "https://api.reddit.com"
agent = {"User-Agent": "Holby Redditor"}


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all hot articles."""
    subre_data = requests.get('{}/r/{}/hot.json?after={}'
                              .format(api_url, subreddit, after),
                              headers=agent,
                              allow_redirects=False)
    if subre_data.status_code == 200:
        if after is None:
            return hot_list
        for post in subre_data.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        after = subre_data.json().get('data').get('after')
        recurse(subreddit, hot_list, after)
        return hot_list
