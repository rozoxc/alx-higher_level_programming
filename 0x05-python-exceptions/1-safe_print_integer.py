#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
    except (ValueError, TypeError):
        return False
    else:
        print("{:d}".format(value))
        return True
