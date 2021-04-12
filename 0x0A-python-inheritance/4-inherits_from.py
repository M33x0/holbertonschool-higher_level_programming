#!/usr/bin/python3
"""Python - Inheritance"""


def inherits_from(obj, a_class):
    """returns True if object is an instance of a class that inherited
    (direct/indirectly)from a class
    ;otherwhise return False """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
