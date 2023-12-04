#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    print("{} {}{}".format(x - 1, "argument" if x == 2 else "arguments", "." if x == 1 else ":"))
    if x > 1:
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]))
