#!/usr/bin/python3
"""
test for module "add_integer(a, b=98):".
have just one function.
"""


def add_integer(a, b=98):
    """ return addition of two numbers"""
    if type(a) not in [int, float]:
        raise typeError("a must be an integer")
    if type(b) not in [int, float]:
        raise typeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b
