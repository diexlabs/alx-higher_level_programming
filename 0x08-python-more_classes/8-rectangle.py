#!/usr/bin/python3

"""Real definition of a rectangle"""


class Rectangle:
    '''A rectlangle klas with getters and setters for attributes

    Attributes:
        width (int): the width of an instance
        height (int): the height attribute of an instance
        number_of_instances (int): keeps track of the total number of instances
        print_symbol (str): the character used for printing rectangle
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''instantiates a Reclangle object with optional width and height

        Variables:
            width (int): the width of the rectangle. defualts to 0
            height (int): the height of the rectangle. defaults to 0
        '''
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    def __str__(self) -> str:
        '''formatted string representation of instance'''
        string = ''
        if 0 in [self.width, self.height]:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            if i != self.height - 1:
                string += '\n'

        return string

    def __repr__(self) -> str:
        '''official representation of an instance'''
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        '''prints to output after an instance is deleted'''
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest of two rectangles'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
