#!/usr/bin/python3

"""Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress."""

from json import load
import requests
from sys import argv


if __name__ == "__main__":

    def make_request(resource, param=None):
        """Retrieve user from API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        r = requests.get(url)

        r = r.json()
        return r

    user = make_request('users', ('id', argv[1]))
    tasks = make_request('todos', ('userId', argv[1]))
    tasks_completed = [task for task in tasks if task['completed']]

    print("Employee {} is done with tasks({}/{}):".format(
        user[0]['name'], len(tasks_completed), len(tasks)))
    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
