#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionnary = a_dictionary.copy()
    for items in new_dictionnary:
        new_dictionnary[items] = new_dictionnary[items] * 2
    return new_dictionnary
