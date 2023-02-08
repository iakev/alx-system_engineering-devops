#!/usr/bin/python3
"""
A module consuming a REST API and highglighting the requisite data
"""
import requests
import sys

# get the user data from users api
employee_id = sys.argv[1]
r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                 .format(employee_id))
user = r.json()
# get todo list associated with the user
payload = {'userId': employee_id}
r = requests.get("https://jsonplaceholder.typicode.com/todos",
                 params=payload)
todos = r.json()
# count number of todos in todos dictionary and completed
# also get title of completed tasks
total = len(todos)
completed = 0
completed_id = {}
for todo in todos:
    if todo.get('completed'):
        completed += 1
        completed_id[todo.get('id')] = todo.get('title')
# print to stdout
print("Employee {} is done with tasks({}/{}):"
      .format(user.get('name'), completed, total))
print("\t ", end="")
i = 0
for k, v in completed_id.items():
    i = i + 1
    print(v, end="\n\t " if i < completed else "\n")
