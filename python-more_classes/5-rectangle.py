#!/usr/bin/python3

'''Rectangle module.

This module defines a Rectangle class
'''


class Rectangle:
    '''Defines a rectangle with validated width and height.'''

    def __init__(self, width=0, height=0):
        '''Initialiaze a new Rectangle instance.

        Args:
            Args:
            width (int): Rectangle width (default: 0).
            height (int): Rectangle height (default: 0).

        Raises:
            TypeError: If width/height is not an integer.
            ValueError: If width/height is less than 0.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''int: Get the rectangle width.'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Set the rectangle width.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''int: Get the rectangle height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the rectangle height.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return the area of the rectangle.'''
        return ((self.__height * self.__width))

    def perimeter(self):
        '''Return the perimeter of the rectangle.

        If width or height is 0, the perimeter is 0.'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        '''Return the string representation of the
        rectangle using '#' characters.

        If width or height is 0, return an empty string.'''
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        '''Return a string representation usable with
        eval() to recreate the instance.'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''Print a message when an instance is deleted.'''
        print("Bye rectangle...")
