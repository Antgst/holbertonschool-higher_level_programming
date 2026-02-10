#!/usr/bin/python3
'''Module that defines a Student class
with a JSON-serializable representation.'''


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

    def to_json(self):
        '''Return the dictionary representation of the Student instance.

        Returns:
            dict: The instance attributes as a dictionary.'''
        return self.__dict__
