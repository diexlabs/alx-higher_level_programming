#!/usr/bin/python3
'''module for model Base Class'''

import json
import os
import turtle
import time


class Base:
    '''A base class for shapes models'''

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        '''initializes a base klas instance
        Args:
            id (int) - an integer identifier. defaults to None
        '''
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        '''returns a json representation of input'''
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''serializes `list_objs` to file'''
        if not list_objs:
            list_objs = []
        if not all([isinstance(x, Base) for x in list_objs]):
            raise ValueError("list_objs can only contain subclasses of `Base`")

        d_list = Base.to_json_string([x.to_dictionary() for x in list_objs])
        filename = f'{cls.__name__}.json'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(d_list)

    def from_json_string(json_string):
        '''returns a list of obj from json_string'''
        if not json_string:
            json_string = '[]'

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''creates a instance from attributes dict'''
        obj = cls(2, 2)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''loads objects from a json file'''
        filename = f'{cls.__name__}.json'
        if not os.path.exists(filename):
            return []

        with open(filename) as f:
            s = f.read()
            objs = cls.from_json_string(s)
            return [cls.create(**obj) for obj in objs]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''saves a list of objs as a csv file'''
        if not list_objs:
            list_objs = []
        if not all([isinstance(x, Base) for x in list_objs]):
            raise ValueError("list_objs can only contain subclasses of `Base`")

        d_list = [x.to_csv() for x in list_objs]
        filename = f'{cls.__name__}.csv'

        with open(filename, 'w', encoding='utf-8') as f:
            for line in d_list:
                f.write(line + '\n')

    @classmethod
    def load_from_file_csv(cls):
        '''loads objects from a csv file'''
        filename = f'{cls.__name__}.csv'
        if not os.path.exists(filename):
            return []

        with open(filename) as f:
            lines = f.readlines()
            objs = [cls.csv_to_dict(line) for line in lines]
            return [cls.create(**obj) for obj in objs]

    def draw(list_rectangles, list_squares):
        '''receives a list of shapes and draws them on screen'''
        SPACING = 20

        t = turtle.Turtle()
        t.pencolor('green')
        t.fillcolor('yellow')
        t.penup()
        t.setpos(-300, 150)
        t.pendown()

        for rectangle in list_rectangles:
            Base.trace_rect(t, rectangle)
            cord = t.pos()
            t.penup()
            t.goto(cord[0] + SPACING, cord[1])
            t.pendown()

        Base.draw_margin(t)

        for rectangle in list_squares:
            Base.trace_rect(t, rectangle)
            cord = t.pos()
            t.goto(cord[0] + SPACING, cord[1])

        time.sleep(60)

    def trace_rect(t, rectangle):
        '''Traces out a rectangle and returs to exact coorditnates'''
        t.setheading(-90)
        t.begin_fill()
        t.pendown()
        t.forward(rectangle.height)
        t.left(90)
        t.forward(rectangle.width)
        t.left(90)
        t.forward(rectangle.height)
        t.left(90)
        t.forward(rectangle.width)
        t.end_fill()
        t.backward(rectangle.width)
        t.penup()

    def draw_margin(t):
        '''draws a seperator to demarcate squares and rectangles'''
        t.setheading(0)
        t.penup()
        t.forward(50)
        t.right(90)
        t.pendown()
        t.fillcolor('red')
        t.begin_fill()
        t.forward(200)
        t.left(90)
        t.forward(2)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(2)
        t.end_fill()
        t.fillcolor('blue')
        t.penup()
        t.backward(52)
