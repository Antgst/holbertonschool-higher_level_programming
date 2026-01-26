#!/usr/bin/python3

'''Square module.

This module defines a Square class with:
- a private size attribute,
- a property to get/set size with validation,
- an area() method to compute the square's area.
'''


class Square:
    '''Defines a square.

    The square is defined by its size (side length),
    stored as a private attribute
    '''

    def __init__(self, size=0):
        '''Initialize a new Square.

        Args:
        size (int): Size of the square. Default to 0

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        '''
        self.size = size

    @property
    def size(self):
        '''Get the size of the square.

        Returns:
        int: The current size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the square with validation.

        Args: value (int): New size value.

        Raises:
        TypeError: If value is not an integer
        ValueError: If value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''Compute and return the area of the square

        Returns:
        int: The area of the square (size * size)
        '''
        return self.__size * self.__size
