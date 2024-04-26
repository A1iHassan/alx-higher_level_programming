#!/usr/bin/python3
"""
a module for task 2 answer

sends a POST request to the passed URL with the email as a parameter
"""


if __name__ == "__main__":
    import sys
    import urllib.request as req
    import urllib.parse as prs

    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    req_string = prs.urlencode(email).encode('ascii')
    req_obj = req.Request(url, req_string)
    with req.urlopen(req_obj) as response:
        body = response.read().decode('utf-8')
        print(body)
