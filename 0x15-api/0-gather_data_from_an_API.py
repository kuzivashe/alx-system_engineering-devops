#!/usr/bin/python3
"""
get all task per id using this API
https://jsonplaceholder.typicode.com/
"""
if __name__ == "__main__":
    import requests
    import sys
    API_USER = "https://jsonplaceholder.typicode.com/users"
    r1 = requests.get("{}/{}".format(API_USER, sys.argv[1]))

    # getting the name of the user with specific id
    name = r1.json().get("name")
    API_TODOS = "https://jsonplaceholder.typicode.com/todos"
    r2 = requests.get(API_TODOS)
    r2 = r2.json()

    # getting the tasks of an specific user
    tasks = []
    for elem in r2:
        user_id = elem.get("userId")
        if (user_id == int(sys.argv[1])):
            tasks.append(elem)

    # total tasks number
    total = len(tasks)

    # done tasks list and number of done tasks
    done_tasks = []
    for elem in tasks:
        state = elem.get("completed")
        if (state):
            done_tasks.append(elem)
    done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for elem in done_tasks:
        print("\t {}".format(elem.get("title")))
