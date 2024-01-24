#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for key, val in copy.items():
        if value == val:
            a_dictionary.pop(key)
    return a_dictionary
