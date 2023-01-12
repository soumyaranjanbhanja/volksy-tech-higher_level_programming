#!/usr/bin/python3
"""class"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """constructer"""
        self.size = size

    @property
    def size(self):
        """Decorator"""
        return self.__size

    @size.setter
    def size(self, value):
        """Decorator"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        a = self.__size * self.__size
        return a

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
