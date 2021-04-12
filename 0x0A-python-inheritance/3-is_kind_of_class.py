#!/usr/bin/python3
"""Python - Inheritance"""


def is_kind_of_class(obj, a_class):
    """return True if object is instance
    of/or if the object is an instance
    of a class that inherit """
    if isinstance(obj, a_class):
        return True
    else:
        return False
