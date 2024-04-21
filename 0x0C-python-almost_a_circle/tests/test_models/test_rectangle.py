#!/usr/bin/python3
''' test rectangle class'''

import unittest
from models.rectangle import Rectangle
import io
import contextlib


class TestRectangle(unittest.TestCase):
    ''' define cases for testing class'''
    def test_display(self):
        '''Test display method '''
        r1 = Rectangle(2, 2)
        r2 = Rectangle(4, 6)
        expected_output = "##\n##\n"
        expected_output2 = "####\n####\n####\n####\n####\n####\n"
        with io.StringIO() as buf1, io.StringIO() as buf2:
            with contextlib.redirect_stdout(buf1):
                r1.display()
            with contextlib.redirect_stdout(buf2):
                r2.display()
            self.assertEqual(buf1.getvalue(), expected_output)
            self.assertEqual(buf2.getvalue(), expected_output2)

    def test_constuctor(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, r2.id-1)
        self.assertEqual(r2.id, r1.id+1)
        self.assertEqual(r3.id, 12)

    def test_raises_exception(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
            r = Rectangle(10, 2)
            r.width = "test"
            r = Rectangle(10, 2)
            r.x = {}
            Rectangle(10, 2, "x", 1)
            Rectangle(10, 2, 1, "y")
        with self.assertRaises(ValueError):
            Rectangle(-10, 10)
            Rectangle(10, -10)
            Rectangle(10, 2, -3, 1)
            Rectangle(10, 2, 3, -1)

    def test_getters(self):
        r = Rectangle(10, 2, 1, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


if __name__ == "__main__":
    unittest.main()
