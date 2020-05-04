#!/usr/bin/python3
''' Python script that fetches https://jsonplaceholder.typicode.com
and export data in a JSON file
'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    employees = requests.get('https://jsonplaceholder.typicode.com/users').json()

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_dic = {}
    username_dic = {}
    for user in employees:
        user_id = user.get('id')
        user_dic[user_id] = []
        username_dic[user_id] = user.get('username')

    for task in todos:
        task_dic = {}
        user_id = task.get('userId')
        task_dic['task'] = task.get('title')
        task_dic['completed'] = task.get('completed')
        task_dic['username'] = username_dic.get(user_id)
        user_dic.get(user_id).append(task_dic)
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_dic, jsonfile)
