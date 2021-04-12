#!/usr/bin/python3
"""Input/Output """


def read_file(filename=""):
    """ read text file (utf8) and print it to stdout """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")
