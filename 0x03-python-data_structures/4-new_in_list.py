#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)-1
    copy_list = my_list.copy()
    if idx > length or idx < 0:
        return None
    else:
        copy_list[idx] = element
        return copy_list
