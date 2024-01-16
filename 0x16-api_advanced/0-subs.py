#!/usr/bin/python3
"""
0-subs
"""

def number_of_subscribers(subreddit):
    """this function calls the reddit api to get the number of subscribers
    in a specific topic"""

    import requests

    # Reddit API:
    # Modhash API is a token required by reddit API to help prevent CSRF
    # /api/me.json call or response is where the modhashes is obtained 
    # for data of listing endpoints
    API = 'https://www.reddit.com/'
    req = requests.get('{}/r/{}/about.json'.format(API, subreddit),
                       headers={'user-agent': 'Custom user'},
                       allow_redirects=False)
    
    # incase there is an invalid subreddit
    if req.status_code != 200:
        return(0)
    
    # if successful
    req = req.json()
    result = req.get('data').get('subscribers')
    if result:
        return(result)
    # incase there are no subscribers
    return(0)
