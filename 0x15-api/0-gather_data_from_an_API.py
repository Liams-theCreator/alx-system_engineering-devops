#!/usr/bin/python3
"""
Script with Rest API
"""
import requests
import sys


if __name__ == '__main__':
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, emp_id)
    final_url = '{}/todos'.format(user_url)

    response_user = requests.get(user_url).json()

    name = response_user.get('name')

    response_final = requests.get(final_url).json()

    total = len(response_final)

    completed = 0
    tasks = []

    for task in response_final:
        if task.get('completed'):
            completed += 1
            tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, total))

    for task in tasks:
        print('\t', task.get('title'))
