#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str1 = str[str.find('object'):str.find('language')]
str = str1 + str[str.find('with'):str.find('with') + 5] + str[:6]
print(str)
