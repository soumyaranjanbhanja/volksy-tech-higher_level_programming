#!/usr/bin/python3
"""class"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """constructer"""
        self.size = size

    @property
    def size(self):
        """decorator"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method"""
        a = self.__size * self.__size
        return a
