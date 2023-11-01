#!/usr/bin/python3
def islower(c):
    conv_to_number = ord(c)
    if 97 <= conv_to_number and conv_to_number <= 122:
        return True
    else:
        return False
