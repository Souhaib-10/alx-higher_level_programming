#!/usr/bin/python
def multiply_by_2(a_dictionary):
    a_dictionary2 = {}
    for i, v in a_dictionary.items():
        a_dictionary2[i] = v*2
    return a_dictionary2
