#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        ''' print the rectangle with the character #, taking care of x and y'''
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        '''
        Returns a string representation of the rectangle.

        Example:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        text = "[Rectangle] ({}) {}/{} ".format(self.id, self.__x, self.__y)
        text += "- {}/{}".format(self.__width, self.__height)
        return text

    def update(self, *args, **kwargs):
        ''' update Attributes.
        Args:
            *args(ints):Many attribute values writed
            **kwargs(dict): Key/Value  update attribute
        '''
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        ''' Return the dictionary of attr with it's numbers'''
        return {
                "x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width
                }
