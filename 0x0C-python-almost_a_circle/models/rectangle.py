#!/usr/bin/python3
''' define class rectangle inherit from class base '''
from models.base import Base


class Rectangle(Base):
    ''' script class Rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor of class Rectangle
        Args:
            width (int):  the initial width of rectangle.
            height (int): the initial height of rectangle.
            x (int):      the x-coordinate
            y (int):      the y-coordinate
            id (int) :     unique identifier for this object
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        '''

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        if(not isinstance(self.__width, int)):
            raise(TypeError("width must be an integer."))
        if(not isinstance(self.__height, int)):
            raise(TypeError("height must be an integer"))
        if(not isinstance(self.__x, int)):
            raise(TypeError("x must be an integer"))
        if(not isinstance(self.__y, int)):
            raise TypeError("y must be an integer")
        if(self.__width <= 0):
            raise ValueError('width must be > 0')
        if (self.__height <= 0):
            raise ValueError('height must be > 0')
        if (self.__x < 0):
            raise ValueError('x must be >= 0')
        if (self.__y < 0):
            raise ValueError('y must be >= 0')

    @property
    def width(self):
        ''' Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter for width '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter for height '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' Getter for height'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' Setter for x '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' Setter for x '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Return the area of the rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' print the rectangle with the character #, taking care of x and y'''
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        ''' Return rectangle message '''
        text = "[Rectangle] ({}) {}/{} ".format(self.id, self.__x, self.__y)
        text += "- {}/{}".format(self.__width, self.height)
        return text
