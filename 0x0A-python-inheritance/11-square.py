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

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''rectangle square'''

        return self.__size * self.__size

    def __str__(self):
        ''' return resultat tp print '''

        return "[Square] {}/{}".format(self.__size, self.__size)
