#!/usr/bin/python3
"""
This module contans the number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    user_agent = {"User-Agent": "Python"}
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return (response.json().get("data").get("subscribers"))
