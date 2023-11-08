#!/usr/bin/pyton3
def uniq_add(my_list=[]):
    change_type = set(my_list)
    result = 0
    for i in change_type:
        result += i
    return result
