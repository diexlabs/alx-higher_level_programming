#!/usr/bin/python3

'''A module for `is_same_class` function'''


def is_same_class(obj, a_class):
    '''checks if an obj is an instance of a class
    Args:
        obj (obj): a python object
        a_class (class): A python class
    Return:
        (bool): True else False
    '''

    return True if obj.__class__ is a_class else False
