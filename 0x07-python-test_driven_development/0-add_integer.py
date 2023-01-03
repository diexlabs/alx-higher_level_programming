#!/usr/bin/python3
'''A module for `add_integer `function`'''

def add_integer(a, b=98):
    '''returns the sum of two integers
    
    Raises:
        TypeError: if either a or b is not int or float
    Returns:
        sum (int): the sum of the two inputs
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
