#!/usr/bin/python3

'''A module containing a square class with a private size attribute'''

class Square:
    '''Square klas with a size private instance attribute'''

    def __init__(self, size=None) -> None:
        '''instantiates a square instance with size param

        Args:
            size: (int) the size of the square
        '''
        if size is not None:
            self.__size = size
