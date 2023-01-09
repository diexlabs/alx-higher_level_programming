#!/usr/bin/python3
'''A module for a ``Rectangle class inheriting from ``BaseGeometry``'''

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''A rectangel class inheriting from ``BaseGeometry``'''

    def __init__(self, width, height):
        '''initializes `width` and `height` as private integers
        Args:
            width (int): width of the instance
            height (int): height of the instance

        Note:
            the `width` and `height` are first validated using
            integer_validator and then set as private attributes
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Computes the area of the rectangel
        Return:
            area (int)
        '''
        return self.__height * self.__width

    def __str__(self):
        '''returns a string representation of the rectangle'''
        return f"[Rectangle] {self.__width}/{self.__height}"
