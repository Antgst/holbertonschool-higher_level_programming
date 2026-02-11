#!/usr/bin/env python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = "" if value is None else str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)
    except (OSError, TypeError, ValueError, ET.ParseError, Exception):
        return None
    return None


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = "" if child.text is None else child.text
        return result
    except (OSError, ET.ParseError, Exception):
        return None
