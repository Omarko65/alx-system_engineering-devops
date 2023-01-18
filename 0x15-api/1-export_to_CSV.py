#!/usr/bin/python3
''' a script that export data in csv format '''
import csv
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
    with open("{}.csv".format(uid), "w") as csvf:
        csvwriter = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for tasks in res:
            csvwriter.writerow([
                u_id,
                u_name,
                tasks.get('completed'),
                tasks.get('title')
            ])
