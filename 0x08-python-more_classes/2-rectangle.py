#!/usr/bin/python3

"""Real definition of a rectangle"""


class Rectangle:
    '''A rectlangle klas with getters and setters for attributes

    Attributes:
        width (int): the width of an instance
        height (int): the height attribute of an instance
    '''

    def __init__(self, width=0, height=0):
        '''instantiates a Reclangle object with optional width and height

        Variables:
            width (int): the width of the rectangle. defualts to 0
            height (int): the height of the rectangle. defaults to 0
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''The width attribute of an instance as a property'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''The height attribute of an  instance as a property'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''calculates and returns the area of the instance'''
        return self.height * self.width

    def perimeter(self):
        '''calculates and returns the perimeter of the instance'''
        if 0 in [self.height, self.width]:
            return 0
        return 2 * (self.width + self.height)
