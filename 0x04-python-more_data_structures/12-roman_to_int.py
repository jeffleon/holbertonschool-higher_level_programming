#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50,
                  "X": 10, "V": 5, "I": 1}
    roman_number = 0
    for letter in roman_string:
        if letter in roman_dict:
            roman_number += roman_dict[letter]
    return roman_number
