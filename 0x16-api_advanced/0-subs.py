#!/usr/bin/python3
"""
    Get number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """
        Returns number of subscribers for given subredit
        Args:
            subreddit: Account to search
    """
    userAgent = 'Python.wsl2.windows.ApiProject:v1 (by Dry-Improvement-3814)'

    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)

    _headers = {'User-Agent': userAgent}

    with requests.get(url, headers=_headers) as response:
        subscribers = response.json().get('data', {}).get("subscribers", 0)
        return subscribers
