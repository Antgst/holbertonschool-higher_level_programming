#!/usr/bin/python3
'''Module that provides a function to save a Python object to a JSON file.'''

import json


def save_to_json_file(my_obj, filename):
    '''Write a Python object to a text file using its JSON representation.

    Args:
        my_obj (object): The Python object to serialize to JSON.
        filename (str): Path to the file where the
        JSON content will be written.'''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
