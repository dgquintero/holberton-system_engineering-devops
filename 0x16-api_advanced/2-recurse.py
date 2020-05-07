#!/usr/bin/python3
''' recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    ''' Function that queries the Reddit API'''
    if after is None:
        return []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    if after:
        url += '?after={}'.format(after)
    req = requests.get(url, headers=headers, allow_redirects=False)
    if str(req) != '<Response [200]>':
        return(None)
    RJson = req.json()
    HotPosts = RJson.get('data').get('children')
    for post in HotPosts:
        hot_list.append(post.get('data').get('title'))
    return hot_list + recurse(subreddit, [], RJson.get('data').get('after'))
