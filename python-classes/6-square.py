#!/usr/bin/python3

'''Defines a Square class with size and position.

This module provides a Square class that supports:
- size validation (non-negative integer)
- position validation (tuple of 2 non-negative integers)
- area computation
- printing the square with '#' offset by position
'''


class Square:
    '''Represents a square with a given size and a printing position offset.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a Square instance.

        Args:
            size (int): Size of the square side (must be >= 0).
            position (tuple): A tuple of 2 non-negative integers (x, y) used
                as the printing offset.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
            TypeError: If position is not a tuple
            of 2 non-negative integers.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Get the current size of the square.

        Returns:
            int: The square size.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the square size.

        Args:
            value (int): New size (must be an integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Get the current position offset.

        Returns:
            tuple: The position (x, y) offset used when printing the square.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''Set the position offset.

        Args:
            value (tuple): A tuple of 2 non-negative integers (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 non-negative integers.
        '''
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Compute the area of the square.

        Returns:
            int: The square area (size * size).
        '''
        return self.__size * self.__size

    def my_print(self):
        '''Print the square to stdout using '#', offset by position.

        If size is 0, prints an empty line.
        Otherwise:
        - prints position[1] empty lines first
        - then prints size lines of (position[0] spaces + size '#')
        '''
        size = self.__size
        position = self.__position

        if size == 0:
            print()
            return
        for i in range(position[1]):
            print()
        for i in range(size):
            print(position[0] * ' ' + '#' * size)
