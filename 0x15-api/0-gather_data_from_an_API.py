#!/usr/bin/python3
''' a script that uses rest api to return information about users '''
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
    print('Employee {} is done with '.format(res['name']), end="")
    r = requests.get(url+'/todos')
    res = r.json()
    done = 0
    task = 0
    for tasks in res:
        if tasks.get('completed'):
            done = done + 1
        task = task + 1
    print('tasks({}/{})'.format(done, task))
    for titles in res:
        if titles.get('completed'):
            print('\t {}'.format(titles['title']))
