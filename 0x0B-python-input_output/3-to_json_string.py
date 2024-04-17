#!/usr/bin/python3
"""script function change obj to json"""
import json


def to_json_string(my_obj):
    ''' function change obj to json

    Args:
        obj: object data

    Returns:
        return json data
    '''

    return json.dumps(my_obj)
