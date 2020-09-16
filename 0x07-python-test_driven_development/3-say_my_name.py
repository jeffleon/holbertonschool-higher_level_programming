#!/usr/bin/python3
"""
Module contain say my name
"""
def say_my_name(first_name, last_name=""):
    """
    Say_my_name function
    """
    errores = {'Typef': 'first_name must be a string',
                'Typel': 'last_name must be a string'}
    if type(first_name) is not str:
        raise TypeError(errores.get('Typef'))
    if type(last_name) is not str:
        raise TypeError(errores.get('Typel'))
    print("My name is {} {}".format(first_name, last_name))
