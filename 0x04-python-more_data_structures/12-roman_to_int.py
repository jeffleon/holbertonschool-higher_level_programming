#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    if (not roman_string) or (type(roman_string) != str):
        return 0

    for letter in range(len(roman_string)):
        if letter == len(roman_string) - 1:
            total += rom[roman_string[letter]]
        elif rom[roman_string[letter]] >= rom[roman_string[letter + 1]]:
            total += rom[roman_string[letter]]
        else:
            total -= rom[roman_string[letter]]
    return total
