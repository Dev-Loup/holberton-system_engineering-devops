#!/usr/bin/python3
""" Reddit method request module
"""
import requests
api_url = "https://api.reddit.com"
agent = {"User-Agent": "Holby Redditor"}


def top_ten(subreddit):
    """ Get the top 10 hot posts
    """

    subre_data = requests.get("{}/r/{}/hot.json?limit=2&raw_json=1"
                              .format(api_url, subreddit),
                              headers=agent,
                              allow_redirects=False)
    if subre_data is not None:
        data = subre_data.json().get('data')
    if data is not None:
        children = data.get('children')
        for post in children:
            print(ascii(post.get('data').get('title')))
