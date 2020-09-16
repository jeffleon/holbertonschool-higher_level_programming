#!/usr/bin/python3
"""
a function of text_indentation
"""
def text_indentation(text):
    """
    if is not a text raise a error and if
    the test is empty
    """
    aux = 0
    if type(text) is not str:
        raise TypeError('must be a string')
    if text == None:
        print(end='')
        return None
    for letter in text:
        if aux == 1 and letter is ' ':
            print('', end='')
            aux = 0
            continue
        if letter is ':' or letter is '.' or letter is '?':
            print("{}\n".format(letter))
            aux = 1
        else:
            print(letter, end='')
            aux = 0
