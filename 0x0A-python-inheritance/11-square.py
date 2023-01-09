#!/usr/bin/python3
'''A module for `Square` klas'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''A square class inheritin from ``Rectangle`` klas'''

    def __init__(self, size):
        '''instantiates size attribute
        Args:
            size (int): the size of the square
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Computes the area of the square

        Note:
            This calculation is based on the formular A = l * l
        '''
        return self.__size ** 2

    def __str__(self):
        '''Returns the string representation of ``Square`` klas'''
        return f"[Square] {self.__size}/{self.__size}"
