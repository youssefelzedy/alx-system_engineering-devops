#!/usr/bin/python3

"""Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress."""

import urllib
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    completed = [task for task in todos if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t " + task.get("title")) for task in completed]
