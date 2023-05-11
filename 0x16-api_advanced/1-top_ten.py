#!/usr/bin/python3
""" playing with reddit API
"""


def top_ten(subreddit):
    """ function that calls the reddit api in order to get
    the top 10 in a specific topic
    """
    import requests
    # the API of reddit has:
    # A modhash is a token that the reddit API requires to help prevent CSRF.
    # Modhashes can be obtained via the /api/me.json call or in response
    # data of listing endpoints.

    # add param limit 10 to get the top 10
    API = 'https://www.reddit.com/'
    r = requests.get('{}/r/{}/hot.json'.format(API, subreddit),
                     headers={'user-agent': 'Custom user'},
                     params={'limit': 10},
                     allow_redirects=False)

    # if an invalid subreddit get in
    if r.status_code != 200:
        print(None)
        return(None)

    # if it passes
    r = r.json()
    # we get the hot posts
    hot = r.get('data').get('children')
    # for each element in hot we have to get the title
    # so here is necesary to get data again in order to get the title
    for elem in hot:
        print(elem.get('data').get('title'))
