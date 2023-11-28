#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(i) >= 65 and ord(i) <= 90:
            print("{}".format(ord(i + 32)), end='')
    print()
