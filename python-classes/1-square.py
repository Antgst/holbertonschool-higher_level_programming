#!/usr/bin/python3

'''Square module.

This module defines a Square class
'''


class Square:
    '''Defines a square.'''

    def __init__(self, size):
        '''Initialiaze a new Square instance.

        Args:
        size : Size of the square (no type/value validation in this task)'''
        self.__size = size
