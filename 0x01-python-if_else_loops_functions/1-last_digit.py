#!/usr/bin/python3
import random
number = -89
msg = f"Last digit of {number:d} is {number % 10}"
if number < 0:
    number = -number
    msg = f"Last digit of {number:d} is -{number % 10}"
if number % 10 > 5:
    print(f"{msg} and is greater than 5")
elif number % 10 == 0:
    print(f"{msg} and is 0")
else:
    print(f"{msg} and is less than 6 and not 0")
