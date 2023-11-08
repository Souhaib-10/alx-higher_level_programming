#!/usr/bin/python
def multiply_by_2(a_dictionary):
    for i, v in a_dictionary.items():
        a_dictionary[i] = v*2
        print("{}: {}".format(i, a_dictionary[i]))
