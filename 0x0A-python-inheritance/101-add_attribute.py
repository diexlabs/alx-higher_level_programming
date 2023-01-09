#!/usr/bin/python3
'''A module for add_attribute function'''


def add_attribute(obj, name: str, value):
    '''adds attribute to obj
    Args:
        obj (obj): A python object
        name (str): name of attribute to add
        value (Any): value of attribute to set

    Raises:
        TypeError - can't add new attribute
    Note:
        checks that an attribute can be added before trying to set
        it
    '''
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
