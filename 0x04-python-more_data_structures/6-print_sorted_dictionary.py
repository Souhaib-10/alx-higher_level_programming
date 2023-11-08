#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {k: v for k, v in sorted(a_dictionary.items())}
    for i, j in sorted_dict.items():
        print("{}: {}".format(i, j))
