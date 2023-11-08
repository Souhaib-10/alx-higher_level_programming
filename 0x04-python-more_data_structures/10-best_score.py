#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None:
        values_dict = a_dictionary.values()
        if len(values_dict) != 0:
            max_values = max(values_dict)
            return max_values
        else:
            return None
    return None
