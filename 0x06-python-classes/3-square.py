#!/usr/bin/python3
"""Empty module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize
        Args:
            size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current square area"""
        return self.__size * self.__size
