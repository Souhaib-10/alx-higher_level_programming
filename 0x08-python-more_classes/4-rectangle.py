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

    def __init__(self, width=0, height=0):
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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        ''' calculate area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''calculate perimeter of the triangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''return string representation of object'''
        if self.__height == 0 or self.__height == 0:
            return " "
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if (i == self.__height-1):
                break
            print()
        return " "

    def __repr__(self):
        '''return string representation of object'''
        return ("Rectangle({}, {})".format(self.__width, self.__height))
