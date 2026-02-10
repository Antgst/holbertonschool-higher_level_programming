#!/usr/bin/python3
'''Module that defines a Student class with JSON serialization and reloading.'''


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
        '''Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes whose names appear in
        attrs are included. Otherwise, all instance attributes are returned.

        Args:
            attrs (list[str] | None): Optional list of attribute
            names to include.

        Returns:
            dict: Dictionary of selected (or all) instance attributes.'''
        if isinstance(attrs, list):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        '''Replace instance attributes using values from a dictionary.

        Args:
            json (dict): Mapping of attribute names to values. Keys
            correspond to
            public attribute names, and values replace the current ones.'''
        for key, value in json.items():
            setattr(self, key, value)
