#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dictionnary_copy = a_dictionary.copy()
    for key in dictionnary_copy:
        if dictionnary_copy[key] == value:
            del a_dictionary[key]
    return a_dictionary
