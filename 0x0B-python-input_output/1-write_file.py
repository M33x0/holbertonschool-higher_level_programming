#!/usr/bin/python3
"""Input/Output"""


def write_file(filename="", text=""):
   """ write text in file """
   char_written = 0
   with open(filename, mode='w', encoding='utf-8') as f:
        char_written = f.write(text)
        return char_written