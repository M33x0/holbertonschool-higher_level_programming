#!/usr/bin/python3


class Mylist(list):
    """Mylist inherit from list"""

    def print_sorted(self):
        """prints sorted list"""
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
