#!/usr/bin/python3
"""
a module for task 5 answer

sends a request and displays the value of
the variable X-Request-Id in the response header
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
