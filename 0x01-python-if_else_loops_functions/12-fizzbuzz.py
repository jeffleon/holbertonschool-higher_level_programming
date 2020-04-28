#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            str_ = "fizzbuzz"
        elif i % 5 == 0:
            str_ = "buzz"
        elif i % 3 == 0:
            str_ = "fizz"
        else:
            str_ = str(i)
        print(str_, end=' ')
fizzbuzz()
