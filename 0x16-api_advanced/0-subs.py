#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers for a given subreddit'''
    urls = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        'User-Agent': 'My User Agent 1.0'
    }

    result_req = requests.get(urls, headers=header, allow_redirects=False)
    return result_req.get("data", {}).get("subscribers", 0)
