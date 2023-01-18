#!/usr/bin/python3
''' a scropt that exports data in json format '''
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(url)
    res = r.json()
    json_dict = {}

    for users in res:
        u_id = users.get('id')
        u_name = users.get('username')
        json_dict[u_id] = []

        to_do = requests.get(url+'/{}/todos'.format(u_id))
        to_do_res = to_do.json()
        for tasks in to_do_res:
            to_do_dict = {
                "username": u_name,
                "task": tasks.get('title'),
                "completed": tasks.get('completed')
            }
            json_dict[u_id].append(to_do_dict)

    with open('todo_all_employess.json', 'w') as f:
        f.write(json.dumps(json_dict))
