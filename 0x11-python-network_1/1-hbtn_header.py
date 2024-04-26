#!/usr/bin/python3
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
	print(response.info().get('X-Request-Id'))
