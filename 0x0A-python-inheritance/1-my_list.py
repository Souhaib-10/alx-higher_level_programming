#!/usr/bin/python3

"""
defines a custom list class, MyList, that extends the built-in list class.
"""


class MyList(list):
    """
    A custom list class that extends the built-in list class.

    This class adds functionality to print the list in sorted order.

    Attributes:
    None

    Methods:
    print_sorted(): Prints a sorted version of the list.
    """

    def print_sorted(self):
        """
        Prints a sorted version of the list.

        Args:
        None

        Returns:
        None
        """
        print(sorted(self))
