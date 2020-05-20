#!/usr/bin/python3
""" class Square """
class Square:
    """ constructor of class """
    def __init__(self, size=0):
        self.size = size

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

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

    def area(self):
        return self.__size * self.__size
