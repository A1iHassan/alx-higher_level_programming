#!/usr/bin/python3
"""
a module for task 3 answer

sends a request and manages HTTPError exceptions
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
