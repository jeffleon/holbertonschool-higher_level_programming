#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    res = "is positive"
elif number < 0:
    res = "is negative"
else:
    res = "is zero"
print(str(number) + " " + res)
