#!/usr/bin/python3

'''A module for `is_kind_of_class` function'''


def is_kind_of_class(obj, a_class):
    '''Returns True if ``obj`` is instance of <klas>a_class

    Args:
        obj - A python object
        a_class - a python class

    Return:
        True else False
    '''
    return isinstance(obj, a_class)
