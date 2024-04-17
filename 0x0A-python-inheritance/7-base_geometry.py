#!/usr/bin/python3
''' script to create class have method area '''


class BaseGeometry:
    ''' define class BaseGeometry'''
    def area(self):
        '''
            Calculate the area of the geometric shape.

            Raises:
                Exception: If the area calculation method is not implemented.

            Returns:
                str: A message Exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' method to validate value is integer or not

        Args:
            name(str): always a string
            value(int): value to check is integer and bigger than 0

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less or equal 0

        Returns:
            None
        '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        else if(value <= 0):
            raise ValueError('{} must be greater than 0'.format(name))
