#!/usr/bin/python3
from add_0.py import add
if __name__ == "__main__":
    a = 1
    b = 2
    print("{:=1} + {:=2} = {:=3}".format(a, b, add(a, b)))
