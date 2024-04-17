#!/usr/bin/python3
''' define class Rectangle inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' contructor of Rectangle class

    Args:
        width(int):value width of rectangle
        height(int):value hight of rectangle
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''
        Return:
            area of rectangle (int)
        '''
        return self.__width * self.__height

    def __str__(self):
        ''' return width/hight rectangle'''
        return "[Rectangle]{}/{}".format(self.__width, self.__height)
