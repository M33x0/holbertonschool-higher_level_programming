#!/usr/bin/python3
"""Input/Output """


def append_write(filename="", text=""):
    """append a string to a text file """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
