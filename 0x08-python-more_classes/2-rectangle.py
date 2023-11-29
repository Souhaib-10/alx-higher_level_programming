#!/usr/bin/python3
'''class rectangle'''


class Rectangle:
    '''
        instance rectangle
        Attributes:
            width (int) : Triangle width
            height (int): Triangle height
        Raises:
            TypeError : if width not integer
                        if height not integer
            ValueError:if width or height is less than 0
                        if height not integer
    '''

    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        ''' calculate area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''calculate perimeter of the triangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
