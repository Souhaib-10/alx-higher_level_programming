#!/usr/bin/python3
''' Use unittest for test base class'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Define test case for base model'''

    def test_constructor(self):
        base_test = Base()
        base_test2 = Base()
        base_test3 = Base(5)
        self.assertEqual(base_test.id, 1)
        self.assertEqual(base_test2.id, 2)
        self.assertEqual(base_test3.id, 5)


    if __name__ == '__main__':
        unittest.main()
