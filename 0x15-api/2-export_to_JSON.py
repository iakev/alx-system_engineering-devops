#!/usr/bin/python3
"""
A module consuming a REST API and exporting data of interest
to a JSON file
"""
import json
import requests
import sys


if __name__ == "__main__":
    # get the user data from users api
    employee_id = sys.argv[1]
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(employee_id))
    user = r.json()
    json_file = "{}.json".format(employee_id)
    # get todo list associated with the user
    payload = {'userId': employee_id}
    r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params=payload)
    todos = r.json()
    # create a dictionary for every task of the format
    # {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    # "username": "USERNAME"}
    # append each dictianary entry to a list
    tasks = []
    task_dict = {}
    for todo in todos:
        task_dict["task"] = todo.get('title')
        task_dict["completed"] = todo.get('completed')
        task_dict["username"] = user.get('username')
        tasks.append(task_dict)
        task_dict = {}
    dict_obj = {employee_id: tasks}
    with open(json_file, mode='w') as f:
        json.dump(dict_obj, f)
