#!/usr/bin/python3
"""
Script with Rest API
"""
import json
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

    username = response_user.get('username')

    response_final = requests.get(final_url).json()

    new_dictionary = []
    for task in response_final:
        data = {'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username}
        new_dictionary.append(data)

    with open('{}.json'.format(emp_id), 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps({emp_id: new_dictionary}))
