#!/usr/bin/python3
"""script to export all employees data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    get_user = requests.get("https://jsonplaceholder.typicode.com/users")
    get_user = get_user.json()
    get_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    get_todo = get_todo.json()
    todo_A = {}

    for user in get_user:
        taskList = []
        for task in get_todo:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todo_A[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_A, f)
