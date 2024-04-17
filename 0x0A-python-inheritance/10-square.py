#!/usr/bin/python3
''' define class Square inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' class square calculate area of square

    Args:
        size(int):size of square
    '''
    def __init__(self, size):
        '''constructor of class'''

        self.integer_validator("size", size)
        self.__size = size
