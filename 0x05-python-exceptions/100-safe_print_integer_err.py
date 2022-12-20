#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        s = ("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(str(err))
        sys.stderr.write('\n')
        return False
    else:
        print(s)
        return True
