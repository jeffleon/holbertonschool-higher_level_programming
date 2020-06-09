#!/usr/bin/python3
"""Module Base"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dict = list()
        for el in list_objs:
            list_dict.append(el.to_dictionary())
        json_f = cls.to_json_string(list_dict)
        with open("{}.json".format(cls.__name__), 'w+') as file:
            file.write(json_f)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            sol = cls(1, 1)
        elif cls.__name__ == 'Square':
            sol = cls(1)
        sol.update(**dictionary)
        return sol

    @classmethod
    def load_from_file(cls):
        with open('{}.json'.format(cls.__name__), 'r') as file:
            str = file.read()
        lista = cls.from_json_string(str)
        lista_flag = list()
        for el in lista:
            arreglos = cls.create(**el)
            lista_flag.append(arreglos)
        return lista_flag
