#!/usr/bin/python3
''' Python script that fetches https://jsonplaceholder.typicode.com
and export data in the CSV format
'''
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    employee = requests.get('{}/users/{}'.format(url, user_id)).json()

    todos = requests.get('{}/users/{}/todos'.format(url, user_id)).json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            w.writerow([
                int(user_id),
                employee.get('username'),
                task.get('completed'),
                task.get('title')
            ])
