#!/usr/bin/python3
""" playing with reddit API
"""


def number_of_subscribers(subreddit):
    """ function that calls the reddit api in order to get
    the number of subcribers  in a specific topic
    """
    import requests
    # the API of reddit has:
    # A modhash is a token that the reddit API requires to help prevent CSRF.
    # Modhashes can be obtained via the /api/me.json call or in response
    # data of listing endpoints.
    API = 'https://www.reddit.com/'
    r = requests.get('{}/r/{}/about.json'.format(API, subreddit),
                     headers={'user-agent': 'Custom user'},
                     allow_redirects=False)

    # if an invalid subreddit get in
    if r.status_code != 200:
        return(0)

    # if it passes
    r = r.json()
    # get information with data key
    result = r.get('data').get('subscribers')
    if result:
        return (result)
    # if there are no subscribers
    return (0)
