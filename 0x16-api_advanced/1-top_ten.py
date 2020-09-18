#!/usr/bin/python3
""" Reddit method request module
"""
import requests
api_url = "https://api.reddit.com"
agent = {"User-Agent": "Holby Redditor"}


def top_ten(subreddit):
    """ Get the top 10 hot posts
    """

    subre_data = requests.get("{}/r/{}/hot.json?limit=10"
                              .format(api_url, subreddit),
                              headers=agent,
                              allow_redirects=False)
    if subre_data.status_code == 200:
        children = subre_data.json().get('data').get('children')
        for thread in children:
            print(ascii(thread.get('data').get('title')))
    else:
        print('None')
