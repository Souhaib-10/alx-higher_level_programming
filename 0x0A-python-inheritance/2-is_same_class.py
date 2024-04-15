#!/usr/bin/python3
''' function that return true or false if object instance class'''


def is_same_class(obj, a_class):
    '''
    check if obj is  an instance of class 'a_class' or one of its subclasses.

    Attributes:
        obj (object) : the object to be checked.
        a_class (type) : the class against which obj will be checked.

    Returns:
        bool : True if obj is an instance of 'a_class'
    '''
    if obj.isinstance(a_class):
        return True
    return False
