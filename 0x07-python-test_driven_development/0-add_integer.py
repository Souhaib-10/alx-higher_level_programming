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

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a+b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
