#!/usr/bin/python3
'''A test module for testing base model klas'''

import os

from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle


class TestBaseCase(TestCase):
    '''test case for base class'''

    def test_init_works(self):
        b = Base()
        self.assertEqual(b.id, 1)
        c = Base()
        self.assertEqual(c.id, 2)
        d = Base(34)
        self.assertEqual(d.id, 34)

    def test_to_json_string_works(self):
        ret = '{"id": 1, "size": 12, "x": 2, "y": 2}'
        self.assertEqual(Base.to_json_string({'id': 1, 'size': 12, 'x': 2, 'y': 2}), ret)

    def test_to_json_string_works_with_none(self):
        ret = "[]"
        self.assertEqual(Base.to_json_string(None), ret)

    def test_save_to_file_works(self):
        r1 = Rectangle(2,2)
        r2 = Rectangle(4,4)
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        with self.assertRaises(FileNotFoundError):
            with open('Rectangle.json'):
                pass
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists('Rectangle.json'))
        os.remove('Rectangle.json')

    def test_from_json_string_works(self):
        s = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        l = [{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]
        self.assertEqual(Rectangle.from_json_string(s), l)

    def test_from_json_string_works_with_none(self):
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_create_works(self):
        r = Rectangle(3, 5)
        d = r.to_dictionary()
        res = Rectangle.create(**d)
        self.assertDictEqual(d, res.to_dictionary())

    def test_save_to_file_csv_works(self):
        r1 = Rectangle(2,2)
        r2 = Rectangle(4,4)
        if os.path.exists('Rectangle.csv'):
            os.remove('Rectangle.csv')
        with self.assertRaises(FileNotFoundError):
            with open('Rectangle.csv'):
                pass
        Rectangle.save_to_file_csv([r1, r2])
        self.assertTrue(os.path.exists('Rectangle.csv'))
        os.remove('Rectangle.csv')
