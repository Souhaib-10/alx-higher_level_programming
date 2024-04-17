#!/usr/bin/python3
''' define class Rectangle inherits from BaseGeometry'''


class Rectangle(BaseGeometry):
    ''' contructor of Rectangle class

    Args:
        width(int):value width of rectangle
        height(int):value hight of rectangle
    
    '''
    def __init__(self,width,height):
        self.integer_validator("width", width)
        self__width = width
        self.integer_validator("height", height)
        self.__height = height
    
