#!/usr/bin/python3
''' a script that export data in csv format '''
import requests
from sys import argv


if __name__ == "__main__":
    try:
        uid = argv[1]
        url = ('https://jsonplaceholder.typicode.com/users/{}'.format(uid))
    except IndexError:
        exit

    r = requests.get(url)
    res = r.json()
    u_name = res.get("username")
    u_id = res.get("id")
    r = requests.get(url+'/todos')
    res = r.json()
    with open("{}.csv".format(uid), "w") as csv:
        for tasks in res:
            csv.write('"{}","{}",'.format(u_id, u_name))
            csv.write('"{}",'.format(tasks.get('completed')))
            csv.write('"{}"\n'.format(tasks.get('title')))
