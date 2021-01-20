#!/usr/bin/python3
"""Input/Output """
import json


def from_json_string(my_str):
    """returns an object(Python DS) represented by a JSON string"""
    return json.loads(my_str)
