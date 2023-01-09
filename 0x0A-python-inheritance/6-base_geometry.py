#!/usr/bin/python3
'''A module for `BaseGeometry` klas'''


class BaseGeometry:
    '''An base class for geometric shapes'''

    def area(self):
        '''A base method to be overriden by subclasses

        Raises:
            Exception - area() is not implemented
        '''
        raise Exception("area() is not implemented")
