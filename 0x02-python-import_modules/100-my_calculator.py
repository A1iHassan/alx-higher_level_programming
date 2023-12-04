#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv
    x = ["+", "-", "*", "/"]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif not argv[2] in x:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, calc.add(a, b)))
        elif argv[2] == "-":
            print("{} - {} = {}".format(a, b, calc.sub(a, b)))
        elif argv[2] == "*":
            print("{} * {} = {}".format(a, b, calc.mul(a, b)))
        elif argv[2] == "/":
            print("{} / {} = {}".format(a, b, calc.div(a, b)))
