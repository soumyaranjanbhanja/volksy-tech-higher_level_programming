#!/usr/bin/python3
"""class"""


class Square:
    """Square is class"""
    def __init__(self, size=0):
        """Constructer"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size    
    def area(self):    
        ar = self.__size * self.__size
        return ar
