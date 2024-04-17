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
