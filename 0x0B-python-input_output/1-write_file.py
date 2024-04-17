#!/usr/bin/python3
'''script function to write in file'''


def write_file(filename="", text=""):
    ''' function to write in file

    Args:
        filename (str): name file
        text (str): text to write in file
    Return :
        text written in file
    '''

    with open(filename, "w", encoding="UFT-8") as f:
        return f.write(text)
