#!/usr/bin/python3
def div(i):
    return i / 2

def divisible_by_2(my_list=[]):
    x = [i % 2 == 0 for i in my_list]
    return x
