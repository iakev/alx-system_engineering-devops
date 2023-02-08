#!/usr/bin/python3
"""
A module consuming a REST API and exporting data of interest
to a CSV file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    # get the user data from users api
    employee_id = sys.argv[1]
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(employee_id))
    user = r.json()
    csv_file = "{}.csv".format(employee_id)
    # get todo list associated with the user
    payload = {'userId': employee_id}
    r = requests.get("https://jsonplaceholder.typicode.com/todos",
                     params=payload)
    todos = r.json()
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([todo.get('userId'), user.get('username'),
                             todo.get('completed'), todo.get('title')])
