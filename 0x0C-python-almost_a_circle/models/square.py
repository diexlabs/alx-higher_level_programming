#!/usr/bin/python3
'''A module for `Square` klas'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''A subclass of ``Rectangle`` with equal height and width'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''gets and sets the size of the square
        Note:
            sets the width and height attribute to the size
        '''
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates the attributes of instance'''
        if args:
            if args:
                self.id = args[0]
                args = args[1:]
            if args:
                self.size, args = args[0], args[1:]
            if args:
                self.x, args = args[0], args[1:]
            if args:
                self.y = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of square'''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def to_csv(self):
        '''returns a comma seperated value of instance attrs'''
        return ', '.join(
            [str(item) for item in [self.id, self.size, self.x, self.y]]
        )

    def csv_to_dict(s: str):
        '''converts a csv string to an attritute dict'''
        attrs = s.split(", ")
        id, size, x, y = [int(item) for item in attrs]
        return {'id': id, 'size': size, 'x': x, 'y': y}
