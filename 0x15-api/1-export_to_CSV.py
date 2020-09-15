#!/usr/bin/python3
""" ToDo's module by employee
        Get all done tasks
"""

import csv
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

        with open(str(emp_id) + '.csv', 'w') as request:
            cursor = csv.writer(request, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
            for task in task_all.json():
                cursor.writerow([emp_id, emp_name,
                                 task.get('completed'),
                                 task.get('title')])
    except ValueError:
        exit


if __name__ == '__main__':
    todos()
