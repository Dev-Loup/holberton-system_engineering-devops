#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list."""
import requests
api_url = "https://api.reddit.com"
agent = {"User-Agent": "Holby Redditor"}


def count_words(subreddit, word_list, hot_list=[], after=''):
    """Parses the title of all hot articles, and prints it sorted.
    """

    subre_data = requests.get('{}/r/{}/hot.json?after={}'
                              .format(api_url, subreddit, after),
                              headers={'User-Agent': 'custom'},
                              allow_redirects=False)
    if subre_data.status_code == 200:
        if after is None:
            summary = {}
            for word in word_list:
                for hot_word in hot_list:
                    if word == hot_word:
                        if word not in summary:
                            summary[word] = 1
                        else:
                            summary[word] += 1
            for word in sorted(summary, key=summary.get, reverse=True):
                if summary[word]:
                    print('{}: {}'.format(word, summary[word]))
            return hot_list
        for thread in resp.json().get('data').get('children'):
            hot_list += thread.get('data').get('title').lower().split()
        after = resp.json().get('data').get('after')
        count_words(subreddit, word_list, hot_list, after)
        return hot_list
    else:
        return None
