#!/usr/bin/python3
"""Input/Output"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file"""
    character_written = 0
    with open(filename, mode='a', encoding='utf-8') as f:
        character_written = f.write(text)
    return character_written