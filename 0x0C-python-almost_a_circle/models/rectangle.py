#!/usr/bin/python3
'''a module for a rectangel klas that inherits from base'''

from .base import Base


class Rectangle(Base):
    '''A rectangle klas inheriting from base'''

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        '''initializes a rectangle klas given params
        Args:
            width (int) - width of instance
            height (int) - height of instance
            x (int) - x cordinate of instance. Defaults to 0
            y (int) - y cordinate of instance. Defaults to 0
            id (int) - id of instance
            
        Note:
            this method initializes superclass with id
        '''
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def __str__(self) -> str:
        '''returns the string representation of instance'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
            {self.width}/{self.height}"

    @property
    def height(self):
        '''gets and sets the height of instance as private attribute

        Raises:
            TypeError - if value is not an integer
            ValueError - if value is less or equal to 0
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        '''gets and sets the width of instance as private attribute

        Raises:
            TypeError - if value is not an integer
            ValueError - if value is less or equal to 0
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        '''gets and sets the height of instance as private attribute

        Raises:
            TypeError - if value is not an integer
            ValueError - if value is less than 0
        '''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''gets and sets the y coordinate of instance as private attribute

        Raises:
            TypeError - if value is not an integer
            ValueError - if value is less than 0
        '''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''computes and returns the area of the instance
        Returns:
            area - calculated as self.width * self.height
        '''
        return self.width * self.height

    def display(self):
        '''prints out the instance on stdout using `#` character'''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        '''updates all the instance attributes from args'''
        if args:
            if args:
                self.id = args[0]
                args = args[1:]
            if args:
                self.width, args = args[0], args[1:]
            if args:
                self.height, args = args[0], args[1:]
            if args:
                self.x, args = args[0], args[1:]
            if args:
                self.y = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of instance'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def to_csv(self):
        '''returns a comma seperated value of instance attrs'''
        return ', '.join(
            [str(item) for item in [
                self.id, self.width, self.height, self.x, self.y
            ]]
        )

    def csv_to_dict(s: str):
        '''converts a csv string to an attritute dict'''
        attrs = s.split(", ")
        id, width, height, x, y = [int(item) for item in attrs]
        return {'id': id, 'width': width, 'height': height, 'x': x, 'y': y}
