#!/usr/bin/python3
"""Input/Output """


def append_write(filename="", text=""):
    """append a text file and return numbers character written """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)

