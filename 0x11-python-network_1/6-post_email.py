#!/usr/bin/python3
"""
a module for task 6 answer

sends a POST request
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    res = requests.post(url, data=data)
    print(res.text)
