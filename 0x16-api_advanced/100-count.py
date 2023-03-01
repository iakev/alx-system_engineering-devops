#!/usr/bin/python3
""" A module that queries the REDDIT API prses
 all subreddit posts titles and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list,
                count=0, payload={}, word_count={}, recurse_done=False):
    """recursive function returning all subreddit posts titles as a list"""
    if word_count == {}:
        for key_word in word_list:
            word_count[key_word.lower()] = 0
    headers = {'User-agent': 'kirimiBot/0.0.1'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    r = requests.get(url, headers=headers, params=payload,
                     allow_redirects=False)
    if r.status_code == 200:
        try:
            full_data = r.json()
        except Exception as e:
            return
        data = full_data.get('data')
        if data:
            after = data.get('after')
            children = data.get('children')
            if children:
                count = len(children)
                for child in children:
                    child_data = child.get('data')
                    if child_data:
                        title = child_data.get('title')
                        title_list = title.split()
                        for key_word in word_list:
                            for word in title_list:
                                if key_word.lower() == word.lower():
                                    word_count[key_word.lower()] += 1
                if after is not None:
                    payload['after'] = after
                    word_count, recurse_done = count_words(subreddit, word_list,
                                                       count, payload,
                                                       word_count,
                                                       recurse_done)
                else:
                    return word_count, True
        else:
            return None
        if recurse_done:
            sorted_count = dict(sorted(word_count.items(),
                                       key=lambda item: item[0]))
            for k, v in sorted_count.items():
                if v > 0:
                    print("{}: {}".format(k, v))
        return word_count, False
