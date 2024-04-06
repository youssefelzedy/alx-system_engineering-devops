#!/usr/bin/python3

"""Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress."""

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
    todo_data_filtered_after = [
        res for res in json_data1
        if res["userId"] == usr_id and res["completed"]]
    
    print(f"Employee {name} is done with tasks("
          f"{len(todo_data_filtered_after)}/"
          f"{len(todo_data_filtered_before)}):")

    for i in todo_data_filtered_after:
        print("\t " + i["title"])