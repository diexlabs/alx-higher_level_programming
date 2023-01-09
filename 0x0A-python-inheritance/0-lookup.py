#!/usr/bin/python3

'''A module for the implementation of lookup function
Note:
    the lookup method returns all the attributes of its argument
'''


def lookup(obj: object):
    '''Returns the attribute list of its argument
    Args:
        obj (obj): A python obj
    Return:
        list[str]: A list of string attributes
    '''

    return dir(obj)
