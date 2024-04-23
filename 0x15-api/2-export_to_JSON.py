#!/usr/bin/python3
"""Script to export employee tasks data in the JSON format."""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_i = sys.argv[1]
    get_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(user_i))
    get_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    get_todo = get_todo.json()

    todoUser = {}
    taskList = []

    for task in get_todo:
        if task.get('userId') == int(user_i):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": get_user.json().get('username')}
            taskList.append(taskDict)
    todoUser[user_i] = taskList

    filename = user_i + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
