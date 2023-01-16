#!/usr/bin/python3
'''a test module for the rectangle class'''

from unittest import TestCase
from models.rectangle import Rectangle


class TestRectangleCase(TestCase):
    '''test case class for rectangle class'''

    def setUp(self) -> None:
        self.rect = Rectangle(12, 10, 2, 4, 3)

    def test_init_works(self):
        self.assertTrue(isinstance(self.rect, Rectangle))

    def test_attrs_correct(self):
        rect = self.rect
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 3)

    def test_attrs_are_private(self):
        rect = self.rect
        attrs = ["__x", "__y", "__width", "__height"]
        for attr in attrs:
            with self.assertRaises(AttributeError):
                getattr(rect, attr)

    def test_width_is_valid(self):
        rect = self.rect
        with self.assertRaises(TypeError):
            rect.width = 'width'
        with self.assertRaises(ValueError):
            rect.width = -1
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_is_valid(self):
        rect = self.rect
        with self.assertRaises(TypeError):
            rect.height = 'height'
        with self.assertRaises(ValueError):
            rect.height = -1
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_is_valid(self):
        rect = self.rect
        with self.assertRaises(TypeError):
            rect.x = 'x'
        with self.assertRaises(ValueError):
            rect.width = -1

    def test_y_is_valid(self):
        rect = self.rect
        with self.assertRaises(TypeError):
            rect.y = 'y'
        with self.assertRaises(ValueError):
            rect.width = -1

    def test_area_is_accurate(self):
        rect = self.rect
        self.assertEqual(rect.area(), 120)

    def test_str_repr_works(self):
        rect = self.rect
        self.assertEqual(str(rect), "[Rectangle] (3) 2/4 - 12/10")

    def test_update_method_works(self):
        self.rect.update(3, 12, 12, 5, 5)
        rect = self.rect
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.id, 3)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_update_works_with_variable_args(self):
        rect = self.rect
        rect.update(34)
        self.assertEqual(rect.id, 34)
        self.assertEqual(rect.width, 12)

    def test_update_works_with_kwargs(self):
        rect = self.rect
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)
        rect.update(x=10)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 4)
        
    def test_to_dictionary_works(self):
        rect = self.rect
        d = {'id': 3, 'width': 12, 'height': 10, 'x': 2, 'y': 4}
        self.assertEqual(rect.to_dictionary(), d)
