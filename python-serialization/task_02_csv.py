#!/usr/bin/env python3
'''Module that converts a CSV file into a JSON file using serialization.'''

import csv
import json


def convert_csv_to_json(csv_filename):
    '''Convert CSV data to JSON and write it to a file named 'data.json'.

    The CSV is read with csv.DictReader so each row becomes a dictionary.
    The resulting list of dictionaries is serialized to JSON and written to
    'data.json'.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True if the conversion succeeds, False if an exception occurs
        (for example, if the CSV file does not exist).'''
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
