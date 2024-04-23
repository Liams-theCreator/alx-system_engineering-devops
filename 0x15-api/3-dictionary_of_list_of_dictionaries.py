#!/usr/bin/python3
"""
Script with Rest API
"""
import json
import requests
import sys

if __name__ == '__main__':

    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users'.format(api_url)
    response_users = requests.get(user_url).json()
    users_tasks = {}

    for user in response_users:
        user_id = user.get('id')
        users_tasks[user_id] = []
        todos_url = '{}/{}/todos'.format(user_url, user_id)
        response_final = requests.get(todos_url).json()
        for task in response_final:
            task = {'task': task.get('title'),
                    'username': user.get('username'),
                    'completed': task.get('completed')}
            users_tasks[user_id].append(task)

    with open('todo_all_employees.json', 'w', encoding='utf-8') as json_file:
        json.dump(users_tasks, json_file)
