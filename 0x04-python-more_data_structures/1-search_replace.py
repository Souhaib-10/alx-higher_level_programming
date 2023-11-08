#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replace_function(x):
        if x == search:
            return replace
        else:
            return x
    doing_replace = list(map(replace_function, my_list))
    return doing_replace
