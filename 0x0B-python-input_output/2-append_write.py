#!/usr/bin/python3
"""Function that open/write and append a file"""


def append_write(filename="", text=""):
    """ Open/write append text in filename"""
    character_written = 0
    with open(filename, mode='a', encoding='utf-8') as f:
        character_written = f.write(text)
    return character_written