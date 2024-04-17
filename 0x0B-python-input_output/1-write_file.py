#!/usr/bin/python3
'''script function to write in file'''


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UFT-8") as f:
        return f.write(text)
