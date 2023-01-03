#!/usr/bin/python3
'''A module containing `lockedClass` klas definition'''


class LockedClass:
    '''A klas that allows for no dynamic attribute except `first_name`'''

    __slots__ = ['first_name']
