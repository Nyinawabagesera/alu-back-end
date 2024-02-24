#!/usr/bin/python3
"""Script to fetch TODOs for a user from API"""

import requests
import sys

def main():
    """Main function to fetch and display TODOs"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)

    total_tasks = 0
    completed_tasks = []
    for task in response.json():
        if task['userId'] == user_id:
            total_tasks += 1
            if task['completed']:
                completed_tasks.append(task['title'])

    user_name = requests.get(user_url).json()['name']

    print("Employee {} has completed tasks ({}/{}):".format(user_name,
          len(completed_tasks), total_tasks))
    for completed_task in completed_tasks:
        print("\t{}".format(completed_task))

if __name__ == '__main__':
    main()
