#!/usr/bin/python3
'''Module that provides a function to create a
Python object from a JSON file.'''

import json


def load_from_json_file(filename):
    '''Create and return a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        object: The Python object represented by the JSON content.'''
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
