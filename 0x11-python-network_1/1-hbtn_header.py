#!/usr/bin/python3
"""
a module for task 1 answer

sends a request to the URL and displays the value of the X-Request-Id
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
