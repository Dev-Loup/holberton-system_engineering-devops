#!/usr/bin/python3
""" Get a JSON file of all user tasks
"""

import json
import requests


def todos_json_all():
    """ execute if main
    """

    url_base = 'https://jsonplaceholder.typicode.com'
    task_all = requests.get('{}/todos'.format(url_base))

    task_dict = {}
    for task in task_all.json():
        emp_id = task.get('userId')
        if task_dict.get(emp_id) is None:
            task_dict[emp_id] = []
            emp_data = requests.get('{}/users/{}'.format(url_base, emp_id))
            emp_name = emp_data.json().get('username')
        task_dict[emp_id].append({'task': task.get('title'),
                                  'completed': task.get('completed'),
                                  'username': emp_name})
    with open('todo_all_employees.json', 'w') as request:
        json.dump(task_dict, request)


if __name__ == '__main__':
    todos_json_all()
