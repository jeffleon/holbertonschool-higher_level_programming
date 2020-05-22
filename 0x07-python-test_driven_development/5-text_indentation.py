#!/usr/bin/python3
def text_indentation(text):
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
        elif letter is ':' or letter is '.' or letter is '?':
            print(letter)
            print()
            aux = 1
        else:
            print(letter, end='')
            aux = 0
