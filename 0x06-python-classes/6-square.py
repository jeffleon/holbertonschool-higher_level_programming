#!/usr/bin/python3
""" class Square """


class Square:
    """ constructor of class """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size1=0):
        if type(size1) is int:
            if size1 >= 0:
                self.__size = size1
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        condition1 = type(value[0]) is int and type(value[1]) is int
        condition2 = value[0] >= 0 and value[1] >= 0
        condition3 = len(value) == 2 and type(value) is tuple
        if condition1 and condition2 and condition3:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        if (self.__position[1] > 0):
            print(self.__position[1] * '')
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    if j == 0 and self.position[0] > 0:
                        print(self.position[0] * ' ', end='')
                    print('#', end='')
                print()
        else:
            print()

    def area(self):
        return self.__size * self.__size
