#!/usr/bin/python3
from sys import argv
from urllib.request import urlopen as req


url = argv[1]
with req(url) as response:
	print(response.info().get('X-Request-Id'))
