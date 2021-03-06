#!/usr/bin/python3
"""Module Base"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """docstring"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """docstring"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """docstring"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """docstring"""
        list_dict = list()
        if list_objs is not None:
            for el in list_objs:
                list_dict.append(el.to_dictionary())
        json_f = cls.to_json_string(list_dict)
        name = cls.__name__
        with open("{}.json".format(name), encoding='utf-8', mode='w') as f:
            f.write(json_f)

    @classmethod
    def create(cls, **dictionary):
        """docstring"""
        if cls.__name__ == 'Rectangle':
            sol = cls(1, 1)
        elif cls.__name__ == 'Square':
            sol = cls(1)
        sol.update(**dictionary)
        return sol

    @classmethod
    def load_from_file(cls):
        """docstring"""
        try:
            with open('{}.json'.format(cls.__name__), 'r') as file:
                str = file.read()
        except IOError:
            return []
        lista = cls.from_json_string(str)
        lista_flag = list()
        for el in lista:
            arreglos = cls.create(**el)
            lista_flag.append(arreglos)
        return lista_flag

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """docstring"""
        cadena = ''
        for el in list_objs:
            if cls.__name__ == 'Rectangle':
                cadena += '{},{},{},{},{}\n'.format(el.id, el.width,
                                                    el.height, el.x, el.y)
            elif cls.__name__ == 'Square':
                cadena += '{},{},{},{}\n'.format(el.id, el.size, el.x,
                                                 el.y)
        with open('{}.csv'.format(cls.__name__), 'w+') as f:
            f.write(cadena)

    @classmethod
    def load_from_file_csv(cls):
        """docstring"""
        lista = []
        filename = '{}.csv'.format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                for line in f:
                    mat = line.split(sep=',')
                    if len(mat) == 5:
                        sol = cls(int(mat[1]), int(mat[2]), int(mat[3]),
                                  int(mat[4]), int(mat[0]))
                    elif len(mat) == 4:
                        sol = cls(int(mat[1]), int(mat[2]), int(mat[3]),
                                  int(mat[0]))
                    lista.append(sol)
            return lista
        except IOError:
            return []
