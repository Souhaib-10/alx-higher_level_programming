#!/usr/bin/python3
def add_integer(a, b=98):
    types = [int, float]
    if type(a) not in types or a is None:
        raise TypeError("a must be an integer")
    elif (type(a) is float):
        a = int(a)
    if type(b) not in types:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)
    return a+b
