#!/usr/bin/python3
"""Input/Output """


def append_write(filename="", text=""):
   """append a text file and return numbers character written """
   number_of_characters = 0
   with open(filename, 'a', encoding='utf-8') as f:
           number_of_characters = f.write(text)
   return number_of_characters
