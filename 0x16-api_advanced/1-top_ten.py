#!/usr/bin/python3
""" A module that queries the REDDIT API and prints
 10 hot posts from a subreddit"""
import requests


def top_ten(subreddit):
    """function to print top ten posts in a subreddit"""
    headers = {'User-agent': 'kirimiBot/0.0.1'}
    payload = {'limit': '10'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    r = requests.get(url, headers=headers, params=payload,
                     allow_redirects=False)
    full_data = r.json()
    data = full_data.get('data')
    if data:
        children = data.get('children')
        if children:
            for child in children:
                child_data = child.get('data')
                if child_data:
                    print(child_data.get('title'))
        else:
            print(children)
    else:
        print(data)
