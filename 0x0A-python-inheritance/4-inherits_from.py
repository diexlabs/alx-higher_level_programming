#!/usr/bin/python3
'''A module for `inherits_from` function'''


def inherits_from(obj, a_class):
    '''Checks if an object is a subclass of class'''
    return issubclass(obj.__class__, a_class) and obj.__class__ is not a_class
