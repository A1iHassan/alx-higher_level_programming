#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(f"{my_list[i]}", sep="", end="")
    except IndexError:
        print()
        return i
    else:
        print()
        if x == 0:
            return x
        else:
            return i + 1
