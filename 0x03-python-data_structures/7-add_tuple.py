#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_tuple = ()
    if len(tuple_b) < 2:
        if len(tuple_b) < 1:
            return (tuple_a)
        else:
            tuple_b += (0,)
            for i, j in zip(tuple_a, tuple_b):
                result_tuple += ((i+j),)
            return result_tuple
    else:
        first_two_elements = tuple_a[:2]
        first_two_elements_b = tuple_b[:2]
        for i, j in zip(first_two_elements, first_two_elements_b):
            result_tuple += ((i+j),)
        return result_tuple
