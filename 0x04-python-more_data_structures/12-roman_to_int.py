#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    rom_dict = {"M": 1000, "D": 500, "C": 100, "L": 50,"X": 10, "V": 5, "I": 1}
    roman_number = 0
    rest_val = 0
    for i in range(len(roman_string)):
        for key, val in rom_dict.items():
            if key == roman_string[i]:
                roman_number += val
                if rest_val < val:
                    roman_number -= (rest_val * 2)
                    rest_val = val
    return roman_number
