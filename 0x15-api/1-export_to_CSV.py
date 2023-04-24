#!/usr/bin/python3
"""
get all task per id using this API
https://jsonplaceholder.typicode.com/
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys
    API_USER = "https://jsonplaceholder.typicode.com/users"
    r1 = requests.get("{}/{}".format(API_USER, sys.argv[1]))

    # getting the name of the user with specific id
    username = r1.json().get("username")
    API_TODOS = "https://jsonplaceholder.typicode.com/todos"
    r2 = requests.get(API_TODOS)
    r2 = r2.json()

    # getting the tasks of an specific user
    tasks = []
    for elem in r2:
        user_id = elem.get("userId")
        if (user_id == int(sys.argv[1])):
            tasks.append(elem)

    # save in csv file with double quotes
    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as csvfile:
        fieldnames = ['user_id', 'username', 'status', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                delimiter=',', quoting=csv.QUOTE_ALL)
        for elem in tasks:
            writer.writerow({'user_id': sys.argv[1], 'username': username,
                             'status': elem.get("completed"),
                             'title': elem.get("title")})
