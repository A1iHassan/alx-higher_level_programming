#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
            str[i] = chr(ord(str[i]) + 32)
            print("{}".format(str[i]), end='')
    print()
