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
    todo_data_filtered_after = [
        res for res in json_data1
        if res["userId"] == usr_id and res["completed"]]

    csv_file = f"{usr_id}.csv"

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for item in todo_data_filtered_before:
            row_data = [item["userId"], name, item["completed"], item["title"]]
            writer.writerow(row_data)
