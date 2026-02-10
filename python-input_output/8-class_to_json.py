#!/usr/bin/python3
'''Module that provides a function to get a JSON-serializable
dict description of an object.'''


def class_to_json(obj):
    '''Return the dictionary description of an object for JSON serialization.

    Args:
        obj (object): An instance of a class with JSON-serializable attributes.

    Returns:
        dict: The instance attributes of `obj` as a dictionary.'''
    return obj.__dict__
