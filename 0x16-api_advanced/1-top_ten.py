#!/usr/bin/python3
"""
1-top_ten
"""

def top_ten(subreddit):
    """ this function calls the reddit api to get
    the top 10 in a specific topic
    """
    import requests
    # Reddit API:
    # Modhash API is a token required by reddit API to help prevent CSRF
    # /api/me.json call or response is where the modhashes is obtained 
    # for data of listing endpoints

    API = 'https://www.reddit.com/'
    req = requests.get('{}/req/{}/hot.json'.format(API, subreddit),
                       headers={'user-agent': 'Customer user'},
                       params={'limit': 10},
                       allow_redirects=False)
    
    # incase there is an invalid subreddit
    if req.status_code != 200:
        print(None)
        return(None)
    
    # if successful
    req = req.json()
    # using the hot posts
    hot = req.get('data').get('children')
    # for each element in hot we have to get the title
    # so here is necesary to get data again in order to get the title
    for elem in hot:
        print(elem.get('data').get('title'))