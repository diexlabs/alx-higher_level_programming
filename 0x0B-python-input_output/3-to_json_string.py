#!/usr/bin/python3
'''A module for a function that returns a json repr of
object to standard out
'''


import json


def to_json_string(my_obj):
    '''returns the json serialized form of obj
    Args:
        my_obj - python object to serialize
    '''
    return json.dumps(my_obj)
