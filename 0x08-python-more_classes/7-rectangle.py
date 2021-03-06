#!/usr/bin/python3

"""Rectangle"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """print a object"""
        rect = ''
        if self.__height == 0 or self.__width == 0:
            return rect
        for col in range(self.__height):
            for row in range(self.__width):
                rect += str(self.print_symbol)
            if col == self.__height - 1:
                break
            else:
                rect += '\n'
        return rect

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Width"""
        if (type(value) is not int):
            raise TypeError('width must be an integer')
        elif (value < 0):
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height"""
        if (type(value) is not int):
            raise TypeError('height must be an integer')
        elif (value < 0):
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))
