#!/usr/bin/python3
''' define base class'''
import json


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write convert json of a list to a file
        Args:
        list_objs (list): A list object inhertied
        """
        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as jf:
            if list_objs is None:
                jf.write('[]')
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jf.write(Base.to_json_string(list_dicts))
