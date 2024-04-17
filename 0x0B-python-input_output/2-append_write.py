#!/usr/bin/python3
'''script for function append text end of file'''


def append_write(filename="", text=""):
    '''Append a string to text file

    Args:
    filename (str): the name of the file
    text (str): the text to append to the file

    Returns:
        return  the number of characters added
    '''

    with open(filename="", "a", encoding="utf-8") as f:
        return f.write(text)
