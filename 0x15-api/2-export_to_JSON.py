#!/usr/bin/python3
''' Python script that fetches https://jsonplaceholder.typicode.com
and export data in a JSON file
'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    employee = requests.get('{}/users/{}'.format(url, user_id)).json()

    todos = requests.get('{}/users/{}/todos'.format(url, user_id)).json()

    task_list = []
    for task in todos:
        task_dic = {}
        task_dic['task'] = task.get('title')
        task_dic['completed'] = task.get('completed')
        task_dic['username'] = employee.get('username')
        task_list.append(task_dic)
    json_obj = {}
    json_obj[user_id] = task_list
    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
