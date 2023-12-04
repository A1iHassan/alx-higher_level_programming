#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    y = "argument" if x == 2 else "arguments"
    print("{} {}{}".format(x - 1, "." if x == 1 else ":"))
    if x > 1:
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]))
