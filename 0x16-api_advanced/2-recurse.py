#!/usr/bin/python3
"""
2-recurse
"""

def recurse(subreddit, hot_list=[], next=None, count=0):
    """ 
    this function calls the reddit api to get
    the top 10 in a specific topic
    """
    import requests

    if count == 0:
        API = 'https://www.reddit.com/'
        req = requests.get('{}/r/{}/hot.json'.format(API, subreddit),
                           headers={'user-agent': 'Custom user'},
                           allow_redirects=False)
        
    else:
        API = 'https://www.reddit.com/'
        req = requests.get('{}/r/{}/hot.json'.format(API, subreddit),
                           headers={'user-agent': 'Custom user'},
                           params={'after': next},
                           allow_redirects=False)
        
    if req.status_code != 200:
        return(None)
    
    req = req.json()

    next = req.get('data').get('after')
    hot = req.get('data').get('children')
    new = list(map(lambda x: x.get('data').get('title'), hot))
    if next:
        result = recurse(subreddit, hot_list, next, count + 1)
    else:
        return (new)
    hot_list = new + result
    return(hot_list)