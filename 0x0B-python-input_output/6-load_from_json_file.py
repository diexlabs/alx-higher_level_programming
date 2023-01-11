#!/usr/bin/python3
'''a programe that loads a python object from file'''


import json


def load_from_json_file(filename):
    '''loads a python object from file
    Args:
        filename (str) - name of file
    '''
    with open(filename) as f:
        json.load(f)
