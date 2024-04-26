#!/usr/bin/python3
"""
a module for task 10 answer
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
