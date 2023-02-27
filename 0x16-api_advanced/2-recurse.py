#!/usr/bin/python3
""" A module that queries the REDDIT API and returns
 list of all subreddit posts titles"""
import requests


def recurse(subreddit, hot_list=[], count=0, payload={}):
    """recursive function returning all subreddit posts titles as a list"""
    headers = {'User-agent': 'kirimiBot/0.0.1'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    r = requests.get(url, headers=headers, params=payload,
                     allow_redirects=False)
    full_data = r.json()
    data = full_data.get('data')
    if data:
        after = data.get('after')
        children = data.get('children')
        if children:
            count = len(children)
            for child in children:
                child_data = child.get('data')
                if child_data:
                    hot_list.append(child_data.get('title'))
            if after is not None:
                payload['after'] = after
                hot_list = recurse(subreddit, hot_list, count, payload)
            else:
                return hot_list
    else:
        return None
    return hot_list
