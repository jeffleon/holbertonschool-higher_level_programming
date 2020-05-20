#!/usr/bin/python3
""" class Square """


class Square:
    """ constructor of class """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ the Geeter of size """
        return self.__size

    @size.setter
    def size(self, size1=0):
        """ the Setter of size """
        if type(size1) is int:
            if size1 >= 0:
                self.__size = size1
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        """ the Getter of position """
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        """ the Setter of position """
        if (
                not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0
        ):

            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size > 0:
            if (self.__position[1] > 0):
                for i in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

    def area(self):
        return self.__size * self.__size
