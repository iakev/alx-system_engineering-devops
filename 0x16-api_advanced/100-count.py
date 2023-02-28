#!/usr/bin/python3
""" A module that queries the REDDIT API prses
 all subreddit posts titles and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, hot_list=[],
                count=0, payload={}, recurse_done=False):
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
                hot_list, recurse_done = count_words(subreddit, word_list,
                                                     hot_list, count,
                                                     payload, recurse_done)
            else:
                recurse_done = True
                return hot_list, recurse_done
    else:
        return None
    # after getting all hot posts in hot_list then now parse and compute count
    if recurse_done:
        word_count = {}
        for key in word_list:
            word_count[key] = 0
        for title in hot_list:
            title_list = title.split()
            for key in word_list:
                for word in title_list:
                    if key.lower() == word.lower():
                        word_count[key] += 1
                        sorted_count = dict(sorted(word_count.items(),
                                                   key=lambda item: item[0]))
        for k, v in sorted_count.items():
            if v != 0:
                print("{}: {}".format(k, v))
    return hot_list, False
