#!/usr/bin/python3
''' define base class'''


class Base:
    '''define the base class with attributes and methods'''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' constructor  of the class
        Args:
        id (int): an identifier for this object.
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Return the json serialization of list
        Args:
            list_dictionaries (list): A list of dict
        '''
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)
