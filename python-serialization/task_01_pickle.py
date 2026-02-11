#!/usr/bin/env python3
'''Module that provides basic JSON serialization and
deserialization for dictionaries.'''

import json


def serialize_and_save_to_file(data, filename):
    '''Serialize a Python dictionary to JSON and save it to a file.

    The output file is created if it doesn't exist and replaced if it does.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): Path to the output JSON file.'''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    '''Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): Path to the input JSON file.

    Returns:
        dict: Dictionary obtained from the JSON content.'''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
