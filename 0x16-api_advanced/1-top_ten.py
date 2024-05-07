#!/usr/bin/python3
"""
    List the top 10 hot posts
"""


import requests


def top_ten(subreddit):
    """
        returns a list of the top 10 hot posts in
        a given subreddit
        Args:
        subreddit: Account to search
    """
    userAgent = 'Python.wsl2.windows.ApiProject:v1 (by Dry-Improvement-3814)'

    if subreddit is None or type(subreddit) is not str:
        print(None)

    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)

    _headers = {
        'User-Agent': userAgent
    }

    _params = {
        'limit': 10
    }

    with requests.get(url, headers=_headers, params=_params) as response:
        titles = response.json()
        if response.status_code == 200:
            ch = titles.get('data').get('children')
            if ch is None or (len(ch) > 0 and ch[0].get('kind') != 't3'):
                print('None')
            else:
                for c in ch:
                    print(c.get('data').get('title'))
        else:
            print('None')
