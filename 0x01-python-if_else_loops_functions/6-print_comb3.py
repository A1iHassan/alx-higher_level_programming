#!/usr/bin/python3
for i in range(9):
    for j in range(i, 10):
        print("{}{}".format(i, j), end=", ")
        if i == j == 8:
            break
else:
    print("{}".format(89))
