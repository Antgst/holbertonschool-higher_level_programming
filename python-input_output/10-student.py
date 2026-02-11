#!/usr/bin/python3
'''Module that defines a Student class with optional JSON attribute filtering.'''


class Student:
    '''Represents a student with basic identifying information.'''
    def __init__(self, first_name, last_name, age):
        '''Initialize a Student with first name, last name, and age.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Return a dictionary representation of the Student instance.'''
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
