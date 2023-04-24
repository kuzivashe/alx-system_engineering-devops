#!/usr/bin/python3
"""
get all task per id using this API
https://jsonplaceholder.typicode.com/
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    # getting all the information
    API_USER = "https://jsonplaceholder.typicode.com/users"
    r1 = requests.get(API_USER)
    r1 = r1.json()
    API_TODOS = "https://jsonplaceholder.typicode.com/todos"
    r2 = requests.get(API_TODOS)
    r2 = r2.json()

    # save all info in dic
    dic = {}
    for user in r1:
        tasks = []
        for elem in r2:
            if (user.get("id") == elem.get("userId")):
                tasks.append(elem)
        keys_remove = ["id", "userId", "title"]
        # remove the keys inside the dictionaries
        for elem in tasks:
            elem["task"] = elem["title"]
            for k in keys_remove:
                del elem[k]
            elem["username"] = user.get("username")
        # save the list configured in the dic
        dic["{}".format(user.get("id"))] = tasks

    # dictionary to turn into json
    with open('todo_all_employees.json', 'w') as fd:
        fd.write(json.dumps(dic))
