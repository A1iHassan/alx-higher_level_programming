#!/usr/bin/python3
"""
a module for task 1 answer

send a request to the URL and display the value of the X-Request-Id
"""

import sys
import urllib.request


url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
	print(dict(resp.headers).get("X-Request-Id"))
