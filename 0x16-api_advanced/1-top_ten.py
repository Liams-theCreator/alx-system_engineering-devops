#!/usr/bin/python3
"""
This module contains the top_ten function
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    limit = "10"

    url = "https://www.reddit.com/r/{}/hot.json?limit={}".format(subreddit,
                                                                 limit)

    user_agent = {"User-Agent": "Python"}
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code >= 300:
        print("None")
    else:
        for elem in response.json().get("data").get("children"):
            print(elem.get("data").get("title"))
