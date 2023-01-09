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

    def integer_validator(self, name, value):
        '''Validates that value is a non zero positive integer

        Args:
            name (str): A string name of variable
            value (int): The integer value of `name`
        Raises:
            TypeError - if value is not a valid int
            ValueError - if value is less than 0
        Return:
            None
        '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return
