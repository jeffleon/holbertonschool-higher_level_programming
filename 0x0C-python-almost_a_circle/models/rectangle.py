#!/usr/bin/python3
"""Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
        Attributes:
            id (int): the id of the rectangle object.
            __width (int): The width of the rectangle object.
            __height (int): The height of the rectangle object.
            __x (int): The x of the rectangle object.
            __y (int): The y of the rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__: method that initialize an object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width: getter method for the width attribute
        Return:
            The return value: The rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width: setter method for the width attribute
        Args:
            value (int): The width of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less or equal than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height: getter method for the height attribute
        Return:
            The return value: The rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height: setter method for the height attribute
        Args:
            value (int): The height of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less or equal than 0
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x: getter method for the x attribute
        Return:
            The return value: The rectangle's x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x: setter method for the x attribute
        Args:
            x (int): The x of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y: getter method for the y attribute
        Return:
            The return value: The rectangle's y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y: setter method for the y attribute
        Args:
            y (int): The y of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """docstring"""
        return self.__height * self.__width

    def display(self):
        """docstring"""
        print('\n' * self.__y, end='')
        for h in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """docstring"""
        lista = ['id', 'width', 'height', 'x', 'y']
        for en, a in enumerate(args):
            setattr(self, lista[en], a)
        if len(args) <= 0:
            for k, v in kwargs.items():
                for ele in lista:
                    if ele == k:
                        setattr(self, k, v)
                        break

    def __str__(self):
        """docstring"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def to_dictionary(self):
        """docstring"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
