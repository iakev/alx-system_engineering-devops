#!/usr/bin/python3
"""
A module consuming a REST API and exporting data of interest
to a JSON file
"""
import json
import requests


if __name__ == "__main__":
    # get all users data from users api
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    users = r.json()
    json_file = "todo_all_employees.json"
    obj_dict = {}
    for user in users:
        tasks = []
        task_dict = {}
        payload = {'userId': user.get('id')}
        r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params=payload)
        todos = r.json()
        for todo in todos:
            task_dict["username"] = user.get('username')
            task_dict["task"] = todo.get('title')
            task_dict["completed"] = todo.get('completed')
            tasks.append(task_dict)
            task_dict = {}
        obj_dict[user.get('id')] = tasks
    with open(json_file, mode='w') as f:
        json.dump(obj_dict,f)
