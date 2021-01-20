#!/usr/bin/python3
"""insert line of text to a file after """


def append_after(filename="", search_string="", new_string=""):
    """ append_after """
    line = ""
    with open(filename, mode='r', encoding='utf-8') as p:
        line = p.readlines()
    with open(filename, mode='w', encoding='utf-8') as f:
        for i in line:
            if search_string in i:
                i += new_string
            f.write(i)
