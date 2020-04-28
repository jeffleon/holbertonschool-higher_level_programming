#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            num = ord(i) - 32
        else:
            num = ord(i)
        print('{:c}'.format(num), end='')
    print()
