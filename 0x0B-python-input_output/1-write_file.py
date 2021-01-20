#!/usr/bin/python3
"""Input/Output"""


def write_file(filename="", text=""):
   """write a string to a text file and return 
   numbers character written """
   number_of_characters = 0
   with open(filename, mode='w', encoding='utf-8') as f:
        number_of_characters = f.write(text)
   return number_of_characters