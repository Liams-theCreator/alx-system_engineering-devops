#!/usr/bin/python3
"""
This module defines the recurse function
"""
import requests


def recurse(subreddit, hot_list=[], after=""):

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {"after": after, "limit": "100"}
    user_agent = {"User-Agent": "Python"}

    response = requests.get(url, headers=user_agent, params=param,
                            allow_redirects=False)

    if response.status_code >= 400:
        return None

    response = response.json()
    hot_posts = response.get("data").get("children")
    after = response.get("data").get("after")

    for post in hot_posts:
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
