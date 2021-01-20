#!/usr/bin/python3
"""Input/Output """


def class_to_json(obj):
    """return dictionary of attribute of the obj"""
    return obj.__dict__
