#!/usr/bin/python3

'''Square module.

This module defines a Square class with size validation.
'''


class Square:
    '''
    Defines a square by its size

    Attributes:
    __size (int): Size of the square (private)
    '''
    def __init__(self, size=0):
        '''Initialize a new Square

        Args:
        Size (int): Size of the square. Default to 0

        Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
