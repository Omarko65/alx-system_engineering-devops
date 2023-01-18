#!/usr/bin/python3
'''a script that exports data in json format'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        uid = argv[1]
        url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
        filename = "{}.json".format(uid)
    except IndexError:
        exit

    r = requests.get(url)
    res = r.json()
    u_name = res.get('username')
    r = requests.get(url+'/todos')
    res = r.json()
    json_dict = {}
    json_dict[uid] = []
    for tasks in res:
        task_dict = {
            "task": tasks.get('title'),
            "completed": tasks.get('completed'),
            "username": u_name
        }
        json_dict[uid].append(task_dict)

    with open(filename, "w") as f:
        f.write(json.dumps(json_dict))
