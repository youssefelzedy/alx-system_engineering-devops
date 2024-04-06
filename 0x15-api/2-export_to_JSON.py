#!/usr/bin/python3

"""Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress."""

import csv
import json
from requests import get
from sys import argv


if __name__ == "__main__":

    res1 = get('https://jsonplaceholder.typicode.com/todos/')
    json_data1 = res1.json()
    usr_id = int(argv[1])

    res2 = get('https://jsonplaceholder.typicode.com/users')
    json_data2 = res2.json()
    name = [res for res in json_data2 if res["id"] == usr_id]
    name = name[0]["name"]

    todo_data_filtered_before = [
        res for res in json_data1 if res["userId"] == usr_id]

    row = []

    for i in todo_data_filtered_before:

        new_dict = {}

        if i["userId"] == usr_id:
            new_dict["task"] = i["title"]
            new_dict["completed"] = i["completed"]
            new_dict["username"] = name
            row.append(new_dict)

    final_dict = {}
    final_dict[usr_id] = row
    print(final_dict)

    json_obj = json.dumps(final_dict)

    with open(f"{usr_id}.json", "w") as file:
        file.write(json_obj)
