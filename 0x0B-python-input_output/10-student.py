#!/usr/bin/python3
"""Class student"""


class Student:
    """Class of a student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionnary of all the attributes"""
        if type(attrs) == list:
            dictionnary = {}
            dictionnary_attributes = self.__dict__
            for key in attrs:
                if not type(key) == str:
                    return self.__dict__
                for name in dictionnary_attributes :
                    if key == name:
                        dictionnary[key] = dictionnary_attributes[name]
            return dictionnary
        return self.__dict__
