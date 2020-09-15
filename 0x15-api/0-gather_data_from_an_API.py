#!/usr/bin/python3
""" ToDo's module by employee
        Get all done tasks
"""

import requests
from sys import argv


def todos():
    """ execute if main
    """

    url_base = 'https://jsonplaceholder.typicode.com'
    try:
        emp_id = int(argv[1])
        emp_data = requests.get('{}/users/{}'.format(url_base, emp_id))
        emp_name = emp_data.json().get('name')
        task_all = requests.get('{}/todos?userId={}'.format(url_base, emp_id))
        task_done = requests.get('{}/todos?userId={}&completed=true'
                                 .format(url_base, emp_id))

        print('Employee {} is done with tasks({}/{}):'
              .format(emp_name, len(task_done.json()), len(task_all.json())))

        for task in task_done.json():
            print('\t {}'.format(task.get('title')))
    except ValueError:
        exit


if __name__ == '__main__':
    todos()
