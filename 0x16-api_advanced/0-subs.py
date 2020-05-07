#!/usr/bin/python3
''' Python script that fetches http://www.reddit.com/
'''
import requests

def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                 Chrome/70.0.3538.77 Safari/537.36"}
    req = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                        headers=headers).json()
    countsubr = req.get("data", {}).get("subscribers", 0)
    return countsubr
