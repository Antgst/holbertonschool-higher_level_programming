#!/usr/bin/python3

'''Square module.

This module defines a Square class that supports:
- size validation via a property,
- area computation,
- printing the square using `#`.'''


class Square:
    '''
    Defines a square by its size.

    The size is stored as a private attribute and exposed through a property
    that validates assignments.
    '''

    def __init__(self, size=0):
        '''
        Initialize a new Square.

        Args:
            size (int): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        self.__size = size

    @property
    def size(self):
        '''
        Get the size of the square.

        Returns:
            int: The current size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Set the size of the square with validation.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Compute and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''
        Print the square using the `#` character.

        Prints nothing if size is 0.
        '''
        if self.__size == 0:
            return
        for i in range(self.__size):
            print("#" * self.__size)
