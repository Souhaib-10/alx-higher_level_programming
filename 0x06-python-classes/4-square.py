#!/usr/bin/python3
''' square validation class'''


class Square:

    '''initial object from square class


    Args:
        size (int): size square
    '''

    def __init__(self, size):
        ''' change size value '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Return the current area the square.'''
        return (self.__size ** 2)

    @property
    def size(self):
        '''Return current value size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        ''' change size value '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
