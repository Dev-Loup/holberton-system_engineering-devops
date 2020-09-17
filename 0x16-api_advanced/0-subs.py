#!/usr/bin/python3
""" Reddit method request module
"""
import requests
api_url = "https://api.reddit.com"
agent = {"User-Agent": "Holby Redditor"}


def number_of_subscribers(subreddit):
    """ Get number of active subscribers
    """

    subre_data = requests.get("{}/r/{}/about".format(api_url, subreddit),
                              headers=agent,
                              allow_redirects=False)
    if subre_data is not None:
        data = subre_data.json().get('data')
    if data is not None:
        subs = data.get('subscribers')
    else:
        subs = 0
    return subs
