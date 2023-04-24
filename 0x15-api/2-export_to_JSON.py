#!/usr/bin/python3
"""
get all task per id using this API
https://jsonplaceholder.typicode.com/
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    API_USER = "https://jsonplaceholder.typicode.com/users"
    r1 = requests.get("{}/{}".format(API_USER, sys.argv[1]))

    # getting the name and username of the user with specific id
    username = r1.json().get("username")
    # another form to get the task of an specific user
    API_TODOS = "https://jsonplaceholder.typicode.com/todos"
    r2 = requests.get("{}?userId={}".format(API_TODOS, sys.argv[1]))
    r2 = r2.json()
    keys_remove = ["id", "userId", "title"]
    # remove the keys inside the dictionaries
    for elem in r2:
        elem["task"] = elem["title"]
        for k in keys_remove:
            del elem[k]
        elem["username"] = username
    # dictionary to turn into json
    dic = {}
    dic["{}".format(sys.argv[1])] = r2
    with open('{}.json'.format(sys.argv[1]), 'w') as fd:
        fd.write(json.dumps(dic))
