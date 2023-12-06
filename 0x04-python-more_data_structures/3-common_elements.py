#!/usr/bin/python3
def common_elements(set_1, set_2):
    x = set(i for i in set_1 if i in set_2)
    return x
