#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None:
        values_dict = a_dictionary.values()
        max_values = max(values_dict)
        return max_values        
    return None
