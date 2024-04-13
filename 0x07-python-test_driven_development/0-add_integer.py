#!/usr/bin/python3
"""
test for module "add_integer(a, b=98):".
have just one function.
"""


def add_integer(a, b=98):
    """ return addition of two numbers

    Args:
        a: the fierst argument (int, flaot)
        b: the second argument (int, float)

    Raises:
        TypeError : if a, b are not int or float

    Returns:
        the sum of two arguments
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a+b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
