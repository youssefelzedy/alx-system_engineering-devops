#!/usr/bin/python3
""" How many subs? """
import json
import requests
import sys


def top_ten(subreddit):
    """return top 10 posts of a subreddit"""
    list = []
    try:
        response = requests.get('https://www.reddit.com/r/{}/top.json?limit=10'
                                .format(subreddit),
                                headers={'User-agent': 'Mozilla/5.0'},
                                allow_redirects=False)
    except requests.exceptions.RequestException:
        return 0
    try:
        data = response.json().get('data').get('children')
        for i in data:
            title = i.get('data').get('title')
            list.append(title)
    except (json.decoder.JSONDecodeError, AttributeError):
        return 0
    for i in list:
        print(i)
