#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{}".format(sum(int(arg) for arg in argv[1:])))
