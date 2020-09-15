#!/usr/bin/python3
""" Get a JSON file of user tasks
"""

import json
import requests
from sys import argv


def todos_csv():
    """ execute if main
    """

    url_base = 'https://jsonplaceholder.typicode.com'
    try:
        emp_id = int(argv[1])
        emp_data = requests.get('{}/users/{}'.format(url_base, emp_id))
        emp_name = emp_data.json().get('username')
        task_all = requests.get('{}/todos?userId={}'.format(url_base, emp_id))

        task_dict = {}
        task_dict[emp_id] = []
        for task in task_all.json():
            task_dict[emp_id].append({'task': task.get('title'),
                                      'completed': task.get('completed'),
                                      'username': task.get('username')})
        with open(str(emp_id) + '.json', 'w') as request:
            json.dump(task_dict, request)
    except ValueError:
        exit


if __name__ == '__main__':
    todos_csv()
