#!/usr/bin/python3

'''A module containing a `Square` klas'''


class Square:
    '''Square klas with a size private instance attribute'''

    def __init__(self, size=0) -> None:
        '''initializes a square instance while validating size input

        Args:
            size (int): the size input

        Raises:
            TypeError: if size is not a valid int
            ValueError: if size is less than 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
