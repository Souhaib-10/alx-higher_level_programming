#!/usr/bin/python3
'''script function to read file'''


def read_file(filename=""):
    """function that reads a text file and prints it"""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
