#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_ = number % 10 if number > 0 else ((number * -1) % 10) * -1
str_1 = "Last digit of {:d} is {:d} ".format(number, last_)
if last_ > 5:
    str_2 = "and is greater than 5"
elif last_ < 6 and last_ != 0:
    str_2 = "and is less than 6 and not 0"
else:
    str_2 = "and is 0"
print("{}{}".format(str_1, str_2))
