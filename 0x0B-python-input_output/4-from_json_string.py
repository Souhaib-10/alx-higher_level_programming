#!/usr/bin/python3
"""script function change json to string"""
import json


def from_json_string(my_str):
    ''' function change json to obj

    Args:
        my_str: json data

    Returns:
        return obj data
    '''

    return json.loads(my_str)
