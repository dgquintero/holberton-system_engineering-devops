#!/usr/bin/python3
''' Python script that fetches https://jsonplaceholder.typicode.com/posts/1
'''
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1', params={})
    print(r.headers.get("X-Request-Id"))
