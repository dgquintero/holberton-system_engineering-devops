#!/usr/bin/python3
''' Python script that fetches https://jsonplaceholder.typicode.com/posts/1
'''
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    employee = requests.get('{}/users/{}'.format(url, user_id)).json()

    todos = requests.get('{}/users/{}/todos'.format(url, user_id)).json()

    task_list = []
    for task in todos:
        if task.get('completed') is True:
            task_list.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(employee.get('name'),
                                                          len(task_list),
                                                          len(todos)))
    print('\n'.join('\t {}'.format(task) for task in task_list))
