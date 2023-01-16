#!/usr/bin/python3
'''A test module for ``models/square.py``'''

from unittest import TestCase
from models.square import Square


class TestSquareCase(TestCase):
    def setUp(self) -> None:
        self.square = Square(12, 2, 2, 20)

    def test_init_works(self):
        square = self.square
        self.assertEqual(square.id, 20)
        self.assertTrue(isinstance(square, Square))

    def test_size_correctly_initialized(self):
        square = self.square
        self.assertEqual(square.width, 12)
        self.assertEqual(square.height, 12)

    def test_size_property_works(self):
        square = self.square
        self.assertEqual(square.size, 12)
        square.size = 15
        self.assertEqual(square.size, 15)

    def test_update_works(self):
        square = self.square
        self.assertEqual(square.id, 20)
        square.update(10)
        self.assertEqual(square.id, 10)

    def test_update_works_with_variable_args(self):
        square = self.square
        square.update(2,2,2,2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.size, 2)

        square.update(4,4)
        self.assertEqual(square.size, 4)

    def test_update_works_with_kwargs(self):
        square = self.square
        square.update(x=20, y=20)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 20)

    def test_to_dictionary_works(self):
        square = self.square
        d = {'id': 20, 'size': 12, 'x': 2, 'y': 2}
        self.assertEqual(square.to_dictionary(), d)
