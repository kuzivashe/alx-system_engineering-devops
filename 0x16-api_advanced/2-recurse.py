#!/usr/bin/python3
""" playing with reddit API
"""


def recurse(subreddit, hot_list=[], next=None, count=0):
    """ function that calls the reddit api in order to get
    the top 10 in a specific topic
    """
    import requests

    if count == 0:
        API = 'https://www.reddit.com/'
        r = requests.get('{}/r/{}/hot.json'.format(API, subreddit),
                         headers={'user-agent': 'Custom user'},
                         allow_redirects=False)
    else:
        API = 'https://www.reddit.com/'
        r = requests.get('{}/r/{}/hot.json'.format(API, subreddit),
                         headers={'user-agent': 'Custom user'},
                         params={'after': next},
                         allow_redirects=False)

    if r.status_code != 200:
        return(None)

    r = r.json()

    next = r.get('data').get('after')
    hot = r.get('data').get('children')
    new = list(map(lambda x: x.get('data').get('title'), hot))
    if next:
        result = recurse(subreddit, hot_list, next, count + 1)
    else:
        return (new)
    hot_list = new + result
    return(hot_list)
