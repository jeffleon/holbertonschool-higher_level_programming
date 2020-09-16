#!/usr/bin/python3
"""Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """docstring"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """docstring"""
        return self.width

    @size.setter
    def size(self, value):
        """docstring"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """docstring"""
        lista = ['id', 'size', 'x', 'y']
        for en, a in enumerate(args):
            setattr(self, lista[en], a)
        if len(args) <= 0:
            for k, v in kwargs.items():
                for ele in lista:
                    setattr(self, k, v)
                    break

    def to_dictionary(self):
        """docstring"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
