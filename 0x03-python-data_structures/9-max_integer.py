#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximum = my_list[0]
    for i in my_list:
        maximum = i if i > maximum else maximum
    return maximum
