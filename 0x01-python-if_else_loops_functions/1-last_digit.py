#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_ = str(number)[-1]
str_1 = "Last digit of {:d} is {} ".format(number, last_)
if int(last_) > 5:
    str_2 = "and is greater than 5"
elif int(last_) < 6 and int(last_) != 0:
    str_2 = "and is less than 6 and not 0"
else:
    str_2 = "and is 0"
print("{}{}".format(str_1,str_2))
