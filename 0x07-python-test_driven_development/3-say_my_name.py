#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    errores = {'Typef': 'first_name must be a string',
                'Typel': 'first_name must be a string'}
    if type(first_name) is not str:
        raise TypeError(errores.get('Typef'))
    if type(last_name) is not str:
        raise TypeError(errores.get('Typel'))
    print("My name is {} {}".format(first_name, last_name))
