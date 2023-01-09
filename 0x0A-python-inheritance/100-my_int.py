#!/usr/bin/python3
'''A module for ``MyInt`` klas inheriting from int'''


class MyInt(int):
    '''A dummy implementation of int that reverses comparison'''

    def __eq__(self, __x: object) -> bool:
        '''reverses comparisom of int for equality'''
        return not super().__eq__(__x)

    def __ne__(self, __x: object) -> bool:
        '''Reverses integer comparisom for not equal'''
        return not super().__ne__(__x)
