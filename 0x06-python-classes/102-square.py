#!/usr/bin/python3

'''A module containing a `Square` klas'''


class Square:
    '''Square klas with a size private instance attribute'''

    def __init__(self, size=0) -> None:
        '''instantiates an square instace while validating the size input'''
        self.size = size

    @property
    def size(self):
        '''returns the size private attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''calculates the area of a square

        Return:
            area (int): the area of the square
        '''
        return self.__size ** 2

    def __eq__(self, square) -> bool:
        '''compares two squares for equality'''
        return self.size == square.size

    def __gt__(self, square):
        '''compares two squares for inequality'''
        return self.size > square.size

    def __lt__(self, square):
        '''compares two squares for inequality'''
        return self.size < square.size

    def __ge__(self, square):
        '''compares if size is greater than or equal to square.size'''
        return self.size > square.size or self.size == square.size

    def __le__(self, square):
        '''compares if size is less than or equal to square size'''
        return self.size < square.size or self.size == square.size
