#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError as e:
        import sys


        sys.stderr.write("Exception: {}".format(e))
        return False
