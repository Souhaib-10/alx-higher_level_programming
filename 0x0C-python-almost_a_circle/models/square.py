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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        text = "[Square] ({}) {}/{} ".format(self.id, self.x, self.y)
        text += "- {}".format(self.width)
        return text

    def update(self, *args, **kwargs):
        ''' update Attributes.
        Args:
            *args(ints):Many attribute values writed
            **kwargs(dict): Key/Value  update attribute
        '''
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)
