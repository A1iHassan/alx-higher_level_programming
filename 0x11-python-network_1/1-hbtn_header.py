#!/usr/bin/python3
from sys import argv
from urllib.request import urlopen as req


url = argv[1]
with req(url) as response:
    body = response.read()
    print(body.headers['X-Request-Id'])
