#!/usr/bin/python3
"""
Script with Rest API
"""
import csv
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

    with open('{}.csv'.format(emp_id), mode='w') as employee_f:
        writer = csv.writer(employee_f, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in response_final:
            status = elem.get('completed')
            title = elem.get('title')
            writer.writerow([emp_id, username, status, title])
