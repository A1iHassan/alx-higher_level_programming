#!/usr/bin/python
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        print("Exception: {}".format(error))
