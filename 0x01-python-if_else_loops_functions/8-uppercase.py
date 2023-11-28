#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        x = str[i]
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            x = chr(ord(str[i]) - 32)
        print("{}".format(x), end='')
    print()
