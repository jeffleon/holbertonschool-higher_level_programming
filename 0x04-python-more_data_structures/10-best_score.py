#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = max(a_dictionary.values())
        key = list(a_dictionary.keys())[list(a_dictionary.values()).index(val)]
    else:
        return None
    return key
