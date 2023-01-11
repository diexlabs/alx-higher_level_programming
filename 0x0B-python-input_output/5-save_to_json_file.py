#!/usr/bin/python3
'''A module for a function that writes a
json encoded string to file
'''


import json


def save_to_json_file(my_obj, filename):
    '''serializes an object to file
    Args:
        my_obj - a python object
        filename - name of file to write to
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
