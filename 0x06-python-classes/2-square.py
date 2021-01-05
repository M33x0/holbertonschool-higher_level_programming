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
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
