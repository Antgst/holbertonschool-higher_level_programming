#!/usr/bin/python3

''''''


class Square:

    def __init__(self, size=0, position=(0, 0)):
        ''''''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        ''''''
        return self.__size

    @size.setter
    def size(self, value):
        ''''''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return self.size == value

    @property
    def position(self):
        ''''''
        return self.__position

    @position.setter
    def position(self, value):
        ''''''
        if (
            not isinstance(value, tuple)
            or isinstance(value[0], int)
            or isinstance(value[1], int)
            or len(value) != 2
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''''''
        return self.__size * self.__size

    def my_print(self):
        size = self.__size
        position = self.__position
        for i in range(position[1]):
            print()
        if size == 0:
            print()
        else:
            for i in range(size):
                print(position[0] * ' ' + '#' * size)
