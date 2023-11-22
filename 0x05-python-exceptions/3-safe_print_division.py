#!/bin/usr/python3
def safe_print_division(a, b):
    try:
        op = a/b
    except ZeroDivisionError:
        op = None
    finally:
        print("Inside result: {}".format(op))
    return op
