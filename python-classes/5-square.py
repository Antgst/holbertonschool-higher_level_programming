#!/usr/bin/python3

'''TEST DOC'''


class Square:
    '''
    Docstring pour Square
    '''

    def __init__(self, size=0):
        '''
        Docstring pour __init__

        :param self: Description
        :param size: Description
        '''
        self.__size = size

    @property
    def size(self):
        '''
        Docstring pour size

        :param self: Description
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Docstring pour size

        :param self: Description
        :param value: Description
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Docstring pour area

        :param self: Description
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''
        Docstring pour my_print

        :param self: Description
        '''
        if self.__size == 0:
            return
        for i in range(self.__size):
            print("#" * self.__size)
