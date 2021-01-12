#!/usr/bin/python3
""" Locked class to prevent dynamic instance """


class LockedClass:
    """ class locked """
    __slots__ = 'first_name'
