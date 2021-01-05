"""Empty module"""


class Square:
    """Define a square shape """
    """ init method is a constructor of the class square"""
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
