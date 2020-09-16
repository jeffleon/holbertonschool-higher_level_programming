#!/usr/bin/python3
"""
This module print a square
"""
def print_square(size):
    """
    This function print a squre
    and if size is not a int dont work
    """
    errores = {'Type': 'size must be an integer',
                'Zero': 'size must be >= 0'}
    if not isinstance(size, (float, int)):
        raise TypeError(errores.get('Type'))
    if size < 0:
        raise ValueError(errores.get('Zero'))
    if type(size) is float and size < 0:
        raise TypeError(errores.get('Type'))
    if type(size) is float:
        size = int(size)
    for i in range(size):
        print('#' * size)
