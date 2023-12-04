#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = my_list[:]
    if idx >= len(my_list) or idx < 0:
        return x
    x[idx] = element
    return x
