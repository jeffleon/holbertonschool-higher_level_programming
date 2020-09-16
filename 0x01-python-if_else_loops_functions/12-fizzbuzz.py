#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            str_ = "FizzBuzz"
        elif i % 5 == 0:
            str_ = "Buzz"
        elif i % 3 == 0:
            str_ = "Fizz"
        else:
            str_ = str(i)
        print(str_, end=' ')
