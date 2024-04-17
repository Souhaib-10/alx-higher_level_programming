#!/usr/bin/python3
''' script for read file

    Args:
    filename (str): name of file
'''


def read_file(filename=""):
    '''read file'''
    with open(filename) as f:
        test = f.read()
        print(text, end="")
