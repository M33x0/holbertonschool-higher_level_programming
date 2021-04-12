#!/usr/bin/python3
"""Python - Inheritance"""


def is_same_class(obj, a_class):
    """return True if object is instance of a class """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
