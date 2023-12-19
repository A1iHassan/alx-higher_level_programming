#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        sys.stderr("Exception: {}".format(e))
        return False
    else:
        return True
