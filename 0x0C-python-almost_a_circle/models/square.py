#!/usr/bin/python3
''' script to create class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' define class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor class
        Args:
            size (int): Size of square
            x (int): The x coordinate of square
            y (int): The y coordinate of square
            id (int): The identifier of square
        '''
        super().__init(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        text = "[Square] ({}) {}/{} ".format(self.id, self.__x, self.__y)
        text += "- {}/{}".format(self.__width, self.height)
        return text
