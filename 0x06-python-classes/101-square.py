#!/usr/bin/python3

'''A module containing a `Square` klas'''


class Square:
    '''Square klas with a size private instance attribute'''

    def __init__(self, size=0, position=(0, 0)) -> None:
        '''instantiates an square instace while validating the size input'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''marks the coordinates of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        if not (
                isinstance(value, tuple)
                and len(value) == 2
                and all([isinstance(item, int)
                        and item >= 0 for item in value])
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''calculates the area of a square

        Return:
            area: (int) the area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        """prints a square of `size` size using the `#` character"""
        if self.size == 0:
            print()
        else:
            i = 0
            while i < self.position[1]:
                print()
                i += 1
            for i in range(self.size):
                print(" " * self.position[0], end='')
                print("#" * self.size)

    def __str__(self) -> str:
        '''prints out the square instance to stdout'''
        self.my_print()
