#!/usr/bin/python3
"""
playing with reddit API
"""

import requests


def hot_print(response, word_list, param, hot_dict):
    """
    print number of times the hot word is repeated
    and fill the hot_dict dictionary with that values
    """
    hots = response.json().get("data").get("children")
    for hot in hots:
        for hot_word in word_list:
            title = hot.get("data").get("title")
            if title is not None:
                words = title.split()
                for word in words:
                    if hot_word.lower() == word.lower():
                        hot_dict[hot_word] += 1

    if param is None:
        lista = sorted(hot_dict.items(), key=lambda x: x[1])
        lista.reverse()
        # print(lista)
        for key, value in lista:
            if value != 0:
                print("{}: {}".format(key, value))


def count_words(subreddit, word_list, param1=None, hot_dict={}):
    """
    counts words from reddits API
    """
    url = "https://www.reddit.com"
    resp = requests.get("{}/r/{}/hot.json".format(url, subreddit),
                        headers={'User-Agent': 'Custom user'},
                        params={'after': param1})

    if len(hot_dict) == 0:
        for elem in word_list:
            hot_dict[elem] = 0

    if resp:
        next_r = resp.json().get("data").get("after")
        if next_r:
            count_words(subreddit, word_list,
                        param1=next_r,
                        hot_dict=hot_dict)

            hot_print(resp, word_list, param1, hot_dict)
            return hot_dict

        else:
            hot_print(resp, word_list, param1, hot_dict)
            return hot_dict
    else:
        return None
