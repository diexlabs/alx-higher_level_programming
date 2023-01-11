#!/usr/bin/python3
'''A module for a function that loads an object from json'''


import json


def from_json_string(my_str):
    '''loads an object from json string'''
    if not my_str or type(my_str) is not str:
        return
    return json.loads(my_str)
