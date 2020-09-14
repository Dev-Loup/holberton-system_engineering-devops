#!/usr/bin/python3
""" ToDo's module by employee
        Get all done tasks
"""

from sys import argv
import requests

url_base = 'https://jsonplaceholder.typicode.com'
emp_id = argv[1]
req_emp = requests.get('{}/users/{}'.format(url_base, emp_id))
emp_name = req_emp.json().get('name')
all_t = requests.get('{}/todos?userId={}'.format(url_base, emp_id))
done_t = requests.get('{}/todos?userId={}&completed=true'
                      .format(url_base, emp_id))

print('Employee {} is done with tasks({}/{}):'
      .format(emp_name, len(done_t.json()), len(all_t.json())))

for task in done_t.json():
    print('\t {}'.format(task.get('title')))
